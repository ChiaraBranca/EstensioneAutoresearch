import os
import sys
import json
import re
import urllib.request
import urllib.parse
import time 

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

def fetch_semantic_scholar_papers(query, existing_ids=None, target_count=100):
    """
    Estrae paper dal motore multidisciplinare Semantic Scholar.
    Permette di specificare un anno o un range di anni direttamente nella query.
    Es: 'brain 2015' -> Cerca 'brain' solo nel 2015.
    """
    if existing_ids is None:
        existing_ids = set()
        
    # 1. Estrazione automatica di eventuali anni dalla query (es. "2015" o "2018 2021")
    target_years = [int(y) for y in re.findall(r'\b(19\d\d|20\d\d)\b', query)]
    
    # 2. Pulizia della query (togliamo gli anni dal testo per non confondere la ricerca semantica)
    clean_query_text = re.sub(r'\b(19\d\d|20\d\d)\b', '', query).strip()
    if not clean_query_text:
        clean_query_text = query # Fallback
        
    clean_query = urllib.parse.quote(clean_query_text)
    
    # 3. Costruzione dinamica del parametro anno per Semantic Scholar
    year_param = ""
    if len(target_years) == 1:
        year_param = f"&year={target_years[0]}"
    elif len(target_years) >= 2:
        # Se metti due anni (es. "brain 2015 2020"), cerca in quel range
        year_param = f"&year={min(target_years)}-{max(target_years)}"
        
    print(f"[SEMANTIC SCHOLAR] Query: '{clean_query_text}' | Filtro Anno: {year_param.replace('&year=', '') if year_param else 'Nessuno (Tutta la storia)'}")
    
    new_papers = []
    offset = 0
    limit = 100 
    
    while len(new_papers) < target_count:
        # Costruiamo l'URL unendo la query pulita e il parametro anno (se presente)
        url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={clean_query}&offset={offset}&limit={limit}&fields=title,abstract,year,externalIds{year_param}"
        
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                
            batch = data.get('data', [])
            if not batch: 
                print("[SEMANTIC SCHOLAR] Nessun altro risultato trovato dal motore di ricerca.")
                break
                
            for paper in batch:
                if len(new_papers) >= target_count:
                    break
                    
                if not paper.get('abstract'):
                    continue
                    
                paper_id = paper['paperId']
                if 'externalIds' in paper and paper['externalIds']:
                    if 'DOI' in paper['externalIds']:
                        paper_id = paper['externalIds']['DOI'].replace('/', '_')
                    elif 'ArXiv' in paper['externalIds']:
                        paper_id = paper['externalIds']['ArXiv']
                
                if paper_id in existing_ids:
                    continue
                    
                new_papers.append({
                    'id': paper_id,
                    'title': paper.get('title', '').strip().replace('\n', ' '),
                    'abstract': paper.get('abstract', '').strip().replace('\n', ' '),
                    'year': str(paper.get('year', '2026'))
                })
                
            offset += limit
            time.sleep(1.5) # Pausa rate-limit
            
        except Exception as e:
            error_detail = str(e)
            if hasattr(e, 'read'):
                try:
                    error_detail = e.read().decode('utf-8')
                except:
                    pass
            print(f"[ERRORE FETCH S2] Fallita connessione (Offset {offset}). Dettaglio: {error_detail}")
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
        
        # ORA CERCHIAMO ESATTAMENTE 100 PAPER INEDITI!
        target_papers = 100
        
        papers = fetch_semantic_scholar_papers(search_query, existing_ids=existing_ids, target_count=target_papers)
        
        with open("new_papers.json", "w", encoding="utf-8") as f:
            json.dump(papers, f, indent=2)
            
        print(f"[PREPARE] Recuperati {len(papers)} nuovi paper INEDITI per '{search_query}' in new_papers.json. "
              f"Il motore ha automaticamente ignorato gli ID già presenti nella memoria storica ({len(existing_ids)} paper).")
              
    elif action == "--eval":
        score, count = compute_living_survey_score(topic)
        print(f"INTEGRATED_COUNT:{count}")
        print(f"LSS_SCORE:{score}")