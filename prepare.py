import argparse
import urllib.request
import xml.etree.ElementTree as ET
import re
import sys
import os

def fetch_latest_arxiv():
    """Scarica l'ultimo paper su LLM e Memory da ArXiv e lo salva in current_paper.txt"""
    url = 'http://export.arxiv.org/api/query?search_query=all:LLM+AND+all:memory&sortBy=submittedDate&sortOrder=descending&max_results=1'
    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
        root = ET.fromstring(data)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        entry = root.find('atom:entry', ns)
        
        if entry is not None:
            title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
            summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
            paper_id = entry.find('atom:id', ns).text.strip()
            
            with open('current_paper.txt', 'w') as f:
                f.write(f"TITOLO: {title}\nABSTRACT: {summary}\nID: {paper_id}\n")
            print(">>> Successo: Scaricato nuovo paper in current_paper.txt")
        else:
            print(">>> Nessun paper trovato su ArXiv.")
    except Exception as e:
        print(f">>> Errore durante il fetch: {e}")

def verify_survey():
    """Verifica l'integrità e la sintassi di survey.md (il nostro calcolatore di Loss)"""
    if not os.path.exists('survey.md'):
        print("ERRORE: survey.md non esiste!")
        sys.exit(1)
        
    try:
        with open('survey.md', 'r') as f:
            content = f.read()
        
        # 1. Verifica che la tabella Markdown sia presente e non corrotta
        if not re.search(r'\|.*\|.*\|', content):
            print("ERRORE: La tabella comparativa è corrotta o mancante.")
            sys.exit(1)
            
        # 2. Controllo di coerenza: nessun segnaposto o marcatore incompleto
        if "TODO" in content or "FIXME" in content:
            print("ERRORE: Trovati marcatori TODO/FIXME non completati.")
            sys.exit(1)
        
        print("VERIFICA SUPERATA. (Loss = 0)")
        sys.exit(0)

    except Exception as e:
        print(f"ERRORE di compilazione: {e}")
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fetch', action='store_true', help='Scarica nuovi paper')
    parser.add_argument('--verify', action='store_true', help='Verifica integrità survey.md')
    args = parser.parse_args()

    if args.fetch:
        fetch_latest_arxiv()
    if args.verify:c
        verify_survey()