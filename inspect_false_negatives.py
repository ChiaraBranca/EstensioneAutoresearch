"""
=============================================================================
FILE: inspect_false_negatives.py
DESCRIPTION:
For a given cycle, lists the abstracts of "false negative" papers - ones the
Oracle scored above the threshold (so it thinks they are relevant) but the
Actor did NOT integrate - so you can quickly read them and judge whether the
Actor was actually right to exclude them (Oracle fooled by lexical/embedding
ambiguity, e.g. "RAG" vs "EAG") or whether it was a genuine retrieval miss.

This does not decide anything automatically - it is a reading aid for manual
qualitative inspection, meant to build concrete case-study evidence (like the
RAG/EAG example) for the thesis discussion of the Oracle's limitations.

Usage:
  python inspect_false_negatives.py <cosine_scores.json> <references.bib> <new_papers.json> [threshold]

The new_papers.json should be the ARCHIVED one for that same cycle, i.e.
surveys/<topic>/eval_logs/new_papers_<timestamp>.json (same timestamp as the
cosine_scores_<timestamp>.json you are inspecting) - it is the only place that
still has the title/abstract text once the cycle is over.
=============================================================================
"""
import sys
import os
import json
import re


def clean_id(raw_id):
    return re.sub(r'v\d+$', '', str(raw_id).strip())


def get_integrated_papers(bib_file):
    if not os.path.exists(bib_file):
        return set()
    with open(bib_file, "r", encoding="utf-8") as f:
        content = f.read()
    ids = set(re.findall(r'@\w+\{([^,]+),', content))
    return {clean_id(i) for i in ids}


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)

    scores_file = sys.argv[1]
    bib_file = sys.argv[2]
    papers_file = sys.argv[3]
    threshold = float(sys.argv[4]) if len(sys.argv) > 4 else 0.50

    with open(scores_file, "r", encoding="utf-8") as f:
        scores = json.load(f)
    with open(papers_file, "r", encoding="utf-8") as f:
        papers = json.load(f)

    integrated = get_integrated_papers(bib_file)
    papers_by_id = {p["id"]: p for p in papers}

    false_negatives = []
    for paper_id, score in scores.items():
        base_id = clean_id(paper_id)
        is_relevant_gt = score >= threshold
        is_relevant_ai = base_id in integrated
        if is_relevant_gt and not is_relevant_ai:
            false_negatives.append((paper_id, score))

    false_negatives.sort(key=lambda x: -x[1])  # highest score (most "confident" Oracle mistake) first

    print(f"\n{len(false_negatives)} false negative(s) at threshold {threshold:.2f} "
          f"(Oracle said relevant, Actor excluded):\n")

    for paper_id, score in false_negatives:
        paper = papers_by_id.get(paper_id)
        print("=" * 70)
        print(f"ID: {paper_id}   |   Cosine sim: {score:.4f}")
        if paper:
            print(f"Title: {paper.get('title', '(no title)')}")
            abstract = paper.get('abstract', '(no abstract)')
            print(f"Abstract: {abstract[:400]}{'...' if len(abstract) > 400 else ''}")
        else:
            print("(paper not found in new_papers.json - wrong file/timestamp?)")
        print()

    print("=" * 70)
    print("\nFor each one above, ask: is this genuinely about the topic, or does it\n"
          "just share vocabulary/acronyms with it (lexical ambiguity)? Cases of the\n"
          "second kind are Oracle labeling errors, not real Actor mistakes - good\n"
          "material for a 'limitations of the Oracle' case study in the thesis.")
          