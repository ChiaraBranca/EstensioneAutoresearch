import os
import sys
import json
import urllib.request
import urllib.parse

def classify_with_llm(topic, abstract):
    """Usa il LLM locale come Oracolo binario."""
    # Prende le stesse variabili d'ambiente di loop.py
    api_base = os.environ.get("OPENAI_API_BASE", "http://127.0.0.1:9000/v1")
    api_key = os.environ.get("OPENAI_API_KEY", "none")
    
    prompt = (
        f"Sei un classificatore binario accademico. Valuta se questo abstract è pertinente "
        f"all'argomento '{topic}'.\n\nAbstract: {abstract}\n\n"
        f"Rispondi ESCLUSIVAMENTE con il numero '1' (se pertinente) o '0' (se non pertinente). Non aggiungere nessun altro carattere o parola."
    )
    
    data = {
        "model": "openai/lab-main", 
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0, # Deve essere 0.0 per essere deterministico e oggettivo
        "max_tokens": 5
    }
    
    req = urllib.request.Request(
        f"{api_base}/chat/completions",
        data=json.dumps(data).encode('utf-8'),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            reply = result['choices'][0]['message']['content'].strip()
            return 1 if '1' in reply else 0
    except Exception as e:
        print(f"[ERRORE ORACLE] Fallita classificazione: {e}")
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
        
    topic = sys.argv[1]
    
    if not os.path.exists("new_papers.json"):
        sys.exit(0)
        
    with open("new_papers.json", "r", encoding="utf-8") as f:
        papers = json.load(f)
        
    truth_dict = {}
    print(f"\n[ORACLE] Autogenerazione Ground Truth per {len(papers)} paper...")
    
    for p in papers:
        is_relevant = classify_with_llm(topic, p['abstract'])
        truth_dict[p['id']] = is_relevant
        
    with open("ground_truth.json", "w", encoding="utf-8") as f:
        json.dump(truth_dict, f, indent=2)
        
    print("[ORACLE] ground_truth.json generato in automatico!")