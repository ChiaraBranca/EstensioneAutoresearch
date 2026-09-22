import os
import re
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

plt.style.use('seaborn-v0_8-paper' if 'seaborn-v0_8-paper' in plt.style.available else 'default')
plt.rcParams.update({'font.size': 10, 'axes.labelsize': 11, 'axes.titlesize': 12, 'figure.titlesize': 14})

SURVEY_TITLE = "cancer"
# [AI AGENT ZONE] Edit only these dictionaries
TIMELINE_DATA = {"2024": 0, "2025": 0, "2026": 34}
TAXONOMY_DATA = {"AI Diagnostics & Imaging": 8, "Computational Oncology & Modeling": 4, "Genomics & Biomarkers": 10, "Tumor Microenvironment & Mechanisms": 5, "Clinical Therapeutics & Immunotherapy": 6, "Epidemiology & Public Health": 1}

def plot_publication_timeline():
    years, counts = list(TIMELINE_DATA.keys()), list(TIMELINE_DATA.values())
    fig, ax = plt.subplots(figsize=(10, 3.5))
    ax.bar(years, counts, color='#2b5c8f', width=0.6)
    ax.set_title(f"Publication Timeline: {SURVEY_TITLE}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Cited Papers")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    if max(counts if counts else [0]) == 0: ax.set_ylim(0, 5)
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "timeline.png"), dpi=300)
    plt.close()

def plot_taxonomy_distribution():
    labels, values = list(TAXONOMY_DATA.keys()), list(TAXONOMY_DATA.values())
    if sum(values) == 0: labels, values = ["No data"], [1]
    colors = ['#2b5c8f', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#ff7f0e', '#4e79a7', '#f28e2b', '#76b7b2', '#59a14f']
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors[:len(labels)])
    ax.set_title(f"Taxonomy Distribution: {SURVEY_TITLE}")
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "taxonomy.png"), dpi=300)
    plt.close()

if __name__ == "__main__":
    # --- START OF RE-CHECK BLOCK (SANITIZER) ---
    bib_path = os.path.join(BASE_DIR, "references.bib")
    if os.path.exists(bib_path):
        with open(bib_path, "r", encoding="utf-8") as f:
            bib_content = f.read()
        
        # Extract all years from the actually surviving papers in the .bib file
        actual_years = re.findall(r'year\s*=\s*[{"]?(\d{4})[}"]?', bib_content)
        
        if actual_years:
            # Overwrite the Actor's estimates with the absolute truth from the .bib file
            TIMELINE_DATA = {year: actual_years.count(year) for year in sorted(set(actual_years))}
        else:
            # Fallback if the .bib is empty
            TIMELINE_DATA = {"2024": 0, "2025": 0, "2026": 0}

        # --- TAXONOMY SANITY CHECK (not a fix, only a warning) ---
        # Unlike TIMELINE_DATA, TAXONOMY_DATA is never reconstructed from the .bib file
        # (there is no ground-truth "methodological category" field to recompute it from).
        # This only performs a weak consistency check: the total number of papers the
        # Actor claims to have categorized should match the number of entries actually
        # present in the bibliography. A mismatch does not necessarily mean the taxonomy
        # is wrong, but it is a signal worth investigating manually.
        entry_count = len(re.findall(r'@\w+\{', bib_content))
        taxonomy_total = sum(TAXONOMY_DATA.values()) if TAXONOMY_DATA else 0
        if entry_count and taxonomy_total != entry_count:
            print(
                f"[TAXONOMY WARNING] TAXONOMY_DATA sums to {taxonomy_total}, but "
                f"references.bib has {entry_count} entries. The taxonomy breakdown "
                f"may be stale or miscounted (it is not cross-checked automatically "
                f"like TIMELINE_DATA)."
            )
        # --- END OF TAXONOMY SANITY CHECK ---
    # --- END OF RE-CHECK BLOCK ---

    plot_publication_timeline()
    plot_taxonomy_distribution()
    print(f"[GENERATE_FIGURES] Charts updated in {FIG_DIR} (Timeline reconciled with .bib)")
