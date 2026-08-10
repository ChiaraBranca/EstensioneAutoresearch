import os
import sys
import json
import urllib.request
import urllib.parse

def classify_with_llm(topic, abstract):
    """Usa il LLM locale come Oracolo binario."""
    api_base = os.environ.get("OPENAI_API_BASE", "http://127.0.0.1:9000/v1")
    api_key = os.environ.get("OPENAI_API_KEY", "none")
    
    # Prompt migliorato: diamo respiro al modello
    prompt = (
        f"Sei un valutatore scientifico. Leggi il seguente abstract e valuta se è "
        f"pertinente (anche in senso lato) al tema: '{topic}'.\n\n"
        f"Abstract: {abstract}\n\n"
        f"Rispondi '1' se il paper tratta argomenti utili o correlati a questo tema.\n"
        f"Rispondi '0' se il paper è completamente fuori tema.\n"
        f"Devi stampare come risposta finale ESCLUSIVAMENTE il numero 1 o il numero 0."
    )
    
    data = {
        "model": "openai/lab-main", 
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0, 
        "max_tokens": 10 # Leggermente alzato nel caso il modello parli prima di dire il numero
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
            # Cerca esplicitamente il carattere '1' nella risposta, ignorando eventuali chiacchiere extra
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