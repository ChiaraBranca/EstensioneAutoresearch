"""
=============================================================================
FILE: auto_evaluator.py
DESCRIPTION: 
This script acts as the "Oracle" (LLM-as-a-Judge) in the framework.
It operates in a Zero-Shot manner, analyzing the raw abstracts downloaded
by prepare.py and assigning a binary relevance score (1 or 0) based on the topic.
This generates a "Ground Truth" (ground_truth.json) that is completely independent
from the Actor agent, allowing for objective mathematical evaluation later.
=============================================================================
"""

import os
import sys
import json
import urllib.request
import urllib.parse
import time
from dotenv import load_dotenv

load_dotenv()

def get_valid_model_name(api_base, api_key):
    """Queries the local server to dynamically discover the running model ID."""
    try:
        req = urllib.request.Request(
            f"{api_base}/models",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data['data'][0]['id']
    except Exception as e:
        print(f"[ORACLE WARNING] Unable to fetch model name, attempting fallback. Detail: {e}")
        return "lab-main"

def classify_with_llm(topic, abstract, valid_model_name):
    """Uses the local LLM as a binary Oracle judge."""
    api_base = os.environ.get("OPENAI_API_BASE", "http://127.0.0.1:9000/v1")
    api_key = os.environ.get("OPENAI_API_KEY", "none")
    
    prompt = (
        f"You are a scientific evaluator. Read the following abstract and assess if it is "
        f"relevant (even broadly) to the theme: '{topic}'.\n\n"
        f"Abstract: {abstract}\n\n"
        f"Reply '1' if the paper discusses topics useful or related to this theme.\n"
        f"Reply '0' if the paper is completely off-topic.\n"
        f"You must output EXCLUSIVELY the number 1 or the number 0 as your final response."
    )
    
    data = {
        "model": valid_model_name,
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
        print(f"[ORACLE ERROR] Classification failed. Detail: {error_detail}")
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
        
    topic = sys.argv[1]
    
   if not os.path.exists("new_papers.json"):
        sys.exit(0)
        
    api_base = os.environ.get("OPENAI_API_BASE", "https://api.ailabroma3.it/v1")
    api_key = os.environ.get("OPENAI_API_KEY", "")
    
    valid_model_name = get_valid_model_name(api_base, api_key)
    # If the server fails to return the model name, force the new default
    if valid_model_name == "lab-main": 
        valid_model_name = "lab-qwen36"
        
    print(f"\n[ORACLE] Valid API model identified: '{valid_model_name}'")
        
    with open("new_papers.json", "r", encoding="utf-8") as f:
        papers = json.load(f)
        
    truth_dict = {}
    print(f"[ORACLE] Auto-generating Ground Truth for {len(papers)} papers...")
    print(f"[ORACLE] Rate Limiting Active: Waiting 8 seconds between requests.")
    
    for p in papers:
        is_relevant = classify_with_llm(topic, p['abstract'], valid_model_name)
        truth_dict[p['id']] = is_relevant
        print(f" -> Processed {p['id']} | Relevant: {is_relevant}")
        # SAFETY LOCK: pause the script for 8 seconds to respect rate limits (max 8 req/min)
        time.sleep(8) 
        
    with open("ground_truth.json", "w", encoding="utf-8") as f:
        json.dump(truth_dict, f, indent=2)

    print("[ORACLE] ground_truth.json generated successfully!")