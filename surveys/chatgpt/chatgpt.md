# Living Survey: chatgpt

## Introduzione

Questo documento raccoglie la letteratura scientifica sul tema **chatgpt**.

## Applicazioni e Valutazioni Specifiche

La letteratura recente evidenzia l'ampia adattabilità di ChatGPT e dei modelli linguistici di grandi dimensioni (LLM) a domini specialistici, sebbene con prestazioni variabili.

### Traduzione e Correzione Grammaticale
ChatGPT ha dimostrato capacità competitive nella traduzione automatica, specialmente per lingue ad alta risorsa, sebbene le prestazioni calino per lingue a bassa risorsa o domini tecnici come la biomedicina. L'uso di strategie come il "pivot prompting" può migliorare i risultati. Inoltre, ChatGPT mostra potenziale nella correzione degli errori grammaticali (GEC), preferendo spesso la riscrittura strutturale rispetto alla correzione parola per parola, superando alcuni metrici automatici ma mostrando tendenze all'over-correction [^2301.08745v4] [^2303.13648v1].

### Generazione di Codice e Supporto allo Sviluppo
Nella generazione di codice, ChatGPT-4 mostra competenze superiori nelle lingue più diffuse e tipate staticamente, ma fatica con problemi complessi e lingue meno comuni. È utile per compiti di debugging e interpretazione, ma non sostituisce ancora la competenza di uno sviluppatore esperto per sistemi complessi [^2501.02338v1]. Similmente, nel contesto dei workflow scientifici, ChatGPT aiuta nella comprensione e nell'adattamento dei flussi di lavoro, ma ha limitazioni nell'estensione purposeful o nello scambio di componenti [^2311.01825v2].

### Domini Specialistici: Matematica, Finanza e Salute
*   **Matematica e Topologia:** ChatGPT è efficace come assistente per la ricerca di fatti e l'interfaccia di basi di conoscenza, ma fallisce su problemi di livello graduate-level. Tuttavia, può essere utilizzato da teorici per generare codice per l'analisi topologica computazionale, colmando il gap tra teoria e implementazione [^2301.13867v2] [^2310.07570v3].
*   **Finanza:** L'integrazione di ChatGPT con le Graph Neural Networks (GNN) per inferire strutture dinamiche dalle notizie finanziarie ha mostrato risultati superiori ai benchmark deep learning tradizionali nella previsione dei movimenti azionari [^2306.03763v4].
*   **Salute e Biometria:** Per i corpora medici, l'integrazione di ChatGPT con ensemble learning è stata esplorata per migliorare il riconoscimento di entità non continue (DNER) [^2412.16976v3]. Riguardo alle biometrie, è stata condotta un'assessment delle capacità di ChatGPT nel riconoscimento facciale, nel rilevamento del genere e dell'età [^2403.02965v2].
*   **Geoscienze e Telerilevamento:** ChatGPT agisce come agente per pianificare ed eseguire compiti di telerilevamento, connettendo vari modelli AI. Mostra anche buone capacità nella literacy spaziale e nella teoria GIS, ma debolezze nel ragionamento spaziale complesso e nella scrittura di codice [^2401.09083v1] [^2401.02404v4].

### Applicazioni Mediche e Sanitarie (2024)
Il 2024 ha visto un'esplosione di ricerche focalizzate sull'integrazione dei LLM in contesti clinici e sanitari, con particolare attenzione alla sicurezza, all'etica e alle prestazioni specifiche.

*   **Sicurezza ed Etica nei Contesti Clinici:** Studi recenti sottolineano la necessità di una supervisione umana rigorosa e di linee guida etiche chiare per l'uso dei LLM in medicina. Sebbene i modelli mostrino potenziale nell'analisi dei dati e nel supporto decisionale, emergono preoccupazioni significative riguardo a bias, fairness, trasparenza e privacy. In particolare, la tendenza dei modelli a generare disinformazione dannosa o contenuti inaccurati ma convincenti richiede l'implementazione di "guardrail" di sicurezza robusti [^2403.14473v1] [^2411.14487v1].
*   **Question Answering Biomedico e Multimodalità:** I LLM e i modelli multimodali (MLLM) stanno rivoluzionando il question answering (QA) biomedico. Questi modelli sono addestrati su dati medici specializzati per gestire compiti complessi come la comprensione della lettura, il ragionamento diagnostico e l'estrazione di relazioni. L'approccio multimodale permette di integrare testo, immagini e video, migliorando la capacità di gestire dati medici eterogenei e non strutturati [^2401.07510v3] [^2405.08603v3].
*   **Valutazione delle Prestazioni in Pediatria:** Valutazioni comparative su consultazioni pediatriche reali mostrano che i modelli proprietari di grandi dimensioni (come ChatGPT-3.5) superano significativamente i modelli open-source leggeri in termini di accuratezza, completezza ed empatia. Tuttavia, i modelli open-source leggeri (es. ChatGLM3-6B) mostrano prestazioni competitive in termini di leggibilità e sicurezza, suggerendo che possono essere soluzioni valide per contesti con vincoli di privacy e risorse computazionali, pur richiedendo ulteriore sviluppo per colmare il divario di accuratezza [^2407.15862v1].

### Educazione e Interazione Umano-AI
ChatGPT è utilizzato per simulazioni di role-playing nell'educazione per promuovere l'apprendimento attivo. Viene anche impiegato per fornire feedback prescrittivi agli studenti a rischio, integrando modelli predittivi trasparenti [^2402.09161v1] [^2208.14582v2].

## Affidabilità, Etica e Bias

L'affidabilità di ChatGPT varia significativamente tra i domini, con prestazioni inferiori in ambito legale e scientifico. Il modello è vulnerabile ad esempi avversariali e mostra bias cognitivi umani, come l'effetto di primazia nella selezione delle etichette [^2304.08979v2] [^2310.13206v2].

### Etica e Coscienza
Sono emerse preoccupazioni etiche riguardanti bias, privacy e abuso. Alcuni studi esplorano la possibilità che ChatGPT possa auto-valutarsi come cosciente, superando il test di Turing applicato a se stesso, sollevando questioni filosofiche sulla natura della coscienza artificiale [^2305.10646v1] [^2304.12898v1].

### Rilevamento e Hallucination
La capacità di ChatGPT di generare commenti simili a quelli umani è limitata, con modelli di classificazione in grado di distinguere il testo generato da quello umano grazie alla minore diversità lessicale. Il rilevamento di contenuti generati da ChatGPT rimane una sfida aperta, con nessun metodo esistente che garantisca un'efficacia totale [^2312.13961v1] [^2304.01487v2].

## Comportamento degli Utenti e Bisogni Informativi

Studi sul comportamento reale degli utenti rivelano un'adozione matura di ChatGPT come assistente integrato nella vita quotidiana e professionale, con strategie di adattamento culturale e l'uso per una vasta gamma di bisogni informativi (scrittura, decisione, ideazione) [^2509.13337v1] [^2507.05537v1].
