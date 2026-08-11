import os
import sys
import json
import urllib.request
import urllib.parse

def get_valid_model_name(api_base, api_key):
    """Interroga il server locale per scoprire il nome esatto del modello in esecuzione."""
    try:
        req = urllib.request.Request(
            f"{api_base}/models",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            # Prende l'ID del primo modello disponibile nella lista
            return data['data'][0]['id']
    except Exception as e:
        print(f"[ORACLE WARNING] Impossibile recuperare il nome del modello, tento fallback. Dettaglio: {e}")
        return "lab-main" # Fallback nel caso in cui fallisca

def classify_with_llm(topic, abstract, valid_model_name):
    """Usa il LLM locale come Oracolo binario."""
    api_base = os.environ.get("OPENAI_API_BASE", "http://127.0.0.1:9000/v1")
    api_key = os.environ.get("OPENAI_API_KEY", "none")
    
    prompt = (
        f"Sei un valutatore scientifico. Leggi il seguente abstract e valuta se è "
        f"pertinente (anche in senso lato) al tema: '{topic}'.\n\n"
        f"Abstract: {abstract}\n\n"
        f"Rispondi '1' se il paper tratta argomenti utili o correlati a questo tema.\n"
        f"Rispondi '0' se il paper è completamente fuori tema.\n"
        f"Devi stampare come risposta finale ESCLUSIVAMENTE il numero 1 o il numero 0."
    )
    
    data = {
        "model": valid_model_name, # <-- Ora usa il nome certificato dal server stesso!
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.01 
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
        error_detail = str(e)
        if hasattr(e, 'read'):
            try:
                error_detail = e.read().decode('utf-8')
            except:
                pass
        print(f"[ERRORE ORACLE] Fallita classificazione. Dettaglio: {error_detail}")
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
        
    topic = sys.argv[1]
    
    if not os.path.exists("new_papers.json"):
        sys.exit(0)
        
    api_base = os.environ.get("OPENAI_API_BASE", "http://127.0.0.1:9000/v1")
    api_key = os.environ.get("OPENAI_API_KEY", "none")
    
    # 1. Trova il nome giusto del modello
    valid_model_name = get_valid_model_name(api_base, api_key)
    print(f"\n[ORACLE] Identificato modello API valido: '{valid_model_name}'")
        
    with open("new_papers.json", "r", encoding="utf-8") as f:
        papers = json.load(f)
        
    truth_dict = {}
    print(f"[ORACLE] Autogenerazione Ground Truth per {len(papers)} paper...")
    
    for p in papers:
        # 2. Passa il nome giusto alla funzione
        is_relevant = classify_with_llm(topic, p['abstract'], valid_model_name)
        truth_dict[p['id']] = is_relevant
        
    with open("ground_truth.json", "w", encoding="utf-8") as f:
        json.dump(truth_dict, f, indent=2)
        
    print("[ORACLE] ground_truth.json generato in automatico!")