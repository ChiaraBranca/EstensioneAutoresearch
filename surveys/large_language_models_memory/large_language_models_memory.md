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

## Analisi Comparativa
