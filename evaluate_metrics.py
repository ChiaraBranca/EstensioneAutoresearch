import json
import re
import os
import sys

def load_ground_truth(filepath):
    """Carica le valutazioni umane dal file JSON."""
    if not os.path.exists(filepath):
        print(f"Errore: File {filepath} non trovato.")
        sys.exit(1)
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_integrated_papers(bib_file):
    """Estrae gli ID dei paper che l'AI ha effettivamente deciso di includere."""
    if not os.path.exists(bib_file):
        return set()
    with open(bib_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Trova le chiavi BibTeX usando la stessa Regex che hai in prepare.py
    ids = set(re.findall(r'@\w+\{([^,]+),', content))
    return {i.split('v')[0] for i in ids}

def evaluate_performance(ground_truth_file, bib_file):
    ground_truth = load_ground_truth(ground_truth_file)
    integrated_ai = get_integrated_papers(bib_file)

    TP, FP, FN, TN = 0, 0, 0, 0

    for paper_id, is_relevant_gt in ground_truth.items():
        # [NUOVO] Togliamo la 'v' (es. 2409.13191v2 -> 2409.13191) per fare un confronto pulito
        base_id = str(paper_id).split('v')[0]
        
        # Ora cerchiamo il base_id pulito dentro la lista dell'AI
        is_relevant_ai = 1 if base_id in integrated_ai else 0

        if is_relevant_ai == 1 and is_relevant_gt == 1:
            TP += 1
        elif is_relevant_ai == 1 and is_relevant_gt == 0:
            FP += 1
        elif is_relevant_ai == 0 and is_relevant_gt == 1:
            FN += 1
        elif is_relevant_ai == 0 and is_relevant_gt == 0:
            TN += 1
    # Prevenzione divisione per zero
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0.0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0.0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
    accuracy = (TP + TN) / len(ground_truth) if len(ground_truth) > 0 else 0.0

    print("\n" + "="*50)
    print(" 📊 VALIDAZIONE ESTERNA: METRICHE INFORMATION RETRIEVAL")
    print("="*50)
    print(f"Totale paper valutati nel campione: {len(ground_truth)}\n")
    
    print("Matrice di Confusione:")
    print(f"  - True Positives (TP):  {TP} (Inclusi correttamente)")
    print(f"  - False Positives (FP): {FP} (Allucinazioni/Fuori tema inclusi)")
    print(f"  - False Negatives (FN): {FN} (Paper utili persi/scartati)")
    print(f"  - True Negatives (TN):  {TN} (Scartati correttamente)\n")
    
    print("Metriche:")
    print(f"  🎯 Precision: {precision:.4f} (Quando l'AI include un paper, al {precision*100:.1f}% è quello giusto)")
    print(f"  🔍 Recall:    {recall:.4f} (L'AI riesce a trovare il {recall*100:.1f}% di tutta la letteratura utile)")
    print(f"  ⚖️  F1-Score:  {f1:.4f} (Media armonica tra Precision e Recall)")
    print(f"  ✅ Accuracy:  {accuracy:.4f} (Decisioni totali corrette)")
    print("="*50 + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python evaluate_metrics.py <nome_cartella_argomento>")
        print("Es:  python evaluate_metrics.py agenti_llm")
        sys.exit(1)
        
    topic_dir = sys.argv[1]
    gt_file = "ground_truth.json"
    bib_path = os.path.join("surveys", topic_dir, "references.bib")
    
    evaluate_performance(gt_file, bib_path)