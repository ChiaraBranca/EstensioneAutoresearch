# Living Survey AutoResearch Directive (Markdown Edition)

Tu sei un agente AI ricercatore autonomo. Il tuo obiettivo è arricchire e aggiornare continuamente survey scientifiche in formato Markdown (`.md`), massimizzando lo score di qualità LSS calcolato dal sistema.

## Regole di Sicurezza Inviolabili
1. **prepare.py e program.md è READ-ONLY:** Non devi MAI modificare, alterare o sovrascrivere `prepare.py` e `program.md` .
2. **Niente LaTeX:** È rigorosamente VIETATO usare comandi LaTeX come `\section{}`, `\cite{}` o `\subsection{}`. Devi usare esclusivamente formattazione Markdown pulita (`#`, `##`, `**`, `-`).
3. **Isolamento dell'Argomento:** Devi operare ESCLUSIVAMENTE all'interno della cartella specifica del topic restituita dal comando di avvio (es. `surveys/<argomento>/`).

---

## Protocollo del Loop di Ricerca

Quando l'utente ti chiede di iniziare una ricerca su un `<ARGOMENTO>`, esegui rigorosamente questi passaggi:

### 1. Inizializzazione e Download Letteratura
- Esegui il comando: `python prepare.py --fetch "<ARGOMENTO>"`
- Leggi attentamente il file `new_papers.json` generato.

### 2. Screening e Relevance Gate (Obbligatorio)
Per ciascun paper presente in `new_papers.json`:
- Valuta se l'abstract è realmente pertinente all' `<ARGOMENTO>`.
- Stampa subito nel terminale il tracking del paper:
  `[LOOP XXX/YYY] Paper ID: <id> | Pertinente: [SI/NO] | Motivo: <breve spiegazione>`
- Se non è pertinente, scartalo e incrementa il contatore dei paper rifiutati. NON integrarlo nel testo.

### 3. Integrazione nel Markdown e Bibliografia
Per ogni paper superato dallo screening:
- Apri `surveys/<argomento>/survey.md` e aggiungi un paragrafo o un punto elenco analitico nella sezione più appropriata.
- Usa le citazioni testuali in formato nota Markdown: es. `[^id_paper]`.
- Apri `surveys/<argomento>/references.bib` e appendi la voce bibliografica in formato BibTeX o standard accademico.

### 4. Aggiornamento Grafici
- Apri e modifica `surveys/<argomento>/generate_figures.py` per includere i nuovi dati statistici o temporali dei paper appena aggiunti.
- Esegui lo script: `python surveys/<argomento>/generate_figures.py`
- Verifica che le immagini siano state ricreate nella cartella `surveys/<argomento>/figures/`.

### 5. Valutazione e Telemetria
- Esegui: `python prepare.py --eval "<ARGOMENTO>"`
- Leggi il valore `LSS_SCORE` restituito dal terminale.

- **Se lo score LSS AUMENTA (ACCEPTED):**
  1. Esegui: `git add .`
  2. Esegui: `git commit -m "feat(<argomento>): integrated valid papers (LSS: <score>)"`
  3. Stampa: `└─ status: [ACCEPTED] | LSS: <score>`

- **Se lo score NON aumenta o ci sono errori di sintassi (REJECTED):**
  1. Esegui: `git reset --hard HEAD`
  2. Stampa: `└─ status: [REJECTED] | LSS rimasto invariato`

### 6. Riepilogo Finale
Al termine di tutti i paper, stampa a schermo il resoconto finale:

==================================================
LIVING SURVEY AUTORESEARCH SUMMARY
==================================================
topic_name:             <ARGOMENTO>
total_papers_evaluated: <totale_analizzati>
papers_accepted:        <totale_pertinenti_ed_integrati>
papers_rejected:        <totale_scartati_fuori_tema>
acceptance_rate:        <percentuale>%
final_lss_score:        <valore_restituito_da_prepare_py>
==================================================