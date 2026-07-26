import os
import matplotlib.pyplot as plt

# Assicurati che la directory di output esista
os.makedirs("figures", exist_ok=True)

# Impostazioni stile pulito per pubblicazioni scientifiche
plt.style.use('seaborn-v0_8-paper' if 'seaborn-v0_8-paper' in plt.style.available else 'default')
plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'figure.titlesize': 14
})

# ==============================================================================
# [ZONA AGENTE AI] MODIFICA ESCLUSIVAMENTE QUESTI DUE DIZIONARI E I TITOLI
# ==============================================================================
SURVEY_TITLE = "Analisi Letteratura Scientifica"

# Formato: "Anno": Numero_di_Paper
TIMELINE_DATA = {
    "2024": 0,
    "2025": 0,
    "2026": 0
}

# Formato: "Categoria / Metodo": Numero_di_Paper
TAXONOMY_DATA = {
    "Baseline Categorization": 1
}
# ==============================================================================
# [ZONA INTOCCABILE] NON MODIFICARE LA LOGICA DI PLOT SOTTOSTANTE
# ==============================================================================

def plot_publication_timeline():
    """Genera la timeline dei paper inclusi nella survey."""
    years = list(TIMELINE_DATA.keys())
    counts = list(TIMELINE_DATA.values())
    
    fig, ax = plt.subplots(figsize=(10, 3.5))
    ax.bar(years, counts, color='#2b5c8f', width=0.6)
    ax.set_title(f"Evoluzione Temporale delle Pubblicazioni: {SURVEY_TITLE}")
    ax.set_xlabel("Anno")
    ax.set_ylabel("Numero di Paper Citati")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Evita errori visivi se tutti i valori sono a zero
    if max(counts if counts else [0]) == 0:
        ax.set_ylim(0, 5)
        
    plt.tight_layout()
    plt.savefig("figures/timeline.png", dpi=300)
    plt.close()

def plot_taxonomy_distribution():
    """Genera la distribuzione dei metodi secondo la tassonomia della survey."""
    labels = list(TAXONOMY_DATA.keys())
    values = list(TAXONOMY_DATA.values())
    
    # Se tutti i valori sono 0, imposta una baseline fittizia per evitare crash di Matplotlib
    if sum(values) == 0:
        labels = ["Nessun dato classificato"]
        values = [1]
        
    # Palette colori estesa per supportare l'aggiunta di molte categorie senza crashare
    colors = [
        '#2b5c8f', '#d95f02', '#7570b3', '#e7298a', '#66a61e', 
        '#ff7f0e', '#4e79a7', '#f28e2b', '#76b7b2', '#59a14f', 
        '#edc948', '#b07aa1', '#ff9da7', '#9c755f', '#bab0ac'
    ]
    
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.pie(
        values, 
        labels=labels, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=colors[:len(labels)]
    )
    ax.set_title(f"Distribuzione per Tassonomia: {SURVEY_TITLE}")
    
    plt.tight_layout()
    plt.savefig("figures/taxonomy.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    plot_publication_timeline()
    plot_taxonomy_distribution()
    print("[GENERATE_FIGURES] Grafici aggiornati con successo in figures/")
