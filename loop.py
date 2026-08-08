import os
import sys
import subprocess
import re
import shutil
from datetime import datetime

# Configurazione automatica ambiente locale
os.environ["OPENAI_API_BASE"] = "http://127.0.0.1:9000/v1"
os.environ["OPENAI_API_KEY"] = "none"

def run_command(cmd, capture_output=True):
    """Esegue un comando di sistema reale e ne restituisce l'output."""
    print(f"\n[SISTEMA] Esecuzione: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    result = subprocess.run(cmd, shell=isinstance(cmd, str), text=True, capture_output=capture_output)
    if result.stdout and capture_output:
        print(result.stdout.strip())
    if result.stderr and capture_output and result.returncode != 0:
        print(f"[ERRORE SISTEMA] {result.stderr.strip()}")
    return result

def get_lss_score(topic):
    """Esegue prepare.py --eval e fa il parsing del punteggio LSS reale dal terminale."""
    res = run_command(f'python prepare.py --eval "{topic}"')
    match = re.search(r'LSS_SCORE:\s*([0-9.]+)', res.stdout)
    if match:
        return float(match.group(1))
    return 0.0

def run_autonomous_loop(topic, iterations=1, search_query=None):
    if not search_query:
        search_query = topic

    print(f"==================================================")
    print(f" AVVIO LIVING SURVEY: Progetto '{topic}' | Query ArXiv: '{search_query}'")
    print(f"==================================================")
    
    # 1. Inizializzazione Workspace
    run_command(f'python prepare.py --init "{topic}"')
    
    clean_name = re.sub(r'[^a-zA-Z0-9]', '_', topic.lower()).strip('_')
    topic_dir = os.path.join("surveys", clean_name)
    
    survey_file = os.path.join(topic_dir, f"{clean_name}.md")
    bib_file = os.path.join(topic_dir, "references.bib")
    fig_script = os.path.join(topic_dir, "generate_figures.py")

    for i in range(1, iterations + 1):
        print(f"\n──────────────────────────────────────────────────")
        print(f" CICLO {i}/{iterations} - RECUPERO LETTERATURA")
        print(f"──────────────────────────────────────────────────")
        
        # Recupero nuovi paper
        fetch_res = run_command(f'python prepare.py --fetch "{topic}" "{search_query}"')
        if "Recuperati 0" in fetch_res.stdout or fetch_res.returncode != 0:
            print("[STOP] Nessun nuovo paper recuperato da ArXiv. Eseguo pulizia e termino.")
            run_command("git checkout .")
            run_command("git clean -fd")
            break
            
        # Misurazione Baseline
        baseline_score = get_lss_score(topic)
        print(f"[METRICA] Punteggio LSS Baseline di partenza: {baseline_score}")

        # =======================================================
        # [NUOVO] GENERAZIONE GROUND TRUTH TRAMITE ORACOLO
        # =======================================================
        print("\n[ORACLE] Generazione Ground Truth (LLM-as-a-Judge)...")
        run_command(f'python auto_evaluator.py "{search_query}"')

        # Prompt Attore
        prompt_attore = (
            f"Leggi attentamente il file 'new_papers.json'. Contiene una lista di paper INEDITI. Per ogni paper all'interno:\n"
            f"1) SCREENING DI PERTINENZA: Valuta se è pertinente al tema e ai vincoli richiesti: '{search_query}'. Se è fuori tema o fuori dall'anno/periodo richiesto, scartalo e ignoralo.\n"
            f"2) Se è pertinente, INTEGRA un'analisi sintetica in '{survey_file}' usando citazioni Markdown tipo [^id_paper]. "
            f"REGOLE DI ESPANSIONE: Se '{survey_file}' contiene già del testo dai cicli precedenti, NON CANCELLARE o riassumere nulla del lavoro passato! Aggiungi i nuovi paper arricchendo le sezioni esistenti o creando nuove sottosezioni in modo organico.\n"
            f"3) Aggiungi le nuove voci bibliografiche in '{bib_file}' (mantenendo intatte le voci preesistenti).\n"
            f"4) Aggiorna i dizionari TIMELINE_DATA e TAXONOMY_DATA all'inizio di '{fig_script}' SOMMANDO i nuovi conteggi ai valori già presenti nel codice.\n"
            f"5) PULIZIA E FORMATTAZIONE: Rimuovi tassativamente dal file '{survey_file}' qualsiasi intestazione di sezione vuota o priva di testo sottostante (ad esempio '## Letteratura Recente' o '## Analisi Comparativa' se non hanno contenuto). Il documento deve contenere solo sezioni piene e argomentate!\n"
            f"NON inventare comandi terminale, NON scrivere codice LaTeX, limitati a modificare i file richiesti."
        )

        print("\n[AI AGENT - ATTORE] Scrittura e integrazione nuova letteratura...")
        run_command(f'uvx --from aider-chat aider --model openai/lab-main --read prepare.py --read program.md --read new_papers.json --yes-always --no-git --message "{prompt_attore}" {survey_file} {bib_file} {fig_script}')

        # Prompt Critico con Memoria Storica
        prompt_critico = (
            f"Agisci come un revisore scientifico spietato (Reviewer 2). "
            f"Confronta attentamente le ultime aggiunte fatte in '{survey_file}' con gli abstract reali presenti in 'new_papers.json'. "
            f"REGOLE DI REVISIONE E MEMORIA STORICA:\n"
            f"1) RISPETTO DEL PASSATO: Il file '{survey_file}' contiene citazioni di cicli precedenti (già registrate in '{bib_file}'). Se una citazione NON si trova in 'new_papers.json' ma fa parte del lavoro storico preesistente o è presente in '{bib_file}', NON CANCELLARLA ASSOLUTAMENTE! È letteratura già verificata in passato.\n"
            f"2) VERIFICA NUOVI INSERIMENTI: Esamina ESCLUSIVAMENTE le affermazioni legate ai paper scaricati nel corrente 'new_papers.json'. Per questi, verifica se l'abstract sostiene DAVVERO quanto scritto o se ci sono allucinazioni/esagerazioni.\n"
            f"3) Se trovi una singola esagerazione, falsità o dato non supportato tra i NUOVI paper, cancella SOLO quella frase o paragrafo incriminato senza toccare il resto del documento.\n"
            f"NON inventare codice, limitati alla revisione mirata di '{survey_file}'."
        )

        print("\n[AI AGENT - CRITICO] Peer-review e verifica veridicità scientifica...")
        run_command(f'uvx --from aider-chat aider --model openai/lab-main --read new_papers.json --read {bib_file} --yes-always --no-git --message "{prompt_critico}" {survey_file}')

        # Esecuzione script dei grafici
        print("\n[SISTEMA] Ricreazione reale dei grafici su disco...")
        run_command(f'python "{fig_script}"')

        # =======================================================
        # [NUOVO] CALCOLO METRICHE DI VALIDAZIONE
        # =======================================================
        # Lo mettiamo qui in modo da misurare l'effettivo lavoro degli agenti
        # prima di fare eventuali rollback con git reset
        print("\n[METRICHE] Calcolo Precision, Recall e F1-Measure...")
        run_command(f'python evaluate_metrics.py "{clean_name}"')

        # Valutazione Reale e Verdetto
        new_score = get_lss_score(topic)
        delta = round(new_score - baseline_score, 2)
        print(f"\n[VERDETTO] Baseline: {baseline_score} -> Nuovo Score: {new_score} (Δ {delta:+.2f})")

        if new_score > baseline_score:
            print("[SUCCESS] Miglioramento confermato! Eseguo Git Commit.")
            run_command("git add .")
            run_command(f'git commit -m "feat({clean_name}): integrated valid papers (LSS: {new_score})" ')
        else:
            print("[REJECT] Nessun miglioramento (o errore di sintassi/allucinazione bloccata). Eseguo Git Reset!")
            run_command("git reset --hard HEAD")
            run_command("git clean -fd")

        # =======================================================
        # [NUOVO] SISTEMA DI ARCHIVIAZIONE LOG JSON
        # =======================================================
        logs_dir = os.path.join(topic_dir, "eval_logs")
        os.makedirs(logs_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if os.path.exists("new_papers.json"):
            new_papers_archive = os.path.join(logs_dir, f"new_papers_{timestamp}.json")
            shutil.move("new_papers.json", new_papers_archive)
            
        if os.path.exists("ground_truth.json"):
            gt_archive = os.path.join(logs_dir, f"ground_truth_{timestamp}.json")
            shutil.move("ground_truth.json", gt_archive)
            
        print(f"[LOG] File JSON archiviati con successo in: {logs_dir} (Timestamp: {timestamp})")

    print("\n==================================================")
    print(" LOOP COMPLETATO CON SUCCESSO!")
    print("==================================================")
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python loop.py \"Nome Progetto\" [numero_cicli] [\"Query o Filtro Anno\"]")
        sys.exit(1)
    
    arg_topic = sys.argv[1]
    arg_iterations = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    arg_query = sys.argv[3] if len(sys.argv) > 3 else None
    
    run_autonomous_loop(arg_topic, arg_iterations, arg_query)