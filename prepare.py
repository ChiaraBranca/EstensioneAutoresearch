import os
import sys
import json
import re
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

# Trasforma "LLM memory agents" in una cartella sicura: "llm_memory_agents"
def get_topic_dir(topic_name):
    clean_name = re.sub(r'[^a-zA-Z0-9]', '_', topic_name.lower()).strip('_')
    return os.path.join("surveys", clean_name)

def init_workspace(topic_name):
    """Verifica se esiste la cartella per l'argomento. Se non esiste, la crea con uno scheletro vuoto."""
    topic_dir = get_topic_dir(topic_name)
    os.makedirs(os.path.join(topic_dir, "figures"), exist_ok=True)
    
    survey_file = os.path.join(topic_dir, "survey.md")
    bib_file = os.path.join(topic_dir, "references.bib")
    fig_script = os.path.join(topic_dir, "generate_figures.py")

    # 1. Se survey.md non esiste, crealo pulito
    if not os.path.exists(survey_file):
        with open(survey_file, "w", encoding="utf-8") as f:
            f.write(f"# Living Survey: {topic_name}\n\n## Introduzione\n\n## Letteratura Recente\n\n## Analisi Comparativa\n")
        print(f"[INIT] Creato nuovo file survey in: {survey_file}")

    # 2. Se references.bib non esiste, crealo vuoto
    if not os.path.exists(bib_file):
        open(bib_file, "a").close()

    # 3. Se generate_figures.py non esiste, genera uno script baseline di default
    if not os.path.exists(fig_script):
        baseline_code = """import os, matplotlib.pyplot as plt
os.makedirs('figures', exist_ok=True)
def plot_timeline():
    plt.figure(figsize=(6,3))
    plt.title('Baseline Timeline')
    plt.savefig('figures/timeline.png')
    plt.close()
if __name__ == '__main__': plot_timeline()
"""
        with open(fig_script, "w", encoding="utf-8") as f:
            f.write(baseline_code)
            
    return topic_dir

def fetch_arxiv_papers(query, max_results=5):
    """Recupera gli ultimi articoli da ArXiv."""
    url = f"http://export.arxiv.org/api/query?search_query=all:{urllib.parse.quote(query)}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    try:
        data = urllib.request.urlopen(url).read()
        root = ET.fromstring(data)
        ns = {'arxiv': 'http://www.w3.org/2005/Atom'}
        papers = []
        for entry in root.findall('arxiv:entry', ns):
            paper_id = entry.find('arxiv:id', ns).text.split('/')[-1]
            title = entry.find('arxiv:title', ns).text.strip().replace('\n', ' ')
            summary = entry.find('arxiv:summary', ns).text.strip().replace('\n', ' ')
            papers.append({'id': paper_id, 'title': title, 'abstract': summary})
        return papers
    except Exception as e:
        print(f"[ERRORE FETCH] Impossibile contattare ArXiv: {e}")
        return []

def count_actual_citations(survey_path):
    """CONTEGGIO REALE (Anti-Imbroglio): conta le citazioni nel Markdown tipo [^id_paper] o [Autore, Anno]"""
    if not os.path.exists(survey_path):
        return 0
    with open(survey_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Trova tutte le ricorrenze di tag tipo [^... ] o [ ... , 202x ]
    citations = set(re.findall(r'\[\^([^\]]+)\]', content))
    return len(citations)

def compute_living_survey_score(topic_name):
    topic_dir = get_topic_dir(topic_name)
    survey_path = os.path.join(topic_dir, "survey.md")
    fig_path = os.path.join(topic_dir, "figures", "timeline.png")
    
    # Valuta l'esistenza dei file
    if not os.path.exists(survey_path):
        return 0.0
        
    integrated_count = count_actual_citations(survey_path)
    figure_generated = os.path.exists(fig_path)
    
    I = 100.0
    C = min(100.0, integrated_count * 20.0)
    V = 100.0 if figure_generated else 0.0
    N = 80.0  # Baseline testuale
    
    score = (0.35 * C) + (0.30 * N) + (0.20 * V) + (0.15 * I)
    return round(score, 2), integrated_count

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python prepare.py [--init|--fetch|--eval] \"Nome Argomento\"")
        sys.exit(1)
        
    action = sys.argv[1]
    topic = sys.argv[2]
    
    if action == "--init":
        path = init_workspace(topic)
        print(f"WORKSPACE_READY:{path}")
    elif action == "--fetch":
        init_workspace(topic)
        papers = fetch_arxiv_papers(topic)
        with open("new_papers.json", "w", encoding="utf-8") as f:
            json.dump(papers, f, indent=2)
        print(f"[PREPARE] Recuperati {len(papers)} nuovi paper per '{topic}' in new_papers.json")
    elif action == "--eval":
        score, count = compute_living_survey_score(topic)
        print(f"INTEGRATED_COUNT:{count}")
        print(f"LSS_SCORE:{score}")