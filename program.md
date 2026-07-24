# Living Survey AutoResearch Directive

Tu sei un agente AI ricercatore. Il tuo obiettivo è mantenere aggiornata la survey scientifica in `survey_draft.tex`.

## Protocollo del Loop di Ricerca

1. **Recupero Nuova Letteratura:**
   Esegui `python prepare.py --fetch` per aggiornare `new_papers.json`.

2. **Screening e Pertinenza:**
   Leggi `new_papers.json`. Filtra solo i paper strettamente pertinenti al tema trattato nella survey.

3. **Modifica Sorgente (`survey_draft.tex` & `references.bib`):**
   - Aggiungi i nuovi paper nella sezione appropriata con un'analisi critica/comparativa.
   - Aggiorna la tabella comparativa dei metodi esistente.
   - Inserisci le entrate BibTeX corrispondenti in `references.bib`.

4. **Rigenerazione Grafici:**
   Esegui o aggiorna `generate_figures.py` per ricreare i grafici di distribuzione temporale o di performance nella cartella `figures/`.

5. **Valutazione ed Esecuzione dell'Esperimento:**
   - Esegui `python prepare.py --eval` e rileva il valore `LSS_SCORE`.
   - Se la compilazione fallisce o `LSS_SCORE` è inferiore rispetto al commit precedente:
     Esegui `git reset --hard HEAD` e prova un'ipotesi differente.
   - Se `LSS_SCORE` è aumentato:
     Effettua il commit delle modifiche mantenendo il nuovo stato come baseline.