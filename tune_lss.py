"""
=============================================================================
FILE: tune_lss.py
DESCRIPTION:
Standalone diagnostic / tuning tool for the Living Survey Score (LSS) formula
defined in prepare.py. It does NOT modify prepare.py, loop.py,
evaluate_metrics.py or program.md.

  score = (wC * C) + (wN * N) + (wV * V) + (wI * I)

Two modes:

  --sensitivity "<Topic>"
      Recomputes the CURRENT raw components (C, N, V, I) for a topic and
      shows how the total score moves across a grid of weight combinations.
      No ground truth needed. Purely diagnostic: it will NOT tell you which
      weights are "best", only how sensitive the score is to each one -
      and it will show you that I is a constant (100.0) in the current
      formula, so no weight assigned to it ever changes a commit/reject
      decision.

  --tune [metrics_history.jsonl]
      Reads a JSONL file (one JSON object per cycle) with fields:
        topic, C, N, V, I, f1
      and grid-searches weight combinations that maximize how often
      "predicted LSS improved" agrees with "real F1 improved" between
      CONSECUTIVE CYCLES OF THE SAME TOPIC (cycles from different topics
      are never compared to each other - see the grouping logic in tune()).
      This is the actual empirical tuning, and requires loop.py to have
      logged several cycles per topic first (see metrics_history.jsonl).

Usage:
  python tune_lss.py --sensitivity "LLM Agents"
  python tune_lss.py --tune metrics_history.jsonl
=============================================================================
"""
import sys
import os
import json
import itertools

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prepare  # reused read-only: get_topic_dir(), count_actual_citations()


def raw_components(topic_name):
    """
    Recompute the four RAW components exactly like
    prepare.compute_living_survey_score() does internally, but return them
    separately (unweighted) so they can be re-weighted freely here.
    """
    topic_dir = prepare.get_topic_dir(topic_name)
    clean_name = os.path.basename(topic_dir)
    survey_path = os.path.join(topic_dir, f"{clean_name}.md")
    bib_file = os.path.join(topic_dir, "references.bib")
    fig_timeline = os.path.join(topic_dir, "figures", "timeline.png")
    fig_taxonomy = os.path.join(topic_dir, "figures", "taxonomy.png")

    if not os.path.exists(survey_path):
        raise FileNotFoundError(f"No survey found for '{topic_name}' at {survey_path}")

    integrated_count = prepare.count_actual_citations(survey_path)

    bib_count = 0
    if os.path.exists(bib_file):
        with open(bib_file, "r", encoding="utf-8") as f:
            bib_count = f.read().count("@article")

    figure_generated = os.path.exists(fig_timeline) and os.path.exists(fig_taxonomy)

    with open(survey_path, "r", encoding="utf-8") as f:
        line_count = len(f.readlines())

    C = min(100.0, (integrated_count * 3.0) + (bib_count * 1.5))
    V = 100.0 if figure_generated else 0.0
    N = min(100.0, 50.0 + (line_count * 0.2))
    I = 100.0  # constant in the current formula - see docstring / printout below

    return {
        "C": C, "N": N, "V": V, "I": I,
        "integrated_count": integrated_count, "bib_count": bib_count,
        "line_count": line_count, "figures_ok": figure_generated,
    }


def weight_grid(step=0.05):
    """All (wC, wN, wV, wI) that are multiples of `step`, each >= 0, summing to 1."""
    n = round(1 / step)
    for ic, iN, iv in itertools.product(range(n + 1), repeat=3):
        if ic + iN + iv > n:
            continue
        ii = n - ic - iN - iv
        yield (ic * step, iN * step, iv * step, ii * step)


def sensitivity(topic_name, step=0.05):
    comp = raw_components(topic_name)

    print(f"\nRaw components for '{topic_name}':")
    print(f"  C (coverage)  = {comp['C']:.2f}  (integrated={comp['integrated_count']}, bib={comp['bib_count']})")
    print(f"  N (length)    = {comp['N']:.2f}  (lines={comp['line_count']})")
    print(f"  V (visuals)   = {comp['V']:.2f}  (figures_ok={comp['figures_ok']})")
    print(f"  I (integrity) = {comp['I']:.2f}  <-- ALWAYS 100.0 in prepare.py.")
    print("                    This term is a CONSTANT: whatever weight you give it,")
    print("                    it can never change which of two cycles scores higher.")
    print("                    Only C, N, V actually drive every commit/reject decision.\n")

    rows = []
    for wc, wn, wv, wi in weight_grid(step):
        score = wc * comp["C"] + wn * comp["N"] + wv * comp["V"] + wi * comp["I"]
        rows.append((wc, wn, wv, wi, score))
    rows.sort(key=lambda r: r[-1])

    print(f"{'wC':>5} {'wN':>5} {'wV':>5} {'wI':>5} | score   (lowest 5 / highest 5 over the grid)")
    print("-" * 55)
    for wc, wn, wv, wi, score in rows[:5]:
        print(f"{wc:5.2f} {wn:5.2f} {wv:5.2f} {wi:5.2f} | {score:6.2f}")
    print("  ...")
    for wc, wn, wv, wi, score in rows[-5:]:
        print(f"{wc:5.2f} {wn:5.2f} {wv:5.2f} {wi:5.2f} | {score:6.2f}")

    current = 0.35 * comp["C"] + 0.30 * comp["N"] + 0.20 * comp["V"] + 0.15 * comp["I"]
    print(f"\nCurrent formula (wC=0.35, wN=0.30, wV=0.20, wI=0.15) gives: {current:.2f}")


def tune(history_path, step=0.05):
    if not os.path.exists(history_path):
        print(f"[ERROR] '{history_path}' not found.\n")
        print("This file doesn't exist yet because loop.py / evaluate_metrics.py don't")
        print("currently persist per-cycle metrics to disk (they only print to stdout).")
        print("Add lightweight logging first (see the snippet provided alongside this")
        print("script), run a handful of cycles, then re-run --tune.")
        return

    cycles = []
    with open(history_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                cycles.append(json.loads(line))

    if len(cycles) < 2:
        print(f"[INFO] Only {len(cycles)} cycle(s) logged so far. Need at least 2 "
              f"consecutive cycles with 'f1' recorded to evaluate any weighting "
              f"scheme. Run a few more cycles first.")
        return

    # IMPORTANT: only compare CONSECUTIVE cycles of the SAME topic. metrics_history.jsonl
    # accumulates cycles from every topic you have ever run loop.py on, in the order they
    # happened; comparing e.g. cycle 3 of "brain" against cycle 1 of "cancer" would be
    # meaningless (different survey, different baseline, unrelated LSS/F1 values). Grouping
    # by "topic" first, and preserving the original (chronological) order within each group,
    # gives only genuine same-survey, cycle-to-cycle comparisons.
    by_topic = {}
    for c in cycles:
        by_topic.setdefault(c.get("topic", "<unknown>"), []).append(c)

    pairs = []
    for topic, topic_cycles in by_topic.items():
        for prev, curr in zip(topic_cycles, topic_cycles[1:]):
            if "f1" in prev and "f1" in curr:
                pairs.append((prev, curr))

    if not pairs:
        print("[INFO] No consecutive same-topic cycle pairs with 'f1' recorded. "
              "Nothing to tune yet (you may only have one cycle per topic so far).")
        return

    print(f"[INFO] Using {len(pairs)} consecutive same-topic cycle pairs across "
          f"{len(by_topic)} topic(s): {', '.join(sorted(by_topic.keys()))}\n")

    results = []
    for wc, wn, wv, wi in weight_grid(step):
        agree, total = 0, 0
        for prev, curr in pairs:
            score_prev = wc * prev["C"] + wn * prev["N"] + wv * prev["V"] + wi * prev["I"]
            score_curr = wc * curr["C"] + wn * curr["N"] + wv * curr["V"] + wi * curr["I"]
            predicted_improve = score_curr > score_prev
            actual_improve = curr["f1"] > prev["f1"]
            agree += int(predicted_improve == actual_improve)
            total += 1
        if total > 0:
            results.append((agree / total, wc, wn, wv, wi, total))

    if not results:
        print("[INFO] No consecutive cycle pairs with 'f1' recorded. Nothing to tune yet.")
        return

    results.sort(reverse=True)
    print(f"{'agree%':>7} {'n':>4} {'wC':>5} {'wN':>5} {'wV':>5} {'wI':>5}")
    print("-" * 40)
    for acc, wc, wn, wv, wi, total in results[:10]:
        print(f"{acc*100:6.1f}% {total:4d} {wc:5.2f} {wn:5.2f} {wv:5.2f} {wi:5.2f}")

    best = results[0]
    print(f"\nBest agreement with real F1 improvement: {best[0]*100:.1f}% using "
          f"wC={best[1]:.2f}, wN={best[2]:.2f}, wV={best[3]:.2f}, wI={best[4]:.2f} "
          f"(n={best[5]} cycle-pairs)")

    # I is a constant (100.0) in every cycle, so it can never change which of two cycles
    # scores higher - any weight assigned to it is interchangeable. If several top results
    # share the same agreement but differ only in wI, that is direct empirical confirmation
    # of this (not a coincidence of the grid), and a reasonable, well-justified simplification
    # is to drop I from the formula entirely and renormalize wC + wN + wV = 1.
    top_score = results[0][0]
    tied = [r for r in results if r[0] == top_score]
    wi_values = sorted(set(round(r[4], 2) for r in tied))
    if len(wi_values) > 1:
        print(f"\n[NOTE] {len(tied)} weight combinations tie for the best agreement "
              f"({top_score*100:.1f}%), differing only in wI ({wi_values}). This confirms "
              f"wI is inert: consider dropping I from the formula and renormalizing "
              f"wC + wN + wV = 1 instead of picking an arbitrary wI.")

    print("\nNote: with few logged cycles this is a weak estimate - treat it as a")
    print("direction, not a final answer, until you have dozens of cycles logged across")
    print("several topics.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    if sys.argv[1] == "--sensitivity" and len(sys.argv) > 2:
        sensitivity(sys.argv[2])
    elif sys.argv[1] == "--tune":
        history_file = sys.argv[2] if len(sys.argv) > 2 else "metrics_history.jsonl"
        tune(history_file)
    else:
        print(__doc__)