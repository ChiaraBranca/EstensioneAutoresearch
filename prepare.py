import os
import sys
import json
import re
import time
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
    ids = set(re.findall(r'@\w+\{([^,]+),', content))
    return ids

def fetch_arxiv_papers(query, existing_ids=None, target_count=50):
    """SERVER 1: ArXiv (Focalizzato su STEM, AI, Fisica). Paginato per Data."""
    if existing_ids is None: existing_ids = set()
    clean_query = urllib.parse.quote(query.strip())
    print(f"[SERVER 1 - ARXIV] Ricerca in corso per: '{query}'...")
    
    new_papers = []
    start = 0
    limit = 50
    
    while len(new_papers) < target_count:
        # Usa sortBy=submittedDate per prendere sempre le novità assolute
        url = f"http://export.arxiv.org/api/query?search_query=all:{clean_query}&start={start}&max_results={limit}&sortBy=submittedDate&sortOrder=descending"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            data = urllib.request.urlopen(req).read()
            root = ET.fromstring(data)
            ns = {'arxiv': 'http://www.w3.org/2005/Atom'}
            entries = root.findall('arxiv:entry', ns)
            
            if not entries: 
                break # Fine dei risultati
                
            for entry in entries:
                if len(new_papers) >= target_count: break
                
                paper_id = entry.find('arxiv:id', ns).text.split('/')[-1].split('v')[0]
                if paper_id in existing_ids: continue
                
                title = entry.find('arxiv:title', ns).text.strip().replace('\n', ' ')
                summary = entry.find('arxiv:summary', ns).text.strip().replace('\n', ' ')
                pub_year = entry.find('arxiv:published', ns).text[:4]
                
                new_papers.append({'id': paper_id, 'title': title, 'abstract': summary, 'year': pub_year})
                
            start += limit
            time.sleep(1) # Pausa di cortesia
        except Exception as e:
            print(f"[ERRORE ARXIV] {e}")
            break
    return new_papers

def fetch_openalex_papers(query, existing_ids=None, target_count=50):
    """SERVER 2: OpenAlex (Focalizzato su Medicina, Scienze Umane, Multidisciplinare)."""
    if existing_ids is None: existing_ids = set()
    clean_query = urllib.parse.quote(query.strip())
    print(f"[SERVER 2 - OPENALEX] Ricerca in corso per: '{query}'...")
    
    new_papers = []
    page = 1
    
    while len(new_papers) < target_count:
        # Il parametro 'mailto' ci inserisce nella "Polite Pool" gratuita da 100.000 req/day
        url = f"https://api.openalex.org/works?search={clean_query}&per-page=50&page={page}&sort=publication_date:desc&mailto=tesi.multiagente@example.com"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
            
            results = data.get('results', [])
            if not results: break
                
            for paper in results:
                if len(new_papers) >= target_count: break
                
                # OpenAlex restituisce l'abstract come "Inverted Index" (una mappa parola-posizioni). Lo ricostruiamo:
                inv_index = paper.get('abstract_inverted_index')
                if not inv_index: continue
                
                word_pos = []
                for word, positions in inv_index.items():
                    for pos in positions:
                        word_pos.append((pos, word))
                word_pos.sort(key=lambda x: x[0])
                abstract = " ".join([w[1] for w in word_pos])
                
                # Creiamo un ID univoco
                paper_id = paper.get('doi') or paper.get('id')
                if not paper_id: continue
                paper_id = paper_id.replace('https://doi.org/', '').replace('/', '_')
                
                if paper_id in existing_ids: continue
                
                new_papers.append({
                    'id': paper_id,
                    'title': paper.get('title', '').strip().replace('\n', ' '),
                    'abstract': abstract.replace('\n', ' '),
                    'year': str(paper.get('publication_year', '2026'))
                })
            page += 1
            time.sleep(0.5)
        except Exception as e:
            print(f"[ERRORE OPENALEX] {e}")
            break
    return new_papers

def count_actual_citations(survey_path):
    if not os.path.exists(survey_path):
        return 0
    with open(survey_path, 'r', encoding='utf-8') as f:
        content = f.read()
    citations = set(re.findall(r'\[\^([^\]]+)\]', content))
    return len(citations)

def compute_living_survey_score(topic_name):
    topic_dir = get_topic_dir(topic_name)
    clean_name = os.path.basename(topic_dir)
    survey_path = os.path.join(topic_dir, f"{clean_name}.md")
    bib_file = os.path.join(topic_dir, "references.bib")
    
    fig_timeline = os.path.join(topic_dir, "figures", "timeline.png")
    fig_taxonomy = os.path.join(topic_dir, "figures", "taxonomy.png")
    
    if not os.path.exists(survey_path):
        return 0.0, 0
        
    integrated_count = count_actual_citations(survey_path)
    
    bib_count = 0
    if os.path.exists(bib_file):
        with open(bib_file, 'r', encoding='utf-8') as f:
            bib_count = f.read().count("@article")

    figure_generated = os.path.exists(fig_timeline) and os.path.exists(fig_taxonomy)
    
    I = 100.0
    C = min(100.0, (integrated_count * 3.0) + (bib_count * 1.5)) 
    V = 100.0 if figure_generated else 0.0
    
    line_count = 0
    with open(survey_path, 'r', encoding='utf-8') as f:
        line_count = len(f.readlines())
    N = min(100.0, 50.0 + (line_count * 0.2)) 
    
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
        
        print("\n--- AVVIO RICERCA FEDERATA MULTI-SERVER ---")
        
        # 1. Chiediamo 50 paper al Server 1 (ArXiv)
        arxiv_papers = fetch_arxiv_papers(search_query, existing_ids, target_count=50)
        
        # Aggiorniamo la memoria per non pescare doppioni sul secondo server!
        for p in arxiv_papers:
            existing_ids.add(p['id'])
            
        # 2. Chiediamo 50 paper al Server 2 (OpenAlex)
        openalex_papers = fetch_openalex_papers(search_query, existing_ids, target_count=50)
        
        # 3. Uniamo il tutto in un unico mega-dataset da 100 paper
        all_papers = arxiv_papers + openalex_papers
        
        with open("new_papers.json", "w", encoding="utf-8") as f:
            json.dump(all_papers, f, indent=2)
            
        print(f"[PREPARE] Recuperati {len(all_papers)} nuovi paper INEDITI ")
        print(f"          Dettaglio: {len(arxiv_papers)} da ArXiv, {len(openalex_papers)} da OpenAlex.")
        
    elif action == "--eval":
        score, count = compute_living_survey_score(topic)
        print(f"INTEGRATED_COUNT:{count}")
        print(f"LSS_SCORE:{score}")