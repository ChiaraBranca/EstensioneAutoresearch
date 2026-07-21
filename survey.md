# Survey sui Framework di Memoria per Agenti LLM ## Metodi Recenti

Un approccio innovativo per la gestione della memoria negli agenti LLM multi-turno è **HyMCache** [1], un framework che integra memoria ibrida CXL (CXL-Hybrid Memory) per il caching dei token KV. HyMCache sfrutta la natura *read-dominant* e *append-only* dell'accesso ai cache KV per ottimizzare l'uso di una piccola quantità di DRAM locale combinata con una grande capacità basata su SSD accessibile via CXL. Questo permette di scalare a capacità TB-scale per il contesto condiviso, riducendo i costi mantenendo un'efficienza vicina alla DRAM.

## Architetture di Memoria

La gestione della memoria negli agenti LLM si basa generalmente su tre livelli principali:

1.  **Memoria a Breve Termine (Short-Term Memory)**: Corrisponde al contesto immediato dell'LLM (la finestra di attenzione). È limitata dalla lunghezza massima dei token supportati dal modello.
2.  **Memoria a Lungo Termine (Long-Term Memory)**: Utilizza database vettoriali (Vector Databases) o grafi della conoscenza (Knowledge Graphs) per memorizzare informazioni storiche che possono essere recuperate tramite retrieval (RAG - Retrieval Augmented Generation).
3.  **Memoria Procedurale (Procedural Memory)**: Memorizza le regole, i tool disponibili e le istruzioni su come eseguire compiti specifici, spesso definiti staticamente o appresi attraverso l'esperienza.

## Valutazione delle Prestazioni

Per confrontare l'efficacia dei diversi framework di memoria, si utilizzano metriche come:

*   **Recall**: La capacità del sistema di recuperare le informazioni corrette quando richieste.
*   **Precision**: La pertinenza delle informazioni recuperate rispetto alla query dell'utente.
*   **Overhead di Latenza**: Il tempo aggiuntivo introdotto dal processo di retrieval rispetto a una risposta diretta.
*   **Costo Computazionale**: Il consumo di risorse (CPU/GPU/RAM) necessario per mantenere e aggiornare la memoria.

## Confronto dei Framework

| Framework | Tipo di Memoria | Scalabilità | Latenza | Note |
| :--- | :--- | :--- | :--- | :--- |
| HyMCache | Ibrida (DRAM + CXL) | Alta (TB-scale) | Bassa | Ottimizzato per caching KV |
| MemGPT | Gerarchica (RAM + Disk) | Media | Media | Simula memoria infinita |
| LangChain Memory | Variabile | Bassa | Bassa | Dipende dall'implementazione |
| Zep | Vector DB + Graph | Alta | Media | Focus su dati strutturati |
| AutoGPT | Episodica | Bassa | Alta | Memoria basata su episodi |
