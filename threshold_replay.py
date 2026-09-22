"""
=============================================================================
FILE: threshold_replay.py
DESCRIPTION:
Offline "what-if" tool for the Oracle's RELEVANCE_THRESHOLD.

Since auto_evaluator.py now saves cosine_scores.json (raw, non-binarized cosine
similarities) alongside ground_truth.json, and loop.py archives it per cycle in
surveys/<topic>/eval_logs/cosine_scores_<timestamp>.json, we can recompute what
Precision/Recall/F1/Accuracy WOULD HAVE BEEN at a different threshold, for a
cycle that already happened, without spending any new embedding API calls and
without re-running the Actor/Critic loop.

This answers questions like "would 0.56 have worked better than 0.58 for this
cycle?" directly from already-collected data, instead of guessing or having to
re-run the (expensive) full pipeline to test each candidate threshold.

Usage:
  python threshold_replay.py <cosine_scores.json> <references.bib> [thresholds...]

Example:
  python threshold_replay.py surveys/brain/eval_logs/cosine_scores_20260922_021203.json \
                              surveys/brain/references.bib \
                              0.50 0.52 0.54 0.56 0.58 0.60
  (if no thresholds are given, a default sweep from 0.50 to 0.66 is used)
=============================================================================
"""
import sys
import os
import json
import re


def clean_id(raw_id):
    """Same normalization rule used in evaluate_metrics.py: strip only a trailing
    version suffix like 'v2', never touch a 'v' that appears mid-string."""
    return re.sub(r'v\d+$', '', str(raw_id).strip())


def get_integrated_papers(bib_file):
    """Extract the set of paper IDs actually integrated by the Actor at this cycle,
    exactly like evaluate_metrics.py does."""
    if not os.path.exists(bib_file):
        return set()
    with open(bib_file, "r", encoding="utf-8") as f:
        content = f.read()
    ids = set(re.findall(r'@\w+\{([^,]+),', content))
    return {clean_id(i) for i in ids}


def confusion_at_threshold(scores, integrated, threshold):
    """Recompute the confusion matrix and derived metrics as if RELEVANCE_THRESHOLD
    had been `threshold` for this cycle, reusing the already-computed cosine scores."""
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
    return TP, FP, FN, TN, precision, recall, f1, accuracy


def list_borderline_included(scores, integrated, low, high):
    """Papers the Actor DID include, whose cosine score falls in a borderline band
    (e.g. between 0.50 and 0.58) - i.e. the papers whose classification as
    'relevant' vs 'not relevant' actually flips depending on where you set the
    threshold. This is the direct answer to 'which papers are threshold-sensitive?'"""
    borderline = []
    for paper_id, score in scores.items():
        base_id = clean_id(paper_id)
        if base_id in integrated and low <= score < high:
            borderline.append((paper_id, score))
    return sorted(borderline, key=lambda x: x[1])


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    scores_file = sys.argv[1]
    bib_file = sys.argv[2]
    thresholds = [float(x) for x in sys.argv[3:]] if len(sys.argv) > 3 else \
        [round(0.50 + 0.02 * i, 2) for i in range(9)]  # 0.50 .. 0.66

    if not os.path.exists(scores_file):
        print(f"[ERROR] '{scores_file}' not found. Look for it under "
              f"surveys/<topic>/eval_logs/cosine_scores_<timestamp>.json")
        sys.exit(1)

    with open(scores_file, "r", encoding="utf-8") as f:
        scores = json.load(f)
    integrated = get_integrated_papers(bib_file)

    print(f"\n{len(scores)} papers scored by the Oracle in this cycle, "
          f"{len(integrated)} integrated by the Actor into references.bib.\n")

    print(f"{'thr':>5} {'TP':>4} {'FP':>4} {'FN':>4} {'TN':>4} "
          f"{'prec':>6} {'rec':>6} {'f1':>6} {'acc':>6}")
    print("-" * 58)
    for t in thresholds:
        TP, FP, FN, TN, p, r, f1, acc = confusion_at_threshold(scores, integrated, t)
        print(f"{t:5.2f} {TP:4d} {FP:4d} {FN:4d} {TN:4d} "
              f"{p:6.3f} {r:6.3f} {f1:6.3f} {acc:6.3f}")

    print(f"\nPapers the Actor included whose cosine score is between 0.50 and 0.58")
    print("(these are exactly the ones whose classification flips as you move the threshold):")
    borderline = list_borderline_included(scores, integrated, 0.50, 0.58)
    if borderline:
        for paper_id, score in borderline:
            print(f"  {score:.4f}  {paper_id}")
    else:
        print("  (none - the Actor's picks are not sensitive to this threshold range)")