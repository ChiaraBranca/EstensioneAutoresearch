# Living Survey: cybersecurity

## Introduzione

Questo documento raccoglie la letteratura scientifica sul tema **cybersecurity**.

## Intelligenza Artificiale e Automazione nella Difesa

L'adozione dell'Intelligenza Artificiale (AI) e dei Large Language Models (LLM) sta trasformando radicalmente il panorama della cybersecurity, offrendo sia opportunità difensive che rischi offensivi. Hephaestus propone un "Cybersecurity AI Scientist", un sistema multi-agente modulare che automatizza la ricerca scientifica nel dominio della sicurezza, affrontando la natura non stazionaria degli eventi di sicurezza e richiedendo valutazioni basate su digital twin e cyber range piuttosto che su benchmark statici [^2606.29981v1]. Parallelamente, l'uso di LLM per la generazione di malware è cresciuto esponenzialmente, rappresentando una minaccia significativa che richiede framework di difesa next-generation, come evidenziato da una survey recente che analizza i rischi dual-use dell'AI generativa [^2607.06963v1].

L'automazione si estende anche all'individuazione delle intrusioni (IDS). Un framework AutoML autonomo è stato proposto per le reti 5G/6G, automatizzando la pre-elaborazione dei dati, la selezione delle feature e l'ensemble di modelli per raggiungere una cybersecurity autonoma, superando i limiti dei sistemi tradizionali che richiedono intervento umano [^2409.03141v1]. Inoltre, l'inferenza guidata dalla coerenza (CDI) sta emergendo come strumento promettente per la cybersecurity [^2509.18520v1].

L'uso del Machine Learning (ML) nella cybersecurity è sempre più centrale, sebbene persista un divario tra ricerca e pratica industriale. Uno studio sistematico evidenzia come il ML possa superare i metodi umani nella rilevazione delle minacce, ma sottolinea problemi intrinseci come la necessità di dati di alta qualità e la difficoltà di deployment in ambienti reali [^2206.09707v1]. Per affrontare la scarsità di dati per malware zero-day, è stato proposto un autoencoder denoising Siamese basato su relazioni semantiche, che utilizza immagini di entropia per estrarre informazioni strutturali robuste anche in presenza di offuscamento [^2411.14029v1].

L'AI generativa presenta sfide specifiche. AdaPhish introduce una piattaforma basata su LLM e database vettoriali per l'anonimizzazione e l'analisi in tempo reale delle email di phishing, abilitando un'educazione cybersecurity adattiva e scalabile [^2502.03622v2]. Inoltre, l'uso dell'AI per la sicurezza robotica sta emergendo con approcci offensivi automatizzati che combinano teoria dei giochi e machine learning per identificare vulnerabilità e sviluppare difese autonome per i robot [^2506.15343v1].

Un'analisi critica delle dieci tappe fondamentali per l'AI nella cybersecurity evidenzia questioni etiche, di privacy e di spiegabilità delle decisioni AI nei centri operativi di sicurezza, oltre alle implicazioni dell'uso dell'AI da parte degli attaccanti [^1912.06817v1].

Recentemente, sono stati sviluppati modelli LLM specifici per il dominio della cybersecurity. SecureBERT, un modello linguistico di dominio specifico, è stato addestrato su un ampio corpus di testo di cybersecurity per catturare le connotazioni del testo in questo dominio, migliorando le prestazioni in compiti di NLP critici come l'intelligence sulle minacce informatiche (CTI) [^2204.02685v3]. Inoltre, RedSage, un modello generalista di cybersecurity, è stato addestrato utilizzando dati di pre-addestramento continui focalizzati sulla cybersecurity e un pipeline di augmentation agentic, raggiungendo risultati superiori sui benchmark di cybersecurity rispetto ai modelli baseline [^2601.04940v1]. Per valutare le capacità degli agenti AI in cybersecurity, è stato introdotto CAIBench, un meta-benchmark modulare che valuta le capacità offensive e difensive degli LLM, rivelando un divario significativo tra la conoscenza concettuale e la capacità adattiva in scenari multi-step [^2510.24317v1].

Un nuovo benchmark, SECURE (Security Extraction, Understanding & Reasoning Evaluation), è stato proposto per valutare le prestazioni dei LLM in scenari realistici di cybersecurity, in particolare nel settore dei sistemi di controllo industriale (ICS). Lo studio evidenzia come i benchmark generali non siano sufficienti per catturare le competenze pratiche e applicate necessarie in contesti specifici, mostrando punti di forza e debolezza nei modelli attuali [^2405.20441v4].

L'uso di tecniche avanzate di analisi dei dati, come l'Analisi Topologica dei Dati (TDA), sta guadagnando attenzione per rilevare attività malevole combinando indicatori deboli, sfruttando la struttura ad alto livello dei dati [^2202.08037v1]. Inoltre, l'Intelligenza Artificiale Spiegabile (XAI) sta emergendo come campo cruciale per comprendere il comportamento delle minacce cyber e progettare difese più efficaci, affrontando la natura "black-box" dei modelli AI [^2303.12942v2]. Infine, la valutazione dinamica del rischio per gli agenti di cybersecurity offensivi sta diventando essenziale, poiché gli avversari possono migliorare le capacità degli agenti in modo iterativo, richiedendo valutazioni che tengano conto della libertà d'azione dell'avversario in ambienti stateful e non-stateful [^2505.18384v5].

## Minacce Quantistiche e Crittografia Post-Quantum

La minaccia rappresentata dal computing quantistico alla crittografia classica sta spingendo le organizzazioni verso la preparazione per la cybersecurity post-quantum. Uno studio evidenzia come la maggior parte delle imprese sia insufficientemente preparata, sottovalutando il rischio "harvest now, decrypt later" [^2509.01731v1]. Una review sistematica conferma che mentre il computing quantistico offre vantaggi per la sicurezza, presenta anche minacce impreviste, sottolineando la necessità di una transizione graduale [^2207.03534v1].

Un'analisi recente delle direzioni di ricerca nella cybersecurity quantistica alla fine del primo decennio del secolo evidenzia le principali aree di lavoro accademico, i trend attuali e i gap di ricerca che richiedono finanziamenti futuri [^2512.23607v1].

L'applicazione del quantum computing alla cybersecurity include anche l'addestramento di modelli di machine learning. È stato dimostrato che una Restricted Boltzmann Machine (RBM) addestrata su annealer quantistici (D-Wave) può essere utilizzata per classificare dati di cybersecurity (dataset ISCX), mostrando la fattibilità di migrare problemi pratici di classificazione verso tecniche quantistiche [^2011.13996v4].

## Sicurezza in Settori Critici e Specifici

La cybersecurity deve essere adattata ai contesti specifici delle infrastrutture critiche. Nel settore marittimo, la modernizzazione delle navi e dei porti ha introdotto vulnerabilità specifiche che sono state analizzate per identificare i punti deboli unici dell'industria della shipping [^2208.03607v1]. Nel settore energetico, la convergenza tra cybersecurity e functional safety è cruciale per i veicoli elettrici intelligenti (SEVs), dove un incidente di sicurezza può portare a fallimenti catastrofici della sicurezza funzionale [^2511.07713v1].

Anche le infrastrutture di rete elettrica sono vulnerabili. CritBench introduce un framework per valutare le capacità di cybersecurity dei LLM in ambienti di sottostazioni digitali IEC 61850, rivelando che mentre i modelli hanno conoscenza teorica, faticano nel ragionamento sequenziale dinamico senza tool scaffold specifici [^2604.06019v1]. Nel settore sanitario, le pompe per infusione IoMT presentano vulnerabilità a livello di dispositivo e di rete, richiedendo strategie di sicurezza proattive per proteggere i pazienti [^2509.14604v1].

Il settore automobilistico sta affrontando sfide simili con l'adozione di veicoli autonomi. La compliance con normative come UNR155 e UNR156 richiede sistemi di gestione della sicurezza robusti e continui aggiornamenti per contrastare le minacce emergenti legate alla connettività e all'AI [^2504.20180v1] [^2407.00483v1].

Anche l'agricoltura e il settore alimentare sono vulnerabili. Un'iniziativa educativa propone un corso modulare per formare la forza lavoro agricola alla cybersecurity, un settore storicamente trascurato ma sempre più integrato con tecnologie digitali [^2503.16292v1]. Una review degli incidenti di cybersecurity nel settore alimentare e agricolo evidenzia un aumento della frequenza delle minacce e propone il framework Farmer-Centered AI (FCAI) per supportare i agricoltori nelle decisioni di produzione incorporando l'assicurazione AI [^2403.08036v1].

Nel settore sanitario, la proliferazione di soluzioni IT ha aumentato gli incidenti di cybersecurity. Una systematizzazione di 49 documenti normativi e standard chiave, basata sul framework NIST, aiuta gli operatori a implementare misure di sicurezza efficaci [^2304.14955v1]. Inoltre, la compliance con le normative UE per i dispositivi medici richiede una rigorosa aderenza ai requisiti di cybersecurity, con quattro concetti fondamentali che formano la base per la conformità [^2103.06809v1].

Un framework guidato dai valori per l'innovazione nella cybersecurity è stato proposto per il settore dei trasporti e delle infrastrutture, spostando il focus dall'appeal di mercato al valore strategico e agli obiettivi aziendali. Questo approccio mira a integrare la cybersecurity come abilitatore di business piuttosto che come onere, migliorando l'efficacia operativa e l'allineamento con gli obiettivi critici [^2405.07358v1].

Il settore dell'aviazione affronta vulnerabilità significative sia fisiche che cyber. Uno studio applica la matrice MITRE ATT&CK ai rischi di sicurezza aeroportuale per la prima volta, mappando le tattiche e le tecniche degli attaccanti e proponendo modelli di difesa moderni come l'architettura Zero Trust e la gestione del rischio della catena di approvvigionamento [^2604.23545v1].

## Governance, Norme e Consapevolezza

La cybersecurity non è solo tecnica, ma anche umana e normativa. Un approccio di "salute pubblica" alla cybersecurity propone un sistema nazionale coordinato per la raccolta dati e la risposta agli incidenti, affrontando i fallimenti del mercato dovuti alla natura di bene pubblico della sicurezza [^2602.13869v1]. Per le micro-imprese, un modello di governance proporzionato sotto la direttiva NIS2 enfatizza la consapevolezza come leva principale per la resilienza cyber [^2511.02898v2].

La formazione e la consapevolezza sono fondamentali. Un framework di classificazione per le PMI aiuta a personalizzare gli interventi di competenza e consapevolezza cybersecurity in base alle caratteristiche specifiche dell'azienda [^2110.05370v1]. Gli esercizi Capture the Flag (CTF) possono essere analizzati tramite process mining per migliorare l'analisi post-allenamento e l'engagement dei partecipanti [^2509.15589v2]. Inoltre, la gestione dei patch è un'area critica dove fattori umani e organizzativi influenzano la decisione di applicare o meno gli aggiornamenti di sicurezza [^2502.17703v1].

Studi comportamentali mostrano che la formazione sul lavoro può ridurre l'intenzione di condividere informazioni di sicurezza a casa, spostando il focus verso l'ambiente lavorativo [^2602.19695v1]. L'integrazione di concetti di cybersecurity nei curricula universitari ha dimostrato di migliorare significativamente la conoscenza e la consapevolezza degli studenti [^2209.10407v1].

La valutazione della maturità della cybersecurity è cruciale per le PMI. Un approccio integrato da standard industriali aiuta le piccole imprese a migliorare le loro capacità di sicurezza in modo sostenibile [^2007.01751v1].

Un approccio multidimensionale alla cybersecurity per la foresight strategica è stato proposto, comprendendo domini come Fisico, Culturale, Economico, Sociale, Politico e Cyber, con principi guida che includono i fattori BOTH (Business, Operational, Technological, Human) [^2202.02537v1]. La regolamentazione della cybersecurity nell'UE, in particolare l'Cybersecurity Resilience Act, dovrebbe basarsi su principi chiari e hard legal rules, regolando il ciclo di vita dei sistemi e promuovendo un modello di zero-trust [^2205.13196v1].

L'analisi dei requisiti per le PMI è complessa. Uno studio propone di elicitarli studiando l'adesione alle raccomandazioni degli esperti, utilizzando lo strumento CYSEC per scalare l'elicitation a un gran numero di PMI [^2007.08177v1]. Un framework transdisciplinare per la cybersecurity incoraggia il pensiero transdisciplinare attraverso un approccio Think, Plan, Do, aiutando gli esperti a superare i confini disciplinari tradizionali [^2405.10373v1].

L'educazione e la formazione nella cybersecurity richiedono approcci innovativi. Una review completa dei metodi di training evidenzia strategie tradizionali, basate sulla tecnologia e innovative, inclusi AI e realtà estesa [^2401.11326v1]. Gli esercizi di cybersecurity possono essere generati automaticamente per modellare sistemi IT enterprise, rilasciando un dataset di 100.000 scenari [^2604.01079v1]. L'uso di giochi seri (serious games) per l'educazione alla cybersecurity è efficace ma presenta sfide nella valutazione degli effetti a lungo termine [^2307.09401v1]. Un approccio basato su carte da gioco, fondato sul CyBOK, fornisce conoscenze introduttive e facilita la discussione tra principianti [^2307.16535v1].

La valutazione delle competenze e dei requisiti di carriera nella cybersecurity è un'area di studio attiva. Una review della letteratura identifica le competenze necessarie per i professionisti, evidenziando la necessità di investimento nel tempo e le barriere di genere [^2306.09599v1]. Un corso interdisciplinare per lo sviluppo della forza lavoro combina cybersecurity e interaction design per l'apprendimento esperienziale [^1806.01198v1]. Invece, un sondaggio nell'Inner Scandinavia rivela lacune nelle competenze organizzative e la necessità di formazione specifica [^2510.09673v1].

L'ecosistema della cybersecurity in Asia Sud-Est è valutato tramite indici di prospettive educative e industriali, sottolineando l'importanza di un ecosistema sano dove l'educazione supporta l'industria [^2308.06963v1]. La cybersecurity in politica è un campo complesso che interseca tecnologia, governance e relazioni internazionali, richiedendo strategie agili per proteggere l'integrità dei sistemi politici [^2308.08005v1].

L'analisi del rischio adversarial è essenziale per la cybersecurity. Un framework proposto copre sia minacce adversarial che non intenzionali, includendo l'uso di assicurazione nel portafoglio di sicurezza [^1903.07727v1]. L'approccio comportamentale alla cybersecurity evidenzia come i fattori umani siano la principale vulnerabilità, richiedendo un miglioramento dei comportamenti degli utenti e delle organizzazioni [^2303.13621v1].

La valutazione delle competenze e la creazione di inventari concettuali per la cybersecurity sono sfide complesse. Un progetto CATS ha creato inventari concettuali per misurare l'efficacia dell'insegnamento, evidenziando le difficoltà nella costruzione di domande a scelta multipla per problemi cybersecurity sottili [^2004.05248v1].

Per comprendere le percezioni dei genitori riguardo alla cybersecurity dei bambini, uno studio qualitativo in Norvegia ha identificato le esigenze di consapevolezza, le risorse di apprendimento e le sfide affrontate dai genitori, fornendo indicazioni per sviluppatori ed educatori per creare soluzioni più efficaci [^2108.02512v1].

Un framework basato su LLM, CurricuLLM, è stato sviluppato per automatizzare la classificazione dei contenuti dei curricula di cybersecurity in aree di conoscenza standardizzate, offrendo una soluzione efficiente per l'analisi dei programmi educativi [^2601.04940v1].

Uno studio di caso nel Regno Unito ha analizzato come l'accreditamento nazionale influenzi l'insegnamento della cybersecurity nei corsi di informatica generale, dimostrando che i requisiti di accreditamento possono migliorare significativamente la qualità e la rilevanza dell'educazione [^1906.09584v2].

Un'analisi del sentiment sui contenuti di cybersecurity su Twitter e Reddit ha rivelato che la maggior parte dei contenuti è positiva o neutrale, con VADER che ha mostrato una buona accuratezza nel classificare il sentiment rispetto agli annotatori umani, suggerendo l'uso di questi strumenti per monitorare la percezione pubblica [^2204.12267v1].

Un'analisi delle soluzioni CTF ha mappato le competenze tecniche insegnate (come crittografia e sicurezza di rete) rispetto ai curricula formali, evidenziando la mancanza di focus sugli aspetti umani come l'ingegneria sociale e la consapevolezza, suggerendo l'integrazione di questi temi per attrarre un pubblico più ampio [^2101.01421v1].

Uno studio sulla Virginia ha sviluppato un modello di maturità per valutare l'educazione alla cybersecurity nelle università, mostrando un aumento delle offerte formative dopo l'inizio del Commonwealth Cyber Initiative, con potenziali impatti sulla riduzione del gap di competenze [^2502.18456v1].

## Difesa Collaborativa e Architetture

La collaborazione tra entità è essenziale per una difesa efficace. Le sharing communities possono abilitare il Federated Learning per la cybersecurity, permettendo l'addestramento incrementale dei modelli contro il concept drift senza condividere dati sensibili [^2104.11763v2]. Per le infrastrutture critiche, il concetto di "antifragilità" è proposto come evoluzione della resilienza, dove i sistemi non solo resistono ma migliorano sotto stress, basato su un modello empirico di sistemi resilienti [^2607.29550v1].

Infine, la sicurezza delle catene di approvvigionamento spaziali della NATO è un'area critica, con vulnerabilità legate a sistemi legacy e tecnologia COTS, che richiedono maggiore regolamentazione e consapevolezza lungo la supply chain [^2102.09674v1]. Per i dispositivi IoT a basso consumo, un'architettura dinamica per il monitoraggio della sicurezza (NSM) ha dimostrato di ridurre significativamente i costi energetici e di installazione, promuovendo un IoT green [^2106.00834v4].

## Cloud Computing e Servizi di Sicurezza

La migrazione al cloud computing introduce nuove sfide di sicurezza. Un approccio ontologico alla cybersecurity nel cloud aiuta a identificare le informazioni di sicurezza operative necessarie, evidenziando cambiamenti come la decoupling dei dati e la necessità di tracciare la provenienza dei dati [^1405.6169v1]. Un riesame dei concetti core di cybersecurity alla luce di AWS cloud evidenzia come i concetti tradizionali debbano essere adattati al contesto cloud [^2003.12905v1].

Per le organizzazioni che non possono permettersi personale di sicurezza interno, il Cybersecurity as a Service (CSaaS) emerge come soluzione per outsourcing delle funzioni di sicurezza verso provider gestiti (MSSP), offrendo una guida per le PMI nella selezione di questi provider [^2402.13965v1].

## Etica e Sostenibilità nella Cybersecurity

L'etica nella cybersecurity è un campo in crescita. Un lavoro mappa le preoccupazioni etiche del Cyber Security Body of Knowledge (CyBOK) su dilemmi pratici emersi da interviste con esperti, evidenziando la necessità di bilanciare aspetti tecnici, oggettivi e soggettivi nelle decisioni di sicurezza [^2311.10165v1]. Una guida per i ricercatori di cybersecurity fornisce supporto pratico per l'analisi degli stakeholder, enumerando i tipi di stakeholder e mappandoli ai metodi di ricerca empirica per soddisfare i mandati etici [^2508.14796v1].

La cybersecurity è anche legata allo sviluppo sostenibile. Nel settore dei beni e servizi ambientali (EGSS), la "Green Cybersecurity" diventa cruciale per proteggere i processi di gestione ambientale, contribuendo agli obiettivi di sviluppo sostenibile dell'UE [^2105.13652v1].

## Approcci Sistematici e Bio-Ispirati

La complessità della cybersecurity richiede approcci sistemici. Un framework di "Cybersecurity Dynamics" propone una visione olistica per modellare e analizzare l'evoluzione dello stato globale della sicurezza nello spazio cibernetico, considerando le interazioni attacco-difesa [^2010.05683v1] [^1502.05100v1]. Un approccio di "Systems Thinking" offre teorie e metodi per comprendere le interazioni tra fattori di impatto e strutture nel cyberspazio [^2001.05734v1].

Ispirandosi alla natura, un framework di "Cybersecurity Ecology" propone di mappare i sistemi di sicurezza biologici ai loro analoghi cibernetici, per sviluppare sistemi di sicurezza di nuova generazione bio-ispirati [^1505.04207v2]. Si argomenta che il comportamento emergente è intrinseco alla cybersecurity, richiedendo una comprensione delle dinamiche complesse [^1502.05102v1].

## Tecnologie Avanzate: Graph Mining e Social Engineering

Le tecniche di Graph Mining stanno guadagnando importanza per catturare le correlazioni tra entità cyber, superando i limiti dei metodi ML tradizionali. Una survey completa analizza le tecniche di graph mining per vari task di cybersecurity, raccogliendo dataset e toolkit open source [^2304.00485v2].

Il social engineering rimane una minaccia critica. Una domain ontology e un knowledge graph per il social engineering permettono di analizzare scenari di attacco, identificare le vulnerabilità umane più sfruttate e trovare potenziali percorsi di attacco [^2106.01157v1].

## Bug Bounty e Crowdsourcing

I programmi di bug bounty offrono una piattaforma per il crowdsourcing della sicurezza software. Uno studio analizza le dinamiche economiche e tecniche di questi programmi, evidenziando come i ricercatori siano incentivati a passare a nuovi programmi per trovare vulnerabilità "facili", mentre i manager cercano di massimizzare la diversità delle competenze [^1608.03445v2].

## Smart Home e IoT

La sicurezza delle smart home è un'area critica. Una review delle linee guida governative per gli utenti di smart home mostra che, sebbene ci sia abbondanza di consigli preventivi, manca una guida strutturata per la risposta agli incidenti e il recupero per gli utenti non esperti [^2603.21703v1].

Per migliorare la trasparenza e la tracciabilità delle certificazioni di cybersecurity per i dispositivi IoT, è stata proposta una piattaforma basata su blockchain, in linea con l'Atto sulla Cybersecurity dell'UE, per facilitare lo scambio fidato di informazioni di certificazione [^1909.07039v1].

## Smart Cities e Blockchain

La cybersecurity è fondamentale per il deployment su larga scala delle applicazioni delle smart city. Blockchain emerge come tecnologia promettente per fornire sicurezza in vari domini delle smart city, come sanità, trasporti, agricoltura e supply chain, con una mappatura delle soluzioni esistenti ai requisiti di sicurezza [^2206.02760v1].

## Costi e Governance

La gestione dei costi della cybersecurity è un aspetto spesso trascurato. Un mapping basato sui costi della qualità e sul NIST CSF aiuta le organizzazioni a pianificare e gestire i costi associati alla gestione del rischio di cybersecurity [^1707.02653v1].

## Survey Generali

Una panoramica completa della cybersecurity, dal passato al futuro, copre specializzazioni come la sicurezza software, hardware, malware, biometria, intelligence e forensics, sottolineando il ruolo dell'AI spiegabile e della collaborazione uomo-AI [^2207.01227v3].
