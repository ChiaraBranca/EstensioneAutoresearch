# Living Survey: cybersecurity

## Introduzione

Questo documento raccoglie la letteratura scientifica sul tema **cybersecurity**.

## Intelligenza Artificiale e Automazione nella Difesa

L'adozione dell'Intelligenza Artificiale (AI) e dei Large Language Models (LLM) sta trasformando radicalmente il panorama della cybersecurity, offrendo sia opportunità difensive che rischi offensivi. Hephaestus propone un "Cybersecurity AI Scientist", un sistema multi-agente modulare che automatizza la ricerca scientifica nel dominio della sicurezza, affrontando la natura non stazionaria degli eventi di sicurezza e richiedendo valutazioni basate su digital twin e cyber range piuttosto che su benchmark statici [^2606.29981v1]. Parallelamente, l'uso di LLM per la generazione di malware è cresciuto esponenzialmente, rappresentando una minaccia significativa che richiede framework di difesa next-generation, come evidenziato da una survey recente che analizza i rischi dual-use dell'AI generativa [^2607.06963v1].

L'automazione si estende anche all'individuazione delle intrusioni (IDS). Un framework AutoML autonomo è stato proposto per le reti 5G/6G, automatizzando la pre-elaborazione dei dati, la selezione delle feature e l'ensemble di modelli per raggiungere una cybersecurity autonoma, superando i limiti dei sistemi tradizionali che richiedono intervento umano [^2409.03141v1]. Inoltre, l'inferenza guidata dalla coerenza (CDI) sta emergendo come strumento promettente per la cybersecurity [^2509.18520v1].

L'uso del Machine Learning (ML) nella cybersecurity è sempre più centrale, sebbene persista un divario tra ricerca e pratica industriale. Uno studio sistematico evidenzia come il ML possa superare i metodi umani nella rilevazione delle minacce, ma sottolinea problemi intrinseci come la necessità di dati di alta qualità e la difficoltà di deployment in ambienti reali [^2206.09707v1]. Per affrontare la scarsità di dati per malware zero-day, è stato proposto un autoencoder denoising Siamese basato su relazioni semantiche, che utilizza immagini di entropia per estrarre informazioni strutturali robuste anche in presenza di offuscamento [^2411.14029v1].

L'AI generativa presenta sfide specifiche. AdaPhish introduce una piattaforma basata su LLM e database vettoriali per l'anonimizzazione e l'analisi in tempo reale delle email di phishing, abilitando un'educazione cybersecurity adattiva e scalabile [^2502.03622v2]. Inoltre, l'uso dell'AI per la sicurezza robotica sta emergendo con approcci offensivi automatizzati che combinano teoria dei giochi e machine learning per identificare vulnerabilità e sviluppare difese autonome per i robot [^2506.15343v1].

Un'analisi critica delle dieci tappe fondamentali per l'AI nella cybersecurity evidenzia questioni etiche, di privacy e di spiegabilità delle decisioni AI nei centri operativi di sicurezza, oltre alle implicazioni dell'uso dell'AI da parte degli attaccanti [^1912.06817v1].

## Minacce Quantistiche e Crittografia Post-Quantum

La minaccia rappresentata dal computing quantistico alla crittografia classica sta spingendo le organizzazioni verso la preparazione per la cybersecurity post-quantum. Uno studio evidenzia come la maggior parte delle imprese sia insufficientemente preparata, con meno del 5% che dispone di piani formali di transizione, sottovalutando il rischio "harvest now, decrypt later" [^2509.01731v1]. Una review sistematica conferma che mentre il computing quantistico offre vantaggi per la sicurezza, presenta anche minacce impreviste, sottolineando la necessità di una transizione graduale [^2207.03534v1].

L'applicazione del quantum computing alla cybersecurity include anche l'addestramento di modelli di machine learning. È stato dimostrato che una Restricted Boltzmann Machine (RBM) addestrata su annealer quantistici (D-Wave) può essere utilizzata per classificare dati di cybersecurity (dataset ISCX), mostrando la fattibilità di migrare problemi pratici di classificazione verso tecniche quantistiche [^2011.13996v4].

## Sicurezza in Settori Critici e Specifici

La cybersecurity deve essere adattata ai contesti specifici delle infrastrutture critiche. Nel settore marittimo, la modernizzazione delle navi e dei porti ha introdotto vulnerabilità specifiche che sono state analizzate per identificare i punti deboli unici dell'industria della shipping [^2208.03607v1]. Nel settore energetico, la convergenza tra cybersecurity e functional safety è cruciale per i veicoli elettrici intelligenti (SEVs), dove un incidente di sicurezza può portare a fallimenti catastrofici della sicurezza funzionale [^2511.07713v1].

Anche le infrastrutture di rete elettrica sono vulnerabili. CritBench introduce un framework per valutare le capacità di cybersecurity dei LLM in ambienti di sottostazioni digitali IEC 61850, rivelando che mentre i modelli hanno conoscenza teorica, faticano nel ragionamento sequenziale dinamico senza tool scaffold specifici [^2604.06019v1]. Nel settore sanitario, le pompe per infusione IoMT presentano vulnerabilità a livello di dispositivo e di rete, richiedendo strategie di sicurezza proattive per proteggere i pazienti [^2509.14604v1].

Il settore automobilistico sta affrontando sfide simili con l'adozione di veicoli autonomi. La compliance con normative come UNR155 e UNR156 richiede sistemi di gestione della sicurezza robusti e continui aggiornamenti per contrastare le minacce emergenti legate alla connettività e all'AI [^2504.20180v1] [^2407.00483v1].

Anche l'agricoltura e il settore alimentare sono vulnerabili. Un'iniziativa educativa propone un corso modulare per formare la forza lavoro agricola alla cybersecurity, un settore storicamente trascurato ma sempre più integrato con tecnologie digitali [^2503.16292v1].

## Governance, Norme e Consapevolezza

La cybersecurity non è solo tecnica, ma anche umana e normativa. Un approccio di "salute pubblica" alla cybersecurity propone un sistema nazionale coordinato per la raccolta dati e la risposta agli incidenti, affrontando i fallimenti del mercato dovuti alla natura di bene pubblico della sicurezza [^2602.13869v1]. Per le micro-imprese, un modello di governance proporzionato sotto la direttiva NIS2 enfatizza la consapevolezza come leva principale per la resilienza cyber [^2511.02898v2].

La formazione e la consapevolezza sono fondamentali. Un framework di classificazione per le PMI aiuta a personalizzare gli interventi di competenza e consapevolezza cybersecurity in base alle caratteristiche specifiche dell'azienda [^2110.05370v1]. Gli esercizi Capture the Flag (CTF) possono essere analizzati tramite process mining per migliorare l'analisi post-allenamento e l'engagement dei partecipanti [^2509.15589v2]. Inoltre, la gestione dei patch è un'area critica dove fattori umani e organizzativi influenzano la decisione di applicare o meno gli aggiornamenti di sicurezza [^2502.17703v1].

Studi comportamentali mostrano che la formazione sul lavoro può ridurre l'intenzione di condividere informazioni di sicurezza a casa, spostando il focus verso l'ambiente lavorativo [^2602.19695v1]. L'integrazione di concetti di cybersecurity nei curricula universitari ha dimostrato di migliorare significativamente la conoscenza e la consapevolezza degli studenti [^2209.10407v1].

La valutazione della maturità della cybersecurity è cruciale per le PMI. Un approccio integrato da standard industriali aiuta le piccole imprese a migliorare le loro capacità di sicurezza in modo sostenibile [^2007.01751v1].

## Difesa Collaborativa e Architetture

La collaborazione tra entità è essenziale per una difesa efficace. Le sharing communities possono abilitare il Federated Learning per la cybersecurity, permettendo l'addestramento incrementale dei modelli contro il concept drift senza condividere dati sensibili [^2104.11763v2]. Per le infrastrutture critiche, il concetto di "antifragilità" è proposto come evoluzione della resilienza, dove i sistemi non solo resistono ma migliorano sotto stress, basato su un modello empirico di sistemi resilienti [^2607.29550v1].

Infine, la sicurezza delle catene di approvvigionamento spaziali della NATO è un'area critica, con vulnerabilità legate a sistemi legacy e tecnologia COTS, che richiedono maggiore regolamentazione e consapevolezza lungo la supply chain [^2102.09674v1]. Per i dispositivi IoT a basso consumo, un'architettura dinamica per il monitoraggio della sicurezza (NSM) ha dimostrato di ridurre significativamente i costi energetici e di installazione, promuovendo un IoT green [^2106.00834v4].

## Cloud Computing e Servizi di Sicurezza

La migrazione al cloud computing introduce nuove sfide di sicurezza. Un approccio ontologico alla cybersecurity nel cloud aiuta a identificare le informazioni di sicurezza operative necessarie, evidenziando cambiamenti come la decoupling dei dati e la necessità di tracciare la provenienza dei dati [^1405.6169v1].

Per le organizzazioni che non possono permettersi personale di sicurezza interno, il Cybersecurity as a Service (CSaaS) emerge come soluzione per outsourcing delle funzioni di sicurezza verso provider gestiti (MSSP), offrendo una guida per le PMI nella selezione di questi provider [^2402.13965v1].

## Etica e Sostenibilità nella Cybersecurity

L'etica nella cybersecurity è un campo in crescita. Un lavoro mappa le preoccupazioni etiche del Cyber Security Body of Knowledge (CyBOK) su dilemmi pratici emersi da interviste con esperti, evidenziando la necessità di bilanciare aspetti tecnici, oggettivi e soggettivi nelle decisioni di sicurezza [^2311.10165v1].

La cybersecurity è anche legata allo sviluppo sostenibile. Nel settore dei beni e servizi ambientali (EGSS), la "Green Cybersecurity" diventa cruciale per proteggere i processi di gestione ambientale, contribuendo agli obiettivi di sviluppo sostenibile dell'UE [^2105.13652v1].

## Approcci Sistematici e Bio-Ispirati

La complessità della cybersecurity richiede approcci sistemici. Un framework di "Cybersecurity Dynamics" propone una visione olistica per modellare e analizzare l'evoluzione dello stato globale della sicurezza nello spazio cibernetico, considerando le interazioni attacco-difesa [^2010.05683v1] [^1502.05100v1]. Un approccio di "Systems Thinking" offre teorie e metodi per comprendere le interazioni tra fattori di impatto e strutture nel cyberspazio [^2001.05734v1].

Ispirandosi alla natura, un framework di "Cybersecurity Ecology" propone di mappare i sistemi di sicurezza biologici ai loro analoghi cibernetici, per sviluppare sistemi di sicurezza di nuova generazione bio-ispirati [^1505.04207v2].

## Tecnologie Avanzate: Graph Mining e Social Engineering

Le tecniche di Graph Mining stanno guadagnando importanza per catturare le correlazioni tra entità cyber, superando i limiti dei metodi ML tradizionali. Una survey completa analizza le tecniche di graph mining per vari task di cybersecurity, raccogliendo dataset e toolkit open source [^2304.00485v2].

Il social engineering rimane una minaccia critica. Una domain ontology e un knowledge graph per il social engineering permettono di analizzare scenari di attacco, identificare le vulnerabilità umane più sfruttate e trovare potenziali percorsi di attacco [^2106.01157v1].

## Bug Bounty e Crowdsourcing

I programmi di bug bounty offrono una piattaforma per il crowdsourcing della sicurezza software. Uno studio analizza le dinamiche economiche e tecniche di questi programmi, evidenziando come i ricercatori siano incentivati a passare a nuovi programmi per trovare vulnerabilità "facili", mentre i manager cercano di massimizzare la diversità delle competenze [^1608.03445v2].

## Smart Home e IoT

La sicurezza delle smart home è un'area critica. Una review delle linee guida governative per gli utenti di smart home mostra che, sebbene ci sia abbondanza di consigli preventivi, manca una guida strutturata per la risposta agli incidenti e il recupero per gli utenti non esperti [^2603.21703v1].

## Regolamentazione nel Settore Sanitario

Nel settore sanitario, la proliferazione di soluzioni IT ha aumentato gli incidenti di cybersecurity. Una systematizzazione di 49 documenti normativi e standard chiave, basata sul framework NIST, aiuta gli operatori a implementare misure di sicurezza efficaci [^2304.14955v1].

## Costi e Governance

La gestione dei costi della cybersecurity è un aspetto spesso trascurato. Un mapping basato sui costi della qualità e sul NIST CSF aiuta le organizzazioni a pianificare e gestire i costi associati alla gestione del rischio di cybersecurity [^1707.02653v1].

## Competenze Organizzative

Le organizzazioni nell'Inner Scandinavia mostrano bisogno di migliorare le competenze in cybersecurity. Un sondaggio e interviste con rappresentanti di imprese e settore pubblico rivelano lacune nella preparazione e nella necessità di formazione specifica [^2510.09673v1].

## Survey Generali

Una panoramica completa della cybersecurity, dal passato al futuro, copre specializzazioni come la sicurezza software, hardware, malware, biometria, intelligence e forensics, sottolineando il ruolo dell'AI spiegabile e della collaborazione uomo-AI [^2207.01227v3].
