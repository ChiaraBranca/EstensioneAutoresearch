import argparse
import urllib.request
import xml.etree.ElementTree as ET
import re
import sys
import os

def fetch_latest_arxiv():
    """Scarica gli ultimi paper su Dinosaur Appearance da ArXiv e li salva in current_paper.txt"""
    # Query per paper recenti su aspetto dei dinosauri
    url = 'http://export.arxiv.org/api/query?search_query=all:dinosaur+AND+all:appearance&sortBy=submittedDate&sortOrder=descending&max_results=1'
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
            print(">>> Successo: Scaricato nuovo paper su Dinosaur Appearance in current_paper.txt")
        else:
            print(">>> Nessun paper trovato su ArXiv per 'dinosaur appearance'.")
    except Exception as e:
        print(f">>> Errore durante il fetch: {e}")

def verify_survey():
    """Verifica l'integrità e la struttura di survey.md per il report sui dinosauri"""
    if not os.path.exists('survey.md'):
        print("ERRORE: survey.md non esiste!")
        sys.exit(1)
        
    try:
        with open('survey.md', 'r') as f:
            content = f.read()
        
        # 1. Verifica che la tabella Markdown sia presente e non corrotta
        # Cerca una riga con almeno 3 pipe
        if not re.search(r'\|.*\|.*\|', content):
            print("ERRORE: La tabella comparativa è corrotta o mancante.")
            sys.exit(1)
            
        # 2. Controllo di coerenza: nessun segnaposto o marcatore incompleto
        if "TODO" in content or "FIXME" in content:
            print("ERRORE: Trovati marcatori TODO/FIXME non completati.")
            sys.exit(1)

        # 3. Verifica presenza di sezioni chiave per un report scientifico
        if "Bibliography" not in content and "Bibliografia" not in content:
            print("ERRORE: Sezione Bibliografia mancante.")
            sys.exit(1)
            
        if "Introduction" not in content:
            print("ERRORE: Sezione Introduzione mancante.")
            sys.exit(1)

        print("VERIFICA SUPERATA. (Loss = 0)")
        sys.exit(0)

    except Exception as e:
        print(f"ERRORE di compilazione: {e}")
        sys.exit(1)

def generate_metrics_report():
    """Genera un resoconto sulle metriche di paragone e la loro scelta"""
    report = """
## Resoconto sulle Metriche di Paragone

### Metriche Selezionate
1. **Presenza di Tabella Comparativa**: 
   - **Perché**: Le tabelle sono essenziali per confrontare rapidamente le caratteristiche di diversi gruppi di dinosauri (es. teropodi, sauropodi). Permettono una visualizzazione strutturata dei dati.
   - **Scelta**: La tabella Markdown è standard, facile da parsare e leggibile sia per umani che per script.

2. **Sezione Bibliografia**:
   - **Perché**: Un report scientifico deve essere basato su fonti verificabili. La bibliografia garantisce la tracciabilità delle informazioni.
   - **Scelta**: La presenza di una sezione dedicata assicura che il documento non sia solo un'opinione ma un lavoro di ricerca.

3. **Assenza di TODO/FIXME**:
   - **Perché**: Indica che il documento è completo e non contiene parti incomplete o da revisionare.
   - **Scelta**: Questo è un controllo di qualità base per garantire l'integrità del documento finale.

4. **Sezione Introduzione**:
   - **Perché**: Fornisce il contesto necessario per comprendere il report.
   - **Scelta**: L'introduzione è fondamentale per qualsiasi documento strutturato.

### Perché queste metriche?
Queste metriche sono state scelte per bilanciare la completezza del contenuto con la facilità di verifica automatica. 
- **Semplicità**: Sono facili da verificare con regex e controlli di stringa.
- **Rilevanza**: Coprono gli aspetti fondamentali di un report scientifico (contesto, dati, fonti, completezza).
- **Robustezza**: Non dipendono da formattazioni complesse, riducendo il rischio di falsi negativi.
"""
    print(report)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fetch', action='store_true', help='Scarica nuovi paper')
    parser.add_argument('--verify', action='store_true', help='Verifica integrità survey.md')
    parser.add_argument('--report', action='store_true', help='Genera resoconto metriche')
    args = parser.parse_args()

    if args.fetch:
        fetch_latest_arxiv()
    if args.verify:
        verify_survey()
    if args.report:
        generate_metrics_report()
