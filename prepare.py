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
    """
    Initializes the workspace for a given topic. 
    Creates the markdown file, the bibtex file, and injects the python script for figures.
    """
    topic_dir = get_topic_dir(topic_name)
    os.makedirs(os.path.join(topic_dir, "figures"), exist_ok=True)
    
    clean_name = os.path.basename(topic_dir)
    survey_file = os.path.join(topic_dir, f"{clean_name}.md")
    bib_file = os.path.join(topic_dir, "references.bib")
    fig_script = os.path.join(topic_dir, "generate_figures.py")

    # Initialize empty Markdown Survey
    if not os.path.exists(survey_file):
        with open(survey_file, "w", encoding="utf-8") as f:
            f.write(f"# Living Survey: {topic_name}\n\n## Introduction\n\nThis document collects the scientific literature regarding **{topic_name}**.\n")
        print(f"[INIT] Created new survey file in: {survey_file}")

    # Initialize empty Bibliography
    if not os.path.exists(bib_file):
        open(bib_file, "a").close()

    # Inject the Python script for Matplotlib figure generation (translated to English)
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
    """
    HISTORICAL MEMORY: Reads references.bib and returns a set of IDs already integrated.
    This acts as a Bloom filter to prevent processing duplicate papers across loops.
    """
    bib_file = os.path.join(topic_dir, "references.bib")
    if not os.path.exists(bib_file):
        return set()
    with open(bib_file, "r", encoding="utf-8") as f:
        content = f.read()
    ids = set(re.findall(r'@\w+\{([^,]+),', content))
    return ids

def fetch_arxiv_papers(query, existing_ids=None, target_count=50):
    """
    SERVER 1: ArXiv. Focused on STEM, AI, and Physics.
    Includes Regex filtering to extract the target year directly from the query string.
    """
    if existing_ids is None: existing_ids = set()
    
    # REGEX: Extract target years and clean the search text
    target_years = [int(y) for y in re.findall(r'\b(19\d\d|20\d\d)\b', query)]
    clean_query_text = re.sub(r'\b(19\d\d|20\d\d)\b', '', query).strip()
    if not clean_query_text: clean_query_text = query
        
    clean_query = urllib.parse.quote(clean_query_text)
    print(f"[SERVER 1 - ARXIV] Searching for: '{clean_query_text}'...")
    
    new_papers = []
    start, limit = 0, 50
    
    while len(new_papers) < target_count:
        url = f"http://export.arxiv.org/api/query?search_query=all:{clean_query}&start={start}&max_results={limit}&sortBy=submittedDate&sortOrder=descending"
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
                
                # Apply local year filter
                if target_years and pub_year not in target_years: continue
                
                title = entry.find('arxiv:title', ns).text.strip().replace('\n', ' ')
                summary = entry.find('arxiv:summary', ns).text.strip().replace('\n', ' ')
                
                new_papers.append({'id': paper_id, 'title': title, 'abstract': summary, 'year': pub_year_str})
                
            start += limit
            time.sleep(1) # Courtesy delay
        except Exception as e:
            print(f"[ARXIV ERROR] {e}")
            break
    return new_papers

def fetch_openalex_papers(query, existing_ids=None, target_count=50):
    """
    SERVER 2: OpenAlex. Focused on Medicine, Humanities, and multidisciplinary research.
    Parses the abstract from an Inverted Index structure.
    """
    if existing_ids is None: existing_ids = set()
    
    # REGEX: Extract target years and clean the search text
    target_years = [int(y) for y in re.findall(r'\b(19\d\d|20\d\d)\b', query)]
    clean_query_text = re.sub(r'\b(19\d\d|20\d\d)\b', '', query).strip()
    if not clean_query_text: clean_query_text = query
        
    clean_query = urllib.parse.quote(clean_query_text)
    
    # Dynamic year filtering for OpenAlex API
    year_filter = ""
    if target_years:
        if len(target_years) == 1:
            year_filter = f"&filter=publication_year:{target_years[0]}"
        else:
            min_y, max_y = min(target_years), max(target_years)
            year_filter = f"&filter=publication_year:>{min_y-1},publication_year:<{max_y+1}"

    print(f"[SERVER 2 - OPENALEX] Searching for: '{clean_query_text}'...")
    
    new_papers = []
    page = 1
    
    while len(new_papers) < target_count:
        # Using 'mailto' parameter grants access to the fast 'polite pool'
        url = f"https://api.openalex.org/works?search={clean_query}{year_filter}&per-page=50&page={page}&sort=publication_date:desc&mailto=tesi.multiagente@example.com"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
            
            results = data.get('results', [])
            if not results: break
                
            for paper in results:
                if len(new_papers) >= target_count: break
                
                # Reconstruct abstract from Inverted Index
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
                
                new_papers.append({
                    'id': paper_id,
                    'title': paper.get('title', '').strip().replace('\n', ' '),
                    'abstract': abstract.replace('\n', ' '),
                    'year': str(paper.get('publication_year', '2026'))
                })
            page += 1
            time.sleep(0.5)
        except Exception as e:
            print(f"[OPENALEX ERROR] {e}")
            break
    return new_papers

def count_actual_citations(survey_path):
    """Counts the number of Markdown citations like [^paper_id] in the text."""
    if not os.path.exists(survey_path): return 0
    with open(survey_path, 'r', encoding='utf-8') as f:
        content = f.read()
    citations = set(re.findall(r'\[\^([^\]]+)\]', content))
    return len(citations)

def compute_living_survey_score(topic_name):
    """
    Computes the Living Survey Score (LSS).
    The LSS is a custom heuristic metric determining the overall maturity of the survey:
    - 35% C (Citations): Quantity of citations integrated in MD and BibTeX.
    - 30% N (Narrative): Length and depth of the Markdown text.
    - 20% V (Visuals): Boolean check if charts have been generated.
    - 15% I (Init): Base score for properly initialized workspace.
    """
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
    
    # Calculate weighted components
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
        
        # 1. Fetch from ArXiv
        arxiv_papers = fetch_arxiv_papers(search_query, existing_ids, target_count=50)
        
        # Cross-server deduplication
        for p in arxiv_papers: existing_ids.add(p['id'])
            
        # 2. Fetch from OpenAlex
        openalex_papers = fetch_openalex_papers(search_query, existing_ids, target_count=50)
        
        # 3. Combine datasets
        all_papers = arxiv_papers + openalex_papers
        
        with open("new_papers.json", "w", encoding="utf-8") as f:
            json.dump(all_papers, f, indent=2)
            
        print(f"[PREPARE] Fetched {len(all_papers)} completely NEW papers.")
        print(f"          Details: {len(arxiv_papers)} from ArXiv, {len(openalex_papers)} from OpenAlex.")
        
    elif action == "--eval":
        score, count = compute_living_survey_score(topic)
        print(f"INTEGRATED_COUNT:{count}")
        print(f"LSS_SCORE:{score}")