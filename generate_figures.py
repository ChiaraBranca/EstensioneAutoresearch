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
    # Dati aggiornati per la survey sui dinosauri (2000-2026), buchi neri (2000) e telefoni (1999-2005)
    data = {
        "1999": 2, # 1 WAP, 1 SMS
        "2000": 4, # 1 Dinosaur, 1 Black Hole, 1 Camera Phone, 1 Smartphone
        "2001": 2, # 1 Dinosaur, 1 Smartphone
        "2002": 0,
        "2003": 1, # 1 Dinosaur
        "2004": 1, # 1 Dinosaur
        "2005": 1, # 1 Dinosaur
        "2006": 0,
        "2007": 0,
        "2008": 1, # 1 Dinosaur
        "2009": 0,
        "2010": 1, # 1 Dinosaur
        "2011": 0,
        "2012": 1, # 1 Dinosaur
        "2013": 0,
        "2014": 0,
        "2015": 1, # 1 Dinosaur
        "2016": 0,
        "2017": 0,
        "2018": 1, # 1 Dinosaur
        "2019": 0,
        "2020": 1, # 1 Dinosaur
        "2021": 0,
        "2022": 1, # 1 Dinosaur
        "2023": 0,
        "2024": 1, # 1 Dinosaur
        "2025": 0,
        "2026": 1  # 1 Dinosaur
    }
    
    years = list(data.keys())
    counts = list(data.values())
    
    fig, ax = plt.subplots(figsize=(10, 3.5))
    ax.bar(years, counts, color='#2b5c8f', width=0.6)
    ax.set_title("Evoluzione delle Pubblicazioni nel Dominio Dinosauri, Buchi Neri e Telefoni (1999-2026)")
    ax.set_xlabel("Anno")
    ax.set_ylabel("Numero di Paper Citati")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig("figures/timeline.png", dpi=300)
    plt.close()

def plot_taxonomy_distribution():
    """Genera la distribuzione dei metodi secondo la tassonomia della survey."""
    # Dati aggiornati per la survey sui dinosauri, buchi neri e telefoni
    # Tassonomia simulata basata sui temi trattati
    categories = {
        "Phylogeny & Evolution": 4,
        "Physiology & Metabolism": 3,
        "Biomechanics & Behavior": 3,
        "Paleocolor & Soft Tissue": 2,
        "AI & Reconstruction": 1,
        "Accretion Dynamics": 1,
        "Mobile Communication": 2,
        "Smartphone & Internet": 2
    }
    
    labels = list(categories.keys())
    values = list(categories.values())
    
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, 
           colors=['#2b5c8f', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#ff7f0e', '#4e79a7', '#f28e2b'])
    ax.set_title("Distribuzione dei Paper per Tassonomia")
    
    plt.tight_layout()
    plt.savefig("figures/taxonomy.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    plot_publication_timeline()
    plot_taxonomy_distribution()
    print("[GENERATE_FIGURES] Grafici aggiornati con successo in figures/")
