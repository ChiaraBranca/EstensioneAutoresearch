import os
import sys
import subprocess
import re

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

def run_autonomous_loop(topic, iterations=1):
    print(f"==================================================")
    print(f" AVVIO LIVING SURVEY AUTORESEARCH: '{topic}'")
    print(f"==================================================")
    
    # 1. Inizializzazione Workspace reale
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
        
        # 2. Fetch reale da ArXiv
        fetch_res = run_command(f'python prepare.py --fetch "{topic}"')
        if "Recuperati 0" in fetch_res.stdout or fetch_res.returncode != 0:
            print("[STOP] Nessun nuovo paper recuperato da ArXiv. Termino il loop.")
            break
            
        # 3. Misurazione Baseline
        baseline_score = get_lss_score(topic)
        print(f"[METRICA] Punteggio LSS Baseline di partenza: {baseline_score}")

# 4.a Costruzione del Prompt per L'ATTORE (Scrittura e integrazione incrementale)
        prompt_attore = (
            f"Leggi attentamente il file 'new_papers.json'. Contiene una lista di paper INEDITI. Per ogni paper all'interno:\n"
            f"1) Valuta se è realmente pertinente al tema '{topic}'. Se non è pertinente, scartalo e ignoralo.\n"
            f"2) Se è pertinente, INTEGRA un'analisi sintetica in '{survey_file}' usando citazioni Markdown tipo [^id_paper]. "
            f"REGOLE DI ESPANSIONE: Se '{survey_file}' contiene già del testo dai cicli precedenti, NON CANCELLARE o riassumere nulla del lavoro passato! Aggiungi i nuovi paper arricchendo le sezioni esistenti o creando nuove sottosezioni in modo organico.\n"
            f"3) Aggiungi le nuove voci bibliografiche in '{bib_file}' (mantenendo intatte le voci preesistenti).\n"
            f"4) Aggiorna i dizionari TIMELINE_DATA e TAXONOMY_DATA all'inizio di '{fig_script}' SOMMANDO i nuovi conteggi ai valori già presenti nel codice.\n"
            f"NON inventare comandi terminale, NON scrivere codice LaTeX, limitati a modificare i file richiesti."
        )

        # Esecuzione PASSO 1: L'Attore
        print("\n[AI AGENT - ATTORE] Scrittura e integrazione nuova letteratura...")
        run_command(f'uvx --from aider-chat aider --model openai/lab-main --read prepare.py --read program.md --read new_papers.json --yes-always --no-git --message "{prompt_attore}" {survey_file} {bib_file} {fig_script}')

        # 4.b Costruzione del Prompt per IL CRITICO (Peer-review e anti-allucinazione)
        prompt_critico = (
            f"Agisci come un revisore scientifico spietato (Reviewer 2). "
            f"Confronta attentamente le ultime aggiunte fatte in '{survey_file}' con gli abstract reali presenti in 'new_papers.json'. "
            f"Per ogni nuova citazione e affermazione rispondi a queste regole: "
            f"1) VERIDICITÀ: L'abstract in 'new_papers.json' sostiene DAVVERO quanto scritto nel testo, o il modello precedente ha allucinato, esagerato o frainteso? "
            f"2) CONSENSO SCIENTIFICO: Ci sono affermazioni palesemente assurde, errori matematici o fallacie metodologicamente inaccettabili? "
            f"Se trovi una singola esagerazione, falsità o dato non supportato dall'abstract, CANCELLA COMPLETAMENTE il paragrafo incriminato da '{survey_file}' e rimuovi la relativa tag [^id]. "
            f"Se è tutto rigorosamente verificato e fedele alla fonte, non toccare nulla. NON inventare codice, limitati alla revisione di '{survey_file}'."
        )

        # Esecuzione PASSO 2: Il Critico
        print("\n[AI AGENT - CRITICO] Peer-review e verifica veridicità scientifica...")
        run_command(f'uvx --from aider-chat aider --model openai/lab-main --read new_papers.json --yes-always --no-git --message "{prompt_critico}" {survey_file}')

        # 5. Esecuzione di Aider tramite uvx con il modello locale corretto
        print("\n[AI AGENT] Passo il controllo a openai/lab-main per lo screening e la scrittura...")
        aider_cmd = [
            "uvx",
            "--from", "aider-chat",
            "aider",
            "--model", "openai/lab-main",
            "--read", "prepare.py",
            "--read", "program.md",
            "--read", "new_papers.json",
            "--yes-always",
            "--no-git",
            "--message", prompt,
            survey_file,
            bib_file,
            fig_script
        ]
        run_command(aider_cmd, capture_output=False)

        # 6. Esecuzione reale dello script dei grafici
        print("\n[SISTEMA] Ricreazione reale dei grafici su disco...")
        run_command(f'python "{fig_script}"')

        # 7. Valutazione Reale e Verdetto
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
            run_command("git clean -fd")

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