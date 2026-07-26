import os
import matplotlib.pyplot as plt

os.makedirs("figures", exist_ok=True)
plt.style.use('seaborn-v0_8-paper' if 'seaborn-v0_8-paper' in plt.style.available else 'default')
plt.rcParams.update({'font.size': 10, 'axes.labelsize': 11, 'axes.titlesize': 12, 'figure.titlesize': 14})

# ==============================================================================
# [ZONA AGENTE AI] MODIFICA ESCLUSIVAMENTE QUESTI DUE DIZIONARI E I TITOLI
# ==============================================================================
SURVEY_TITLE = "large language models memory"
TIMELINE_DATA = {"2024": 1, "2025": 0, "2026": 2}
TAXONOMY_DATA = {"Baseline Categorization": 0, "Memory Debugging & Attribution": 1, "Parametric Memory Analysis": 1, "KV Cache Optimization": 1}
# ==============================================================================
# [ZONA INTOCCABILE] NON MODIFICARE LA LOGICA DI PLOT SOTTOSTANTE
# ==============================================================================

def plot_publication_timeline():
    years, counts = list(TIMELINE_DATA.keys()), list(TIMELINE_DATA.values())
    fig, ax = plt.subplots(figsize=(10, 3.5))
    ax.bar(years, counts, color='#2b5c8f', width=0.6)
    ax.set_title(f"Evoluzione Temporale: {SURVEY_TITLE}")
    ax.set_xlabel("Anno")
    ax.set_ylabel("Numero di Paper Citati")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    if max(counts if counts else [0]) == 0: ax.set_ylim(0, 5)
    plt.tight_layout()
    plt.savefig("figures/timeline.png", dpi=300)
    plt.close()

def plot_taxonomy_distribution():
    labels, values = list(TAXONOMY_DATA.keys()), list(TAXONOMY_DATA.values())
    if sum(values) == 0: labels, values = ["Nessun dato"], [1]
    colors = ['#2b5c8f', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#ff7f0e', '#4e79a7', '#f28e2b', '#76b7b2', '#59a14f']
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors[:len(labels)])
    ax.set_title(f"Tassonomia: {SURVEY_TITLE}")
    plt.tight_layout()
    plt.savefig("figures/taxonomy.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    plot_publication_timeline()
    plot_taxonomy_distribution()
    print("[GENERATE_FIGURES] Grafici aggiornati in figures/")
