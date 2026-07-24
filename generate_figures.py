import os
import matplotlib.pyplot as plt
import json

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

def plot_publication_timeline():
    """Genera la timeline dei paper inclusi nella survey."""
    # Qwen/Aider aggiornerà questo dizionario o lo leggerà da un file JSON/BibTeX
    data = {
        "2021": 2,
        "2022": 5,
        "2023": 12,
        "2024": 24,
        "2025": 18,
        "2026": 8  # Inseriti finora
    }
    
    years = list(data.keys())
    counts = list(data.values())
    
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.bar(years, counts, color='#2b5c8f', width=0.6)
    ax.set_title("Evoluzione delle Pubblicazioni nel Dominio")
    ax.set_xlabel("Anno")
    ax.set_ylabel("Numero di Paper Citati")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig("figures/timeline.png", dpi=300)
    plt.close()

def plot_taxonomy_distribution():
    """Genera la distribuzione dei metodi secondo la tassonomia della survey."""
    # Dati baseline che l'agente modificherà man mano che classifica nuovi paper
    categories = {
        "External Memory": 14,
        "Working Memory": 9,
        "Episodic Storage": 18,
        "Parametric Refinement": 6
    }
    
    labels = list(categories.keys())
    values = list(categories.values())
    
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, 
           colors=['#2b5c8f', '#d95f02', '#7570b3', '#e7298a'])
    ax.set_title("Distribuzione dei Paper per Tassonomia")
    
    plt.tight_layout()
    plt.savefig("figures/taxonomy.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    plot_publication_timeline()
    plot_taxonomy_distribution()
    print("[GENERATE_FIGURES] Grafici aggiornati con successo in figures/")