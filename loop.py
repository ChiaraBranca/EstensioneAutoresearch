import os
import sys
import subprocess
import re

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

def run_autonomous_loop(topic, iterations=1):
    print(f"==================================================")
    print(f" AVVIO LIVING SURVEY AUTORESEARCH: '{topic}'")
    print(f"==================================================")
    
    # 1. Inizializzazione Workspace reale
    run_command(f'python prepare.py --init "{topic}"')
    
    # Cartella di lavoro per questo argomento (es. surveys/dinosaurs)
    clean_name = re.sub(r'[^a-zA-Z0-9]', '_', topic.lower()).strip('_')
    topic_dir = os.path.join("surveys", clean_name)
    
    # IL FILE SI CHIAMA COME IL TOPIC (es. dinosaurs.md)
    survey_file = os.path.join(topic_dir, f"{clean_name}.md")
    
    bib_file = os.path.join(topic_dir, "references.bib")
    fig_script = os.path.join(topic_dir, "generate_figures.py")

    for i in range(1, iterations + 1):
        print(f"\n──────────────────────────────────────────────────")
        print(f" CICLO {i}/{iterations} - RECUPERO LETTERATURA")
        print(f"──────────────────────────────────────────────────")
        
        # 2. Fetch reale da ArXiv
        fetch_res = run_command(f'python prepare.py --fetch "{topic}"')
        if "Recuperati 0" in fetch_res.stdout or fetch_res.returncode != 0:
            print("[STOP] Nessun nuovo paper recuperato da ArXiv. Termino il loop.")
            break
            
        # 3. Misurazione Baseline
        baseline_score = get_lss_score(topic)
        print(f"[METRICA] Punteggio LSS Baseline di partenza: {baseline_score}")

        # 4. Costruzione del Prompt per Aider (Solo Editing del Testo!)
        prompt = (
            f"Leggi attentamente il file 'new_papers.json'. Per ogni paper all'interno: "
            f"1) Valuta se è realmente pertinente al tema '{topic}'. Se non è pertinente, scartalo e ignoralo. "
            f"2) Se è pertinente, aggiungi un'analisi sintetica in '{survey_file}' usando citazioni Markdown tipo [^id_paper]. "
            f"3) Aggiungi la voce bibliografica in '{bib_file}'. "
            f"4) Aggiorna SOLTANTO i dizionari TIMELINE_DATA e TAXONOMY_DATA all'inizio di '{fig_script}'. "
            f"NON inventare comandi terminale, NON scrivere codice LaTeX, limitati a modificare i file richiesti."
        )

        # 5. Esecuzione di Aider (Usa la configurazione di default del tuo sistema!)
        print("\n[AI AGENT] Passo il controllo a Qwen per lo screening e la scrittura...")
        aider_cmd = [
            "aider",
            # Rimosso il parametro --model per usare il modello Qwen che usi di solito
            "--read", "prepare.py",
            "--read", "program.md",
            "--read", "new_papers.json",
            "--yes-always",                # Risponde sempre sì ai prompt di conferma di aider
            "--no-git",                    # Diciamo ad aider di non committare, lo controlla loop.py!
            "--message", prompt,
            survey_file,
            bib_file,
            fig_script
        ]
        run_command(aider_cmd, capture_output=False) # Stampa l'output di Aider in tempo reale

        # 6. Esecuzione reale dello script dei grafici (generazione Matplotlib su disco)
        print("\n[SISTEMA] Ricreazione reale dei grafici su disco...")
        run_command(f'python "{fig_script}"')

        # 7. Valutazione Reale e Verdetto (Il computer decide se accettare!)
        new_score = get_lss_score(topic)
        delta = round(new_score - baseline_score, 2)
        print(f"\n[VERDETTO] Baseline: {baseline_score} -> Nuovo Score: {new_score} (Δ {delta:+.2f})")

        if new_score > baseline_score:
            print("[SUCCESS] Miglioramento confermato! Eseguo Git Commit.")
            run_command("git add .")
            run_command(f'git commit -m "feat({clean_name}): integrated valid papers (LSS: {new_score})" ')
        else:
            print("[REJECT] Nessun miglioramento (o errore di sintassi). Eseguo Git Reset!")
            run_command("git reset --hard HEAD")
            run_command("git clean -fd") # Rimuove file temporanei indesiderati

    print("\n==================================================")
    print(" LOOP COMPLETATO CON SUCCESSO!")
    print("==================================================")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python loop.py \"Nome Argomento\" [numero_cicli]")
        sys.exit(1)
    
    arg_topic = sys.argv[1]
    arg_iterations = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    run_autonomous_loop(arg_topic, arg_iterations)