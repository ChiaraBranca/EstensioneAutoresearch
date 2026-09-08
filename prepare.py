"""
=============================================================================
FILE: prepare.py
DESCRIPTION: 
This script acts as the "Hunter" and "Memory Manager" of the framework.
It handles three main tasks:
1. Workspace Initialization (--init): Creates isolated silos (folders) for topics.
2. Federated Information Retrieval (--fetch): Queries ArXiv and OpenAlex, bypassing 
   rate limits and using Regex for dynamic year filtering, while deduplicating 
   against the historical memory (references.bib).
3. Metric Evaluation (--eval): Computes the Living Survey Score (LSS).
=============================================================================
"""

import os
import sys
import json
import re
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

def get_topic_dir(topic_name):
    """Converts a string like 'LLM Agents' into a safe directory name 'surveys/llm_agents'."""
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
            f.write(f"# Living Survey: {topic_name}\n\n## Introduction\n\nThis document collects the scientific literature regarding **{topic_name}**.\n")
        print(f"[INIT] Created new survey file in: {survey_file}")

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
# [AI AGENT ZONE] Edit only these dictionaries
TIMELINE_DATA = {"2024": 0, "2025": 0, "2026": 0}
TAXONOMY_DATA = {"Baseline Categorization": 1}

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
    plot_publication_timeline()
    plot_taxonomy_distribution()
    print(f"[GENERATE_FIGURES] Charts updated in {FIG_DIR}")
'''
        with open(fig_script, "w", encoding="utf-8") as f:
            f.write(baseline_code)
            
    return topic_dir
     
def get_existing_ids(topic_dir):
    bib_file = os.path.join(topic_dir, "references.bib")
    if not os.path.exists(bib_file):
        return set()
    with open(bib_file, "r", encoding="utf-8") as f:
        content = f.read()
    ids = set(re.findall(r'@\w+\{([^,]+),', content))
    return ids

def fetch_arxiv_papers(query, existing_ids=None, target_count=30):
    if existing_ids is None: existing_ids = set()
    
    target_years = [int(y) for y in re.findall(r'\b(19\d\d|20\d\d)\b', query)]
    clean_query_text = re.sub(r'\b(19\d\d|20\d\d)\b', '', query).strip()
    if not clean_query_text: clean_query_text = query
        
    clean_query = urllib.parse.quote(clean_query_text)
    
    arxiv_year_query = ""
    if target_years:
        if len(target_years) == 1:
            arxiv_year_query = f"+AND+submittedDate:[{target_years[0]}01010000+TO+{target_years[0]}12312359]"
        else:
            min_y, max_y = min(target_years), max(target_years)
            arxiv_year_query = f"+AND+submittedDate:[{min_y}01010000+TO+{max_y}12312359]"

    print(f"[SERVER 1 - ARXIV] Searching for: '{clean_query_text}' (Filter: {target_years if target_years else 'Latest'})...")
    
    new_papers = []
    start, limit = 0, 30
    
    while len(new_papers) < target_count:
        url = f"http://export.arxiv.org/api/query?search_query=all:{clean_query}{arxiv_year_query}&start={start}&max_results={limit}&sortBy=submittedDate&sortOrder=descending"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            data = urllib.request.urlopen(req).read()
            root = ET.fromstring(data)
            ns = {'arxiv': 'http://www.w3.org/2005/Atom'}
            entries = root.findall('arxiv:entry', ns)
            
            if not entries: break 
                
            for entry in entries:
                if len(new_papers) >= target_count: break
                
                paper_id = entry.find('arxiv:id', ns).text.split('/')[-1].split('v')[0]
                if paper_id in existing_ids: continue
                
                pub_year_str = entry.find('arxiv:published', ns).text[:4]
                pub_year = int(pub_year_str)
                
                # DOPPIA SICUREZZA: Filtro Locale Python per ArXiv
                if target_years:
                    if len(target_years) > 1:
                        min_y, max_y = min(target_years), max(target_years)
                        if not (min_y <= pub_year <= max_y): continue
                    else:
                        if pub_year not in target_years: continue
                
                title = entry.find('arxiv:title', ns).text.strip().replace('\n', ' ')
                summary = entry.find('arxiv:summary', ns).text.strip().replace('\n', ' ')
                
                new_papers.append({'id': paper_id, 'title': title, 'abstract': summary, 'year': pub_year_str})
                
            start += limit
            time.sleep(5) 
        except Exception as e:
            print(f"[ARXIV ERROR] {e}")
            break
    return new_papers

def fetch_openalex_papers(query, existing_ids=None, target_count=30):
    if existing_ids is None: existing_ids = set()
    
    target_years = [int(y) for y in re.findall(r'\b(19\d\d|20\d\d)\b', query)]
    clean_query_text = re.sub(r'\b(19\d\d|20\d\d)\b', '', query).strip()
    if not clean_query_text: clean_query_text = query
        
    clean_query = urllib.parse.quote(clean_query_text)
    
    year_filter = ""
    if target_years:
        if len(target_years) == 1:
            year_filter = f"&filter=publication_year:{target_years[0]}"
        else:
            min_y, max_y = min(target_years), max(target_years)
            year_filter = f"&filter=publication_year:{min_y}-{max_y}"

    print(f"[SERVER 2 - OPENALEX] Searching for: '{clean_query_text}'...")
    
    new_papers = []
    page = 1
    
    while len(new_papers) < target_count:
        url = f"https://api.openalex.org/works?search={clean_query}{year_filter}&per-page=30&page={page}&sort=publication_date:desc&mailto=tesi.multiagente@example.com"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
            
            results = data.get('results', [])
            if not results: break
                
            for paper in results:
                if len(new_papers) >= target_count: break
                
                pub_year_val = paper.get('publication_year')
                if not pub_year_val: continue
                pub_year = int(pub_year_val)
                
                # DOPPIA SICUREZZA: Filtro Locale Python per OpenAlex
                if target_years:
                    if len(target_years) > 1:
                        min_y, max_y = min(target_years), max(target_years)
                        if not (min_y <= pub_year <= max_y): continue
                    else:
                        if pub_year not in target_years: continue
                        
                inv_index = paper.get('abstract_inverted_index')
                if not inv_index: continue
                
                word_pos = []
                for word, positions in inv_index.items():
                    for pos in positions: word_pos.append((pos, word))
                word_pos.sort(key=lambda x: x[0])
                abstract = " ".join([w[1] for w in word_pos])
                
                paper_id = paper.get('doi') or paper.get('id')
                if not paper_id: continue
                paper_id = paper_id.replace('https://doi.org/', '').replace('/', '_')
                
                if paper_id in existing_ids: continue
                
                raw_title = paper.get('title')
                safe_title = raw_title.strip().replace('\n', ' ') if raw_title else "Untitled Paper"

                new_papers.append({
                    'id': paper_id,
                    'title': safe_title,
                    'abstract': abstract.replace('\n', ' '),
                    'year': str(pub_year)
                })
            page += 1
            time.sleep(0.5)
        except Exception as e:
            print(f"[OPENALEX ERROR] {e}")
            break
    return new_papers

def count_actual_citations(survey_path):
    if not os.path.exists(survey_path): return 0
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
        print("Usage: python prepare.py [--init|--eval] \"Topic Name\" or python prepare.py --fetch \"Topic Name\" \"Search Query\"")
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
        
        print("\n--- INITIATING FEDERATED MULTI-SERVER SEARCH ---")
        
        arxiv_papers = fetch_arxiv_papers(search_query, existing_ids, target_count=30)
        for p in arxiv_papers: existing_ids.add(p['id'])
            
        openalex_papers = fetch_openalex_papers(search_query, existing_ids, target_count=30)
        
        all_papers = arxiv_papers + openalex_papers
        
        with open("new_papers.json", "w", encoding="utf-8") as f:
            json.dump(all_papers, f, indent=2)
            
        print(f"[PREPARE] Fetched {len(all_papers)} completely NEW papers.")
        print(f"          Details: {len(arxiv_papers)} from ArXiv, {len(openalex_papers)} from OpenAlex.")
        
    elif action == "--eval":
        score, count = compute_living_survey_score(topic)
        print(f"INTEGRATED_COUNT:{count}")
        print(f"LSS_SCORE:{score}")