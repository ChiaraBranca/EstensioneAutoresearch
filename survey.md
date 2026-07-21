# Survey sui Framework di Memoria per Agenti LLM ## Metodi Recenti

Un approccio innovativo per la gestione della memoria negli agenti LLM multi-turno è **HyMCache** [1], un framework che integra memoria ibrida CXL (CXL-Hybrid Memory) per il caching dei token KV. HyMCache sfrutta la natura *read-dominant* e *append-only* dell'accesso ai cache KV per ottimizzare l'uso di una piccola quantità di DRAM locale combinata con una grande capacità basata su SSD accessibile via CXL. Questo permette di scalare a capacità TB-scale per il contesto condiviso, riducendo i costi mantenendo un'efficienza vicina alla DRAM.

## Confronto dei Framework

| Framework | Tipo di Memoria | Scalabilità | Latenza | Note |
| :--- | :--- | :--- | :--- | :--- |
| HyMCache | Ibrida (DRAM + CXL) | Alta (TB-scale) | Bassa | Ottimizzato per caching KV |
| MemGPT | Gerarchica (RAM + Disk) | Media | Media | Simula memoria infinita |
| LangChain Memory | Variabile | Bassa | Bassa | Dipende dall'implementazione |
