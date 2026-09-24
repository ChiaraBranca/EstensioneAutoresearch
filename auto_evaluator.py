"""
=============================================================================
FILE: auto_evaluator.py
DESCRIPTION: 
This script acts as the "Oracle" in the framework, but uses CLASSICAL INFORMATION RETRIEVAL.
Instead of asking an LLM to judge (which causes self-preference bias), it uses a 
Transformer Embedding model ('lab-embed') to convert the topic and abstracts into vectors.
It then calculates the Cosine Similarity. If the similarity is above a threshold, 
the paper is Ground Truth = 1, otherwise 0. This provides a completely external 
and mathematical baseline to calculate Precision, Recall, and F1-Score.
=============================================================================
"""

import os
import sys
import json
import urllib.request
import math
import time
from dotenv import load_dotenv

load_dotenv()

# Relevance threshold (Information Retrieval)
# Embedding values typically range between -1 and 1. A value > 0.50 usually indicates good semantic relevance.
#
# NOTE (updated after manual testing across several topics): 0.50 was found to let through
# papers that only share generic vocabulary with the topic (weak positives) while sometimes
# scoring non-English or unusually phrased abstracts too low (false negatives). Observed
# cosine similarities for manually-confirmed relevant papers clustered mostly >= 0.50,
# while borderline/irrelevant ones clustered in the 0.50-0.57 band. 0.50 is used as the new
# default, but THIS STILL NEEDS VALIDATION ACROSS MORE TOPICS before being trusted blindly -
# hence it is kept overridable via the RELEVANCE_THRESHOLD environment variable, e.g.:
#   RELEVANCE_THRESHOLD=0.50 python loop.py "topic" 1 "query"
# to A/B test different thresholds on the same or comparable fetches without editing this file.
RELEVANCE_THRESHOLD = float(os.environ.get("RELEVANCE_THRESHOLD", "0.50"))

def get_embedding(text, api_base, api_key):
    """Fetches the mathematical vector (embedding) for a given text from the API."""
    url = f"{api_base}/embeddings"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "model": "lab-embed", # Using the specific embedding model indicated for the server
        "input": text
    }).encode('utf-8')
    
    try:
        req = urllib.request.Request(url, data=data, headers=headers)
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            return result['data'][0]['embedding']
    except Exception as e:
        print(f"[EMBEDDING ERROR] Failed to fetch embedding: {e}")
        return None

def cosine_similarity(vec1, vec2):
    """Calculates the Cosine Similarity between two vectors (Classical Information Retrieval formula)."""
    if not vec1 or not vec2:
        return 0.0
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm_a = math.sqrt(sum(a * a for a in vec1))
    norm_b = math.sqrt(sum(b * b for b in vec2))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
        
    topic = sys.argv[1]
    
    if not os.path.exists("new_papers.json"): 
        sys.exit(0)
        
    api_base = os.environ.get("OPENAI_API_BASE", "https://api.ailabroma3.it/v1")
    api_key = os.environ.get("OPENAI_API_KEY", "")
    
    print(f"\n[ORACLE - INFORMATION RETRIEVAL MODE]")
    print(f"Using 'lab-embed' to compute vector similarities (Threshold: {RELEVANCE_THRESHOLD})")
    
    # 1. Compute the embedding for the Topic (our reference Query)
    # VERSIONE UNIVERSALE (DOMINIO-AGNOSTICA)
    enriched_topic = f"Interdisciplinary scientific research, clinical studies, computational methods, and technological applications concerning {topic}."
    topic_embedding = get_embedding(enriched_topic, api_base, api_key)
    if not topic_embedding:
        print("[ORACLE FATAL] Could not compute embedding for the topic. Exiting.")
        sys.exit(1)
        
    with open("new_papers.json", "r", encoding="utf-8") as f:
        papers = json.load(f)
        
    truth_dict = {}
    # Raw (non-binarized) cosine scores, kept alongside the binary ground_truth.json.
    # This lets you retroactively simulate "what would have happened with threshold X"
    # without re-computing embeddings, and lets you plot the distribution of scores for
    # relevant vs. irrelevant papers (useful evidence for the thesis' discussion of the
    # Oracle's limitations).
    scores_dict = {}
    print(f"[ORACLE] Auto-generating Ground Truth for {len(papers)} papers using Cosine Similarity...")
    
    for p in papers:
        # 2. Compute the embedding for the abstract
        abstract_emb = get_embedding(p['abstract'], api_base, api_key)
        
        # 3. Calculate the similarity metric
        sim_score = cosine_similarity(topic_embedding, abstract_emb)
        
        # 4. Assign 1 or 0 based on the threshold
        is_relevant = 1 if sim_score >= RELEVANCE_THRESHOLD else 0
        truth_dict[p['id']] = is_relevant
        scores_dict[p['id']] = round(sim_score, 4)
        
        print(f" -> Processed {p['id']} | Cosine Sim: {sim_score:.3f} | Relevant: {is_relevant}")
        
        # Progressive saving to avoid data loss
        with open("ground_truth.json", "w", encoding="utf-8") as f:
            json.dump(truth_dict, f, indent=2)
        with open("cosine_scores.json", "w", encoding="utf-8") as f:
            json.dump(scores_dict, f, indent=2)
            
        # Safety pause to respect API rate limits (max 8 req/min)
        time.sleep(10) 
        
    print("[ORACLE] ground_truth.json generated successfully!")
    print("[ORACLE] cosine_scores.json (raw scores, for threshold analysis) generated successfully!")