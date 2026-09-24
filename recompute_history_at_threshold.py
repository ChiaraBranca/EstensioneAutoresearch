"""
=============================================================================
FILE: recompute_history_at_threshold.py
DESCRIPTION:
Batch version of threshold_replay.py: rewrites an ENTIRE metrics_history.jsonl
so that precision/recall/f1/accuracy reflect a chosen RELEVANCE_THRESHOLD,
using the already-archived cosine_scores_<timestamp>.json files - WITHOUT
re-running any cycle. This is useful when earlier cycles were logged under a
threshold you have since revised (e.g. 0.58), and you want a single, internally
consistent history file at the new threshold (e.g. 0.50) for both LSS-weight
tuning and reporting in the thesis.

C, N, V, I, baseline_score, new_score, committed, topic, cycle and timestamp
are copied through UNCHANGED (they do not depend on the Oracle threshold at
all). Only precision/recall/f1/accuracy are recomputed, and an
"oracle_threshold" field is written (or overwritten) to record which
threshold was used for that row, keeping the resulting history file
self-documenting.

HOW CYCLES ARE MATCHED TO ARCHIVED FILES:
loop.py logs one line to metrics_history.jsonl and archives one
cosine_scores_<timestamp>.json per cycle, moments later, for every topic. In
practice eval_logs/ can contain MORE archived files than logged history
entries (e.g. leftover files from standalone auto_evaluator.py runs done for
manual threshold testing, or from cycles run before metrics_history logging
existed) - so pairing by list position is unsafe. Instead, each history
entry is matched to the archived cosine_scores file whose filename timestamp
is CLOSEST to that entry's own timestamp (greedy nearest-match, processed in
chronological order, each archived file used at most once). This correctly
ignores extra/stray files that don't correspond to any logged entry, as long
as the true match is closer in time than any stray file - which holds in
practice since archiving happens only seconds after logging in the same
cycle. A per-topic summary line reports how many entries were matched vs.
left over, and the match delta (in seconds) is stored per entry for a quick
sanity check.

The confusion matrix for each recomputed row is computed against the topic's
CURRENT references.bib (there is no historical bib snapshot saved per cycle;
using the current one is a safe approximation because papers cited in a given
cycle are not later un-cited except in the same cycle's own critic pass - see
program.md's review rules).

Usage:
  python recompute_history_at_threshold.py <metrics_history.jsonl> <threshold> [surveys_dir]

Example:
  python recompute_history_at_threshold.py metrics_history.jsonl 0.50
  (writes metrics_history_at_0.50.jsonl next to the input file)
=============================================================================
"""
import sys
import os
import json
import re
import glob
from datetime import datetime


def clean_id(raw_id):
    return re.sub(r'v\d+$', '', str(raw_id).strip())


def get_integrated_papers(bib_file):
    if not os.path.exists(bib_file):
        return set()
    with open(bib_file, "r", encoding="utf-8") as f:
        content = f.read()
    ids = set(re.findall(r'@\w+\{([^,]+),', content))
    return {clean_id(i) for i in ids}


def confusion_at_threshold(scores, integrated, threshold):
    TP = FP = FN = TN = 0
    for paper_id, score in scores.items():
        base_id = clean_id(paper_id)
        is_relevant_gt = 1 if score >= threshold else 0
        is_relevant_ai = 1 if base_id in integrated else 0
        if is_relevant_ai == 1 and is_relevant_gt == 1:
            TP += 1
        elif is_relevant_ai == 1 and is_relevant_gt == 0:
            FP += 1
        elif is_relevant_ai == 0 and is_relevant_gt == 1:
            FN += 1
        else:
            TN += 1
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0.0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0.0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
    accuracy = (TP + TN) / len(scores) if scores else 0.0
    return precision, recall, f1, accuracy


def find_topic_dir(surveys_dir, topic):
    """Topic names in metrics_history.jsonl are as passed on the command line
    (e.g. 'Quantum_Computing'), but the folder is the sanitized clean_name
    prepare.py uses (lowercased, non-alnum -> '_'). Recreate that mapping."""
    clean_name = re.sub(r'[^a-zA-Z0-9]', '_', topic.lower()).strip('_')
    return os.path.join(surveys_dir, clean_name)


def parse_archive_timestamp(filepath):
    """Extract the datetime encoded in 'cosine_scores_YYYYMMDD_HHMMSS.json'."""
    m = re.search(r'cosine_scores_(\d{8}_\d{6})\.json$', os.path.basename(filepath))
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1), "%Y%m%d_%H%M%S")
    except ValueError:
        return None


def match_entries_to_files(topic_entries, score_files):
    """Greedy nearest-timestamp matching: process history entries in
    chronological order, each claims the not-yet-used archived file whose
    timestamp is closest to its own (archive filenames only have
    second-level precision, history timestamps have microsecond precision,
    so exact ordering can't be relied on - distance is more robust than a
    strict 'must be later than' rule). Returns a list of
    (entry, matched_filepath_or_None, abs_delta_seconds_or_None).
    """
    file_times = [(f, parse_archive_timestamp(f)) for f in score_files]
    file_times = [(f, t) for f, t in file_times if t is not None]

    entries_with_time = []
    for e in topic_entries:
        try:
            entries_with_time.append((e, datetime.fromisoformat(e["timestamp"])))
        except (KeyError, ValueError):
            entries_with_time.append((e, None))
    entries_with_time.sort(key=lambda pair: (pair[1] is None, pair[1]))

    used = set()
    results = []
    for entry, entry_time in entries_with_time:
        if entry_time is None:
            results.append((entry, None, None))
            continue
        best_file, best_delta = None, None
        for f, t in file_times:
            if f in used:
                continue
            delta = abs((t - entry_time).total_seconds())
            if best_delta is None or delta < best_delta:
                best_file, best_delta = f, delta
        if best_file is not None:
            used.add(best_file)
        results.append((entry, best_file, best_delta))
    return results


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    history_path = sys.argv[1]
    new_threshold = float(sys.argv[2])
    surveys_dir = sys.argv[3] if len(sys.argv) > 3 else "surveys"

    with open(history_path, "r", encoding="utf-8") as f:
        entries = [json.loads(line) for line in f if line.strip()]

    by_topic = {}
    for e in entries:
        by_topic.setdefault(e.get("topic", "<unknown>"), []).append(e)

    updated = []
    for topic, topic_entries in by_topic.items():
        topic_dir = find_topic_dir(surveys_dir, topic)
        bib_file = os.path.join(topic_dir, "references.bib")
        eval_logs_dir = os.path.join(topic_dir, "eval_logs")

        score_files = sorted(glob.glob(os.path.join(eval_logs_dir, "cosine_scores_*.json")))

        if not score_files:
            print(f"[WARNING] '{topic}': no archived cosine_scores files found in "
                  f"{eval_logs_dir} - skipping (leaving its rows unchanged).")
            updated.extend(topic_entries)
            continue

        integrated = get_integrated_papers(bib_file)
        if not integrated:
            print(f"[WARNING] '{topic}': references.bib not found or empty at "
                  f"{bib_file} - skipping (leaving its rows unchanged).")
            updated.extend(topic_entries)
            continue

        if len(score_files) != len(topic_entries):
            print(f"[INFO] '{topic}': {len(topic_entries)} history entries vs "
                  f"{len(score_files)} archived files - using nearest-timestamp "
                  f"matching (extra/stray files will be ignored).")

        matches = match_entries_to_files(topic_entries, score_files)
        matched_count = 0
        for entry, score_file, delta in matches:
            if score_file is None:
                print(f"  [SKIP] {topic} cycle {entry.get('cycle')} @ {entry.get('timestamp')}: "
                      f"no unused archived file left to match - leaving this row unchanged.")
                updated.append(entry)
                continue
            if delta is not None and delta > 300:
                print(f"  [CAUTION] {topic} cycle {entry.get('cycle')}: nearest match is "
                      f"{delta:.0f}s away ({os.path.basename(score_file)}) - double-check this "
                      f"pairing is correct.")
            with open(score_file, "r", encoding="utf-8") as f:
                scores = json.load(f)
            precision, recall, f1, accuracy = confusion_at_threshold(scores, integrated, new_threshold)
            new_entry = dict(entry)
            new_entry["precision"] = precision
            new_entry["recall"] = recall
            new_entry["f1"] = f1
            new_entry["accuracy"] = accuracy
            new_entry["oracle_threshold"] = new_threshold
            new_entry["_recomputed_from"] = os.path.basename(score_file)
            new_entry["_match_delta_seconds"] = round(delta, 1) if delta is not None else None
            updated.append(new_entry)
            matched_count += 1

        unused_files = len(score_files) - matched_count
        print(f"[OK] '{topic}': recomputed {matched_count}/{len(topic_entries)} cycle(s) at "
              f"threshold {new_threshold:.2f} ({unused_files} archived file(s) unused/stray)")

    out_path = os.path.splitext(history_path)[0] + f"_at_{new_threshold:.2f}.jsonl"
    with open(out_path, "w", encoding="utf-8") as f:
        for e in updated:
            f.write(json.dumps(e) + "\n")

    print(f"\nWrote {len(updated)} entries to {out_path}")
    print("Use this file with tune_lss.py --tune instead of the original metrics_history.jsonl.")