"""
=============================================================================
FILE: tune_lss.py
DESCRIPTION:
Standalone diagnostic / tuning tool for the Living Survey Score (LSS) formula
defined in prepare.py:

  score = (wC * C) + (wN * N)

Two modes:

  --sensitivity "<Topic>"
      Recomputes the current C and N for a topic and shows how the score
      moves across the full range of wC (0 to 1, wN = 1 - wC). Diagnostic
      only, no ground truth needed.

  --tune [metrics_history.jsonl] [--metric f1|precision|recall|accuracy]
      Reads a JSONL history file (one line per cycle) and finds the wC/wN
      split that best agrees with real quality changes (measured by the
      chosen metric) between consecutive cycles of the same topic.

Usage:
  python tune_lss.py --sensitivity "LLM Agents"
  python tune_lss.py --tune metrics_history.jsonl
  python tune_lss.py --tune metrics_history.jsonl --metric precision
=============================================================================
"""
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prepare  # reused read-only: get_topic_dir(), count_actual_citations()


def raw_components(topic_name):
    """Recompute C and N exactly like prepare.compute_living_survey_score(),
    returned unweighted so they can be re-weighted freely here."""
    topic_dir = prepare.get_topic_dir(topic_name)
    clean_name = os.path.basename(topic_dir)
    survey_path = os.path.join(topic_dir, f"{clean_name}.md")
    bib_file = os.path.join(topic_dir, "references.bib")

    if not os.path.exists(survey_path):
        raise FileNotFoundError(f"No survey found for '{topic_name}' at {survey_path}")

    integrated_count = prepare.count_actual_citations(survey_path)

    bib_count = 0
    if os.path.exists(bib_file):
        with open(bib_file, "r", encoding="utf-8") as f:
            bib_count = f.read().count("@article")

    with open(survey_path, "r", encoding="utf-8") as f:
        line_count = len(f.readlines())

    C = (integrated_count * 3.0) + (bib_count * 1.5)
    N = 50.0 + (line_count * 0.2)

    return {
        "C": C, "N": N,
        "integrated_count": integrated_count, "bib_count": bib_count,
        "line_count": line_count,
    }


def sensitivity(topic_name, step=0.02):
    comp = raw_components(topic_name)

    print(f"\nRaw components for '{topic_name}':")
    print(f"  C = {comp['C']:.2f}  (integrated={comp['integrated_count']}, bib={comp['bib_count']})")
    print(f"  N = {comp['N']:.2f}  (lines={comp['line_count']})\n")

    print(f"{'wC':>5} {'wN':>5} {'score':>8}")
    print("-" * 22)
    n = round(1 / step)
    for i in range(n + 1):
        wc = round(i * step, 2)
        wn = round(1 - wc, 2)
        score = wc * comp["C"] + wn * comp["N"]
        print(f"{wc:5.2f} {wn:5.2f} {score:8.2f}")

    current = 0.5 * comp["C"] + 0.5 * comp["N"]
    print(f"\nCurrent formula (wC=0.50, wN=0.50) gives: {current:.2f}")


def tune(history_path, step=0.02, metric="f1"):
    if not os.path.exists(history_path):
        print(f"[ERROR] '{history_path}' not found. Run some cycles with loop.py first.")
        return

    cycles = []
    with open(history_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                cycles.append(json.loads(line))

    if len(cycles) < 2:
        print(f"[INFO] Only {len(cycles)} cycle(s) logged. Need at least 2 per topic.")
        return

    # Only compare consecutive cycles of the SAME topic - cycles from
    # different topics/surveys are never comparable to each other.
    by_topic = {}
    for c in cycles:
        by_topic.setdefault(c.get("topic", "<unknown>"), []).append(c)

    pairs = []
    for topic, topic_cycles in by_topic.items():
        for prev, curr in zip(topic_cycles, topic_cycles[1:]):
            if metric in prev and metric in curr:
                pairs.append((prev, curr))

    if not pairs:
        print(f"[INFO] No consecutive same-topic cycle pairs with '{metric}' recorded.")
        return

    print(f"[INFO] Tuning against metric: '{metric}'")
    print(f"[INFO] Using {len(pairs)} consecutive same-topic cycle pairs across "
          f"{len(by_topic)} topic(s): {', '.join(sorted(by_topic.keys()))}\n")

    results = []
    n = round(1 / step)
    for i in range(n + 1):
        wc = round(i * step, 4)
        wn = round(1 - wc, 4)
        agree, total = 0, 0
        for prev, curr in pairs:
            score_prev = wc * prev["C"] + wn * prev["N"]
            score_curr = wc * curr["C"] + wn * curr["N"]
            predicted_improve = score_curr > score_prev
            actual_improve = curr[metric] > prev[metric]
            agree += int(predicted_improve == actual_improve)
            total += 1
        if total > 0:
            results.append((wc, wn, agree / total, total))

    if not results:
        print(f"[INFO] No consecutive cycle pairs with '{metric}' recorded.")
        return

    print(f"{'wC':>5} {'wN':>5} {'agree%':>8}")
    print("-" * 22)
    for wc, wn, acc, total in results:
        print(f"{wc:5.2f} {wn:5.2f} {acc*100:7.1f}%")

    best_acc = max(r[2] for r in results)
    plateau = [r for r in results if r[2] == best_acc]
    wc_lo = min(r[0] for r in plateau)
    wc_hi = max(r[0] for r in plateau)

    print(f"\nBest agreement: {best_acc*100:.1f}% (n={results[0][3]} cycle-pairs)")
    if wc_hi - wc_lo > 2 * step:
        midpoint = round((wc_lo + wc_hi) / 2, 2)
        print(f"[NOTE] This is a PLATEAU, not a single point: every wC from {wc_lo:.2f} "
              f"to {wc_hi:.2f} ties at {best_acc*100:.1f}%. With this sample size the data "
              f"cannot distinguish between these ratios; a defensible choice is the "
              f"plateau's midpoint (wC={midpoint:.2f}).")
    else:
        best_wc = plateau[0][0]
        print(f"[NOTE] Fairly sharp optimum around wC={best_wc:.2f}, wN={1-best_wc:.2f}.")

    print("\nWith few logged cycles this is a weak estimate - treat it as a direction,")
    print("not a final answer, until more cycles are logged across several topics.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    if sys.argv[1] == "--sensitivity" and len(sys.argv) > 2:
        sensitivity(sys.argv[2])
    elif sys.argv[1] == "--tune":
        args = sys.argv[2:]
        metric = "f1"
        if "--metric" in args:
            idx = args.index("--metric")
            metric = args[idx + 1]
            del args[idx:idx + 2]
        history_file = args[0] if args else "metrics_history.jsonl"
        tune(history_file, metric=metric)
    else:
        print(__doc__)