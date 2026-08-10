# Living Survey: cybersecurity

## Introduzione

Questo documento raccoglie la letteratura scientifica sul tema **cybersecurity**.

## Intelligenza Artificiale e Automazione nella Difesa

L'adozione dell'Intelligenza Artificiale (AI) e dei Large Language Models (LLM) sta trasformando radicalmente il panorama della cybersecurity, offrendo sia opportunità difensive che rischi offensivi. Hephaestus propone un "Cybersecurity AI Scientist", un sistema multi-agente modulare che automatizza la ricerca scientifica nel dominio della sicurezza, affrontando la natura non stazionaria degli eventi di sicurezza e richiedendo valutazioni basate su digital twin e cyber range piuttosto che su benchmark statici [^2606.29981v1]. Parallelamente, l'uso di LLM per la generazione di malware è cresciuto esponenzialmente, rappresentando una minaccia significativa che richiede framework di difesa next-generation, come evidenziato da una survey recente che analizza i rischi dual-use dell'AI generativa [^2607.06963v1].

L'automazione si estende anche all'individuazione delle intrusioni (IDS). Un framework AutoML autonomo è stato proposto per le reti 5G/6G, automatizzando la pre-elaborazione dei dati, la selezione delle feature e l'ensemble di modelli per raggiungere una cybersecurity autonoma, superando i limiti dei sistemi tradizionali che richiedono intervento umano [^2409.03141v1]. Inoltre, l'inferenza guidata dalla coerenza (CDI) tramite LLM sta emergendo come strumento promettente per le operazioni di red/blue teaming, permettendo di compilare grafi ponderati su dati in linguaggio naturale per supportare il decision-making [^2509.18520v1].

## Minacce Quantistiche e Crittografia Post-Quantum

La minaccia rappresentata dal computing quantistico alla crittografia classica sta spingendo le organizzazioni verso la preparazione per la cybersecurity post-quantum. Uno studio evidenzia come la maggior parte delle imprese sia insufficientemente preparata, con meno del 5% che dispone di piani formali di transizione, sottovalutando il rischio "harvest now, decrypt later" [^2509.01731v1]. Una review sistematica conferma che mentre il computing quantistico offre vantaggi per la sicurezza, presenta anche minacce impreviste, sottolineando la necessità di una transizione graduale [^2207.03534v1].

L'applicazione del quantum computing alla cybersecurity include anche l'addestramento di modelli di machine learning. È stato dimostrato che una Restricted Boltzmann Machine (RBM) addestrata su annealer quantistici (D-Wave) può essere utilizzata per classificare dati di cybersecurity (dataset ISCX), mostrando la fattibilità di migrare problemi pratici di classificazione verso tecniche quantistiche [^2011.13996v4].

## Sicurezza in Settori Critici e Specifici

La cybersecurity deve essere adattata ai contesti specifici delle infrastrutture critiche. Nel settore marittimo, la modernizzazione delle navi e dei porti ha introdotto vulnerabilità specifiche che sono state analizzate per identificare i punti deboli unici dell'industria della shipping [^2208.03607v1]. Nel settore energetico, la convergenza tra cybersecurity e functional safety è cruciale per i veicoli elettrici intelligenti (SEVs), dove un incidente di sicurezza può portare a fallimenti catastrofici della sicurezza funzionale [^2511.07713v1].

Anche le infrastrutture di rete elettrica sono vulnerabili. CritBench introduce un framework per valutare le capacità di cybersecurity dei LLM in ambienti di sottostazioni digitali IEC 61850, rivelando che mentre i modelli hanno conoscenza teorica, faticano nel ragionamento sequenziale dinamico senza tool scaffold specifici [^2604.06019v1]. Nel settore sanitario, le pompe per infusione IoMT presentano vulnerabilità a livello di dispositivo e di rete, richiedendo strategie di sicurezza proattive per proteggere i pazienti [^2509.14604v1].

## Governance, Norme e Consapevolezza

La cybersecurity non è solo tecnica, ma anche umana e normativa. Un approccio di "salute pubblica" alla cybersecurity propone un sistema nazionale coordinato per la raccolta dati e la risposta agli incidenti, affrontando i fallimenti del mercato dovuti alla natura di bene pubblico della sicurezza [^2602.13869v1]. Per le micro-imprese, un modello di governance proporzionato sotto la direttiva NIS2 enfatizza la consapevolezza come leva principale per la resilienza cyber [^2511.02898v2].

La formazione e la consapevolezza sono fondamentali. Un framework di classificazione per le PMI aiuta a personalizzare gli interventi di competenza e consapevolezza cybersecurity in base alle caratteristiche specifiche dell'azienda [^2110.05370v1]. Gli esercizi Capture the Flag (CTF) possono essere analizzati tramite process mining per migliorare l'analisi post-allenamento e l'engagement dei partecipanti [^2509.15589v2]. Inoltre, la gestione dei patch è un'area critica dove fattori umani e organizzativi influenzano la decisione di applicare o meno gli aggiornamenti di sicurezza [^2502.17703v1].

## Difesa Collaborativa e Architetture

La collaborazione tra entità è essenziale per una difesa efficace. Le sharing communities possono abilitare il Federated Learning per la cybersecurity, permettendo l'addestramento incrementale dei modelli contro il concept drift senza condividere dati sensibili [^2104.11763v2]. Per le infrastrutture critiche, il concetto di "antifragilità" è proposto come evoluzione della resilienza, dove i sistemi non solo resistono ma migliorano sotto stress, basato su un modello empirico di sistemi resilienti [^2607.29550v1].

Infine, la sicurezza delle catene di approvvigionamento spaziali della NATO è un'area critica, con vulnerabilità legate a sistemi legacy e tecnologia COTS, che richiedono maggiore regolamentazione e consapevolezza lungo la supply chain [^2102.09674v1]. Per i dispositivi IoT a basso consumo, un'architettura dinamica per il monitoraggio della sicurezza (NSM) ha dimostrato di ridurre significativamente i costi energetici e di installazione, promuovendo un IoT green [^2106.00834v4].
