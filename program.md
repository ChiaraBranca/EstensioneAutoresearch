# Living Survey AutoResearch Directive

Tu sei un agente AI ricercatore autonomo. Il tuo obiettivo è mantenere aggiornata la survey scientifica in `survey_draft.tex` massimizzando lo score di qualità LSS.

## Protocollo del Loop di Ricerca

1. **Recupero Nuova Letteratura:**
   Esegui `python prepare.py --fetch` per aggiornare `new_papers.json`.

2. **Screening e Pertinenza:**
   - Leggi `new_papers.json`. Filtra solo i paper strettamente pertinenti al tema trattato nella survey.
   - All'inizio dell'analisi di ciascun paper candidato, traccia l'inizio del ciclo nel terminale:
     `[LOOP XXX/YYY] Paper ID: <paper_id> | "<titolo_troncato_30_caratteri>"`

3. **Modifica Sorgente (`survey_draft.tex` & `references.bib`):**
   - **Gerarchia e Formattazione del Testo:**
     Maniene e interpreta la struttura concettuale basata sull'indentazione visiva:
     - **Titolo Principale** (Sezione)
         - **Sottotitolo / Argomento / Paper** (Sottosezione)
             - *Analisi critica e citazioni*
     TRADUZIONE SILENZIOSA: Converti automaticamente questa gerarchia visiva nei tag LaTeX corretti all'interno di `survey_draft.tex`. L'utente non deve mai specificare comandi manuali come `\section`, `\subsection` o altri tag nel prompt.
   - Aggiorna la tabella comparativa dei metodi esistente.
   - Inserisci la voce BibTeX corrispondente in `references.bib`.

4. **Rigenerazione Grafici:**
   Esegui o aggiorna `generate_figures.py` per ricreare i grafici di distribuzione temporale o di performance nella cartella `figures/`.

5. **Valutazione, Git Control e Telemetria Terminale:**
   - Calcola il tempo di esecuzione del singolo ciclo ($dt$).
   - Esegui `python prepare.py --eval` e rileva il valore `LSS_SCORE`.
   - Calcola la variazione: $\Delta LSS = \text{nuovo\_LSS} - \text{baseline\_LSS}$.

   - **Se `LSS_SCORE` è AUMENTATO (ACCEPTED):**
     1. Esegui: `git add .`
     2. Esegui: `git commit -m "feat: integrated paper <paper_id> (LSS: <nuovo_LSS>)"`
     3. Stampa nel terminale:
        `  └─ status: [ACCEPTED] | LSS: <nuovo_LSS> (Δ +<delta>) | dt: <dt>s`
     4. Imposta il nuovo valore come baseline per il ciclo successivo.

   - **Se la compilazione fallisce o `LSS_SCORE` non aumenta (REJECTED):**
     1. Esegui: `git reset --hard HEAD`
     2. Stampa nel terminale:
        `  └─ status: [REJECTED] | LSS: <baseline_LSS> (Δ 0.00) | dt: <dt>s`

6. **Riepilogo Finale di Sessione:**
   Al termine dell'elaborazione di tutti i paper in `new_papers.json`, stampa a schermo la tabella riassuntiva finale:

==================================================
LIVING SURVEY AUTORESEARCH SUMMARY
==================================================
total_papers_evaluated: <totale_paper>
papers_accepted:        <conteggio_accepted>
papers_rejected:        <conteggio_rejected>
acceptance_rate:        <percentuale_successo>%
initial_lss_score:      <score_iniziale>
final_lss_score:        <score_finale>
total_lss_gain:         +<guadagno_totale>
total_seconds:          <tempo_totale_secondi>s
==================================================