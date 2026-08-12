import os
import sys
import json
import re
import urllib.request
import urllib.parse

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
    Usa l'ordinamento decrescente per Data di Pubblicazione per la Living Survey.
    Continua a pescare finché non raccoglie 'target_count' paper INEDITI (non in existing_ids) o finisce le pagine.
    """
    if existing_ids is None:
        existing_ids = set()
        
    # Pulizia query per URL
    clean_query = urllib.parse.quote(query.strip())
    
    print(f"[SEMANTIC SCHOLAR] Ricerca in corso per: '{query}' | Ordinamento: Nuove Pubblicazioni")
    
    new_papers = []
    offset = 0
    # Limite massimo API S2 per chiamata è 100
    limit = 100 
    
    # Ciclo di paginazione: continuiamo a chiedere pagine finché non riempiamo il nostro cesto
    while len(new_papers) < target_count:
        url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={clean_query}&offset={offset}&limit={limit}&fields=title,abstract,year,externalIds&sort=publicationDate:desc"
        
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                
            batch = data.get('data', [])
            if not batch: # Non ci sono più risultati sul motore di ricerca
                print("[SEMANTIC SCHOLAR] Nessun altro risultato trovato dal motore di ricerca.")
                break
                
            for paper in batch:
                if len(new_papers) >= target_count:
                    break
                    
                # Scartiamo i paper senza abstract
                if not paper.get('abstract'):
                    continue
                    
                # Definiamo l'ID univoco: Preferiamo DOI o ArXiv se esistono, altrimenti ID interno di S2
                paper_id = paper['paperId']
                if 'externalIds' in paper:
                    if 'DOI' in paper['externalIds']:
                        paper_id = paper['externalIds']['DOI'].replace('/', '_') # Niente slash per non rompere il Markdown
                    elif 'ArXiv' in paper['externalIds']:
                        paper_id = paper['externalIds']['ArXiv']
                
                # Se è già in memoria storica, lo saltiamo
                if paper_id in existing_ids:
                    continue
                    
                new_papers.append({
                    'id': paper_id,
                    'title': paper['title'].strip().replace('\n', ' '),
                    'abstract': paper['abstract'].strip().replace('\n', ' '),
                    'year': paper.get('year', '2026') # Fallback year
                })
                
            offset += limit # Passiamo alla pagina successiva
            
        except Exception as e:
            print(f"[ERRORE FETCH S2] Impossibile contattare Semantic Scholar (Offset {offset}): {e}", file=sys.stderr)
            break # Usciamo dal loop in caso di errore (es. rate limit)
            
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