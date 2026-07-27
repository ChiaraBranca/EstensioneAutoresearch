# Living Survey: large language models memory

## Introduzione

Questo documento raccoglie la letteratura scientifica sul tema **large language models memory**.

## Letteratura Recente

### Debugging e Attribuzione degli Errori nei Sistemi di Memoria
Recenti studi hanno evidenziato come i sistemi di memoria per LLM, sebbene essenziali per il ragionamento a lungo termine, siano spesso inaffidabili e difficili da debuggare. MemTrace introduce un framework che trasforma i pipeline di memoria in grafi di evoluzione eseguibili, permettendo un tracciamento fine-granulare del flusso informativo. L'analisi rivela che i fallimenti di memoria sono sistematici, derivanti da problemi a livello operativo come la perdita di informazioni e il disallineamento nel retrieval. Questo approccio permette non solo di identificare le cause radice, ma anche di ottimizzare i prompt per correggere automaticamente i fault, migliorando le prestazioni finali fino al 7.62% [^2605.28732v3].

### Memoria Parametrica e Valutazione dell'Impatto
La capacità dei LLM di "ricordare" informazioni apprese durante l'addestramento (memoria parametrica) sta emergendo come strumento per metriche di valutazione alternative. LLM-Metrics sfrutta questa memoria per valutare l'impatto della ricerca scientifica, ipotizzando che i paper ad alto impatto siano più presenti nei dati di training e quindi meglio "ricordati" dai modelli. Studi su centinaia di paper hanno mostrato una correlazione significativa tra la capacità di riconoscimento dei modelli e i conteggi di citazione tradizionali, suggerendo che la memoria parametrica può servire come indicatore real-time e cross-disciplinare dell'impatto accademico [^2605.22176v1].

### Ottimizzazione della Cache KV per l'Inferenza
La gestione efficiente della memoria durante l'inferenza è cruciale per la scalabilità dei LLM. Il Key-Value Cache (KVC) rappresenta un collo di bottiglia significativo. FDC propone un sistema di compressione dimensionale rapida che elimina gli overhead di decompressione tipici delle soluzioni precedenti, riducendo il tempo di attenzione. Utilizzando una compressione adattiva basata sul contributo dei diversi heads e layers, FDC bilancia carico di lavoro e accuratezza, dimostrando riduzioni fino al 64% nel tempo di completamento dei job e aumenti di throughput significativi senza compromessi sostanziali sull'accuratezza [^2408.04107v3].

### Ottimizzazione della Cache KV e Compressione
Oltre alle ottimizzazioni di throughput, la compressione della memoria è un'area di ricerca attiva. WKVQuant propone un framework di quantizzazione che affronta sia i pesi che la cache KV, utilizzando una strategia di quantizzazione bidimensionale e una regolarizzazione per la ricostruzione incrociata, ottenendo risparmi di memoria comparabili alla quantizzazione peso-attivazione [^2402.12065v2]. Inoltre, per i dispositivi edge, la compressione della memoria basata su clustering (Clustering-driven Memory Compression) permette di raggruppare memorie simili per ridurre la ridondanza e preservare la coerenza semantica, migliorando la qualità della generazione a parità di budget di contesto [^2601.17443v1].

### Dinamiche di Apprendimento e Memorizzazione
Comprendere come i LLM acquisiscono e trattengono la memoria è fondamentale. Lo studio su come i modelli imparano i fatti rivela tre fasi di apprendimento, con un plateau che coincide con la formazione di circuiti di attenzione, e mostra che le allucinazioni emergono simultaneamente alla conoscenza [^2503.21676v2]. Un'altra prospettiva è quella della "Memoria Mosaico", che suggerisce che i LLM memorizzano assemblando informazioni da sequenze simili (fuzzy duplicates) piuttosto che solo da ripetizioni esatte, sfidando le credenze comuni sulla deduplicazione dei dati [^2405.15523v2]. Inoltre, studi sulla ritenzione della memoria mostrano che i modelli possono riconoscere esempi visti una sola volta con alta accuratezza, ma le memorie precise vengono sovrascritte rapidamente da nuovi esempi, un pattern simile alla ritenzione umana [^2303.17557v1].

### Architetture di Memoria Augmentata e Esterna
L'integrazione di componenti di memoria esterni o aumentati è una strategia chiave per superare i limiti del contesto. TRIME introduce un metodo di addestramento che utilizza esempi del batch come memoria accessibile, migliorando la perplessità senza overhead computazionale significativo [^2205.12674v3]. Larimar utilizza una memoria associativa esterna per gestire contesti molto più lunghi di quelli visti durante l'addestramento, permettendo un rapido accesso a episodi di testo [^2407.01437v2]. Il Memory Decoder è un componente plug-and-play che imita il comportamento di un retriever esterno, permettendo l'adattamento a domini specifici senza modificare i parametri del modello base [^2508.09874v2].

### Memoria di Lavoro e Ragionamento Latente
La memoria di lavoro (Working Memory) è cruciale per il ragionamento complesso. RiM (Reasoning in Memory) sostituisce la generazione autoregressiva di passaggi di ragionamento con blocchi di memoria fissi, permettendo un ragionamento latente efficiente in un singolo forward pass [^2605.30343v1]. Un approccio simile per gli agenti LLM propone un Working Memory Hub centralizzato e un Episodic Buffer per mantenere la continuità tra le interazioni, migliorando il ragionamento contestuale [^2312.17259v2].

### Memoria Episodica e Personalizzata
La memoria episodica e personalizzata permette ai LLM di adattarsi agli utenti specifici. POEM (Prompting with Episodic Memory) utilizza la memoria episodica per archiviare e recuperare sequenze di esempi ottimizzati per il few-shot learning, migliorando le prestazioni nella classificazione del testo [^2408.07465v1]. Un framework per assistenti personalizzati propone una memoria condizionale evolutiva che registra le preferenze dell'utente dalle conversazioni passate per generare risposte su misura [^2312.17257v2].

### Memoria a Lungo Termine e Integrità
Per le conversazioni lunghe, la memoria a lungo termine è essenziale. Il metodo di riassunzione ricorsiva permette ai LLM di generare memorie consistenti nel tempo, integrandosi con modelli a lungo contesto o RAG [^2308.15022v4]. MemGuard affronta il problema della contaminazione della memoria eterogenea, assegnando ruoli funzionali espliciti alle memorie per prevenire il recupero di informazioni incompatibili, migliorando l'affidabilità del ragionamento a lungo termine [^2605.28009v1].

### Memoria Associativa e In-Context Learning
L'apprendimento in-context (ICL) può essere visto come un recupero da una memoria associativa interna. Uno studio teorico basato sulle Reti di Hopfield mostra come gli esempi in-context influenzino le prestazioni di ICL, proponendo strategie attive per la selezione degli esempi [^2311.03498v2]. Inoltre, l'uso di token di memoria speciali permette di generare embedding di frasi reversibili, consentendo la ricostruzione esatta del testo originale, una capacità promettente per il retrieval basato su memoria [^2506.15001v1].

### Prospettive Teoriche e Computazionali
La memoria nei LLM ha implicazioni teoriche profonde. L'aggiunta di una memoria di lettura/scrittura esterna rende i transformer computazionalmente universali, capaci di simulare una macchina di Turing [^2301.04589v1]. La memoria dei LLM mostra somiglianze sorprendenti con la memoria umana, suggerendo che le caratteristiche biologiche lascino un'impronta sulle narrazioni testuali [^2311.03839v3]. Un'altra teoria propone che la memoria dei LLM operi come la "memoria di Schrödinger", diventando osservabile solo quando viene interrogata [^2409.10482v3]. Infine, la memoria parametrica è collegata alla coscienza emergente attraverso la teoria della ecfori sinergica di Tulving [^2401.02509v2].

### Memoria Multi-Agente
In scenari multi-agente, la condivisione della memoria è cruciale. INMS (Interactive Memory Sharing) stabilisce un pool di memoria conversazionale condiviso tra agenti, permettendo uno scambio dinamico di conoscenze e un miglioramento collettivo delle prestazioni [^2404.09982v3].

## Analisi Comparativa
