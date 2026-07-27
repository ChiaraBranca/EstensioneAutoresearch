import os
import sys
import json
import re
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

def get_topic_dir(topic_name):
    """Converte 'agenti llm e memoria' nella cartella sicura 'surveys/agenti_llm_e_memoria'"""
    clean_name = re.sub(r'[^a-zA-Z0-9]', '_', topic_name.lower()).strip('_')
    return os.path.join("surveys", clean_name)

def init_workspace(topic_name):
    topic_dir = get_topic_dir(topic_name)
    os.makedirs(os.path.join(topic_dir, "figures"), exist_ok=True)
    
    clean_name = os.path.basename(topic_dir)
    survey_file = os.path.join(topic_dir, f"{clean_name}.md")
    bib_file = os.path.join(topic_dir, "references.bib")
    fig_script = os.path.join(topic_dir, "generate_figures.py")

    if not os.path.exists(survey_file):
        with open(survey_file, "w", encoding="utf-8") as f:
            f.write(f"# Living Survey: {topic_name}\n\n## Introduzione\n\nQuesto documento raccoglie la letteratura scientifica sul tema **{topic_name}**.\n")
        print(f"[INIT] Creato nuovo file survey in: {survey_file}")

    if not os.path.exists(bib_file):
        open(bib_file, "a").close()

    # SCRIPT GRAFICI CON PERCORSI ASSOLUTI (Salvataggio protetto nella cartella del topic)
    if not os.path.exists(fig_script):
        baseline_code = '''import os
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

plt.style.use('seaborn-v0_8-paper' if 'seaborn-v0_8-paper' in plt.style.available else 'default')
plt.rcParams.update({'font.size': 10, 'axes.labelsize': 11, 'axes.titlesize': 12, 'figure.titlesize': 14})

SURVEY_TITLE = "''' + topic_name + '''"
TIMELINE_DATA = {"2024": 0, "2025": 0, "2026": 0}
TAXONOMY_DATA = {"Baseline Categorization": 1}

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
    plt.savefig(os.path.join(FIG_DIR, "timeline.png"), dpi=300)
    plt.close()

def plot_taxonomy_distribution():
    labels, values = list(TAXONOMY_DATA.keys()), list(TAXONOMY_DATA.values())
    if sum(values) == 0: labels, values = ["Nessun dato"], [1]
    colors = ['#2b5c8f', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#ff7f0e', '#4e79a7', '#f28e2b', '#76b7b2', '#59a14f']
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors[:len(labels)])
    ax.set_title(f"Tassonomia: {SURVEY_TITLE}")
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "taxonomy.png"), dpi=300)
    plt.close()

if __name__ == "__main__":
    plot_publication_timeline()
    plot_taxonomy_distribution()
    print(f"[GENERATE_FIGURES] Grafici aggiornati in {FIG_DIR}")
'''
        with open(fig_script, "w", encoding="utf-8") as f:
            f.write(baseline_code)
            
    return topic_dir
     
def get_existing_ids(topic_dir):
    """MEMORIA STORICA: Legge references.bib e restituisce gli ID dei paper già integrati."""
    bib_file = os.path.join(topic_dir, "references.bib")
    if not os.path.exists(bib_file):
        return set()
    with open(bib_file, "r", encoding="utf-8") as f:
        content = f.read()
    # Trova tutte le chiavi BibTeX tipo @article{2605.28732v3, ...
    ids = set(re.findall(r'@\w+\{([^,]+),', content))
    # Per sicurezza, prendiamo anche la versione senza la 'v' (es. 2605.28732)
    stripped_ids = {i.split('v')[0] for i in ids}
    return ids.union(stripped_ids)

def fetch_arxiv_papers(query, existing_ids=None, max_results=30):
    if existing_ids is None:
        existing_ids = set()
        
    # 1. Estrazione automatica di eventuali anni specificati nella query (es. 2024)
    target_years = [int(y) for y in re.findall(r'\b(19\d\d|20\d\d)\b', query)]
    
    # 2. Pulizia della query rimuovendo l'anno per non disturbare la ricerca testuale di ArXiv
    clean_query = re.sub(r'\b(19\d\d|20\d\d)\b', '', query).strip()
    if not clean_query:
        clean_query = query
        
    print(f"[ARXIV] Query testuale: '{clean_query}' | Filtro anni attivo: {target_years if target_years else 'Nessuno'}")

    words = clean_query.split()
    arxiv_query = "+AND+".join([f"all:{urllib.parse.quote(w)}" for w in words]) if words else "all:research"
    
    fetch_limit = max(45, max_results * 3)
    url = f"http://export.arxiv.org/api/query?search_query={arxiv_query}&start=0&max_results={fetch_limit}&sortBy=relevance&sortOrder=descending"
    
    try:
        data = urllib.request.urlopen(url).read()
        root = ET.fromstring(data)
        ns = {'arxiv': 'http://www.w3.org/2005/Atom'}
        new_papers = []
        
        for entry in root.findall('arxiv:entry', ns):
            paper_id = entry.find('arxiv:id', ns).text.split('/')[-1]
            base_id = paper_id.split('v')[0]
            
            if paper_id in existing_ids or base_id in existing_ids:
                continue
                
            published_str = entry.find('arxiv:published', ns).text
            pub_year = int(published_str[:4])
            
            # FILTRO TEMPORALE OCCASIONALE: se l'utente ha messo un anno, lo applichiamo
            if target_years and pub_year not in target_years:
                continue
                
            title = entry.find('arxiv:title', ns).text.strip().replace('\n', ' ')
            summary = entry.find('arxiv:summary', ns).text.strip().replace('\n', ' ')
            new_papers.append({'id': paper_id, 'title': title, 'abstract': summary})
            
            if len(new_papers) >= max_results:
                break
                
        return new_papers
    except Exception as e:
        print(f"[ERRORE FETCH] Impossibile contattare ArXiv: {e}", file=sys.stderr)
        return []

def count_actual_citations(survey_path):
    """CONTEGGIO REALE ANTI-ALLUCINAZIONE: conta le tag Markdown [^...] uniche nel file."""
    if not os.path.exists(survey_path):
        return 0
    with open(survey_path, 'r', encoding='utf-8') as f:
        content = f.read()
    citations = set(re.findall(r'\[\^([^\]]+)\]', content))
    return len(citations)

def compute_living_survey_score(topic_name):
    """Calcola la vera Matrice di Verifica (LSS) basandosi sui file fisici presenti."""
    topic_dir = get_topic_dir(topic_name)
    clean_name = os.path.basename(topic_dir)
    
    # CERCA IL FILE <nome_argomento>.md INVECE DI survey.md
    survey_path = os.path.join(topic_dir, f"{clean_name}.md")
    
    fig_timeline = os.path.join(topic_dir, "figures", "timeline.png")
    fig_taxonomy = os.path.join(topic_dir, "figures", "taxonomy.png")
    
    if not os.path.exists(survey_path):
        return 0.0, 0
        
    integrated_count = count_actual_citations(survey_path)
    figure_generated = os.path.exists(fig_timeline) and os.path.exists(fig_taxonomy)
    
    I = 100.0
    C = min(100.0, integrated_count * 20.0) # 20 punti per ogni vera citazione trovata nel testo
    V = 100.0 if figure_generated else 0.0
    N = 80.0  # Baseline per la sintesi testuale
    
    score = (0.35 * C) + (0.30 * N) + (0.20 * V) + (0.15 * I)
    return round(score, 2), integrated_count

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python prepare.py [--init|--eval] \"Nome Argomento\" oppure python prepare.py --fetch \"Nome Argomento\" \"Query di Ricerca\"")
        sys.exit(1)
        
    action = sys.argv[1]
    topic = sys.argv[2]
    
    if action == "--init":
        path = init_workspace(topic)
        print(f"WORKSPACE_READY:{path}")
    elif action == "--fetch":
        search_query = sys.argv[3] if len(sys.argv) > 3 else topic
        topic_dir = init_workspace(topic)
        existing_ids = get_existing_ids(topic_dir)
        papers = fetch_arxiv_papers(search_query, existing_ids=existing_ids, max_results=30)
        with open("new_papers.json", "w", encoding="utf-8") as f:
            json.dump(papers, f, indent=2)
        print(f"[PREPARE] Recuperati {len(papers)} nuovi paper per '{search_query}' in new_papers.json (ignorati {len(existing_ids)} già presenti)")
    elif action == "--eval":
        score, count = compute_living_survey_score(topic)
        print(f"INTEGRATED_COUNT:{count}")
        print(f"LSS_SCORE:{score}")