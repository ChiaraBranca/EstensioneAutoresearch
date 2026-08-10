# Living Survey: diabetes

## Introduzione

Questo documento raccoglie la letteratura scientifica sul tema **diabetes**.

## Intelligenza Artificiale e Predizione del Diabete

L'uso dell'intelligenza artificiale e del machine learning per la predizione e la diagnosi del diabete è un'area di ricerca estremamente attiva. Diversi studi recenti hanno proposto modelli avanzati per migliorare l'accuratezza e l'efficienza.

Il modello *Quantum-Inspired Stacked Integrated Concept Graph Model* (QISICGM) rappresenta un approccio innovativo che combina tecniche ispirate alla quantistica con ensemble di machine learning (Random Forest, Extra Trees, Transformers, CNN e FFNN) per predire il rischio di diabete, superando i metodi tradizionali[^2509.12259v1]. Analogamente, *DiabetesNet* propone una rete neurale a retropropagazione con normalizzazione di batch e bilanciamento dei dati, affrontando le sfide dei dati sbilanciati[^2403.07483v2].

Altri studi si concentrano su tecniche specifiche come le *Extreme Learning Machines* per la predizione precoce basata su questionari, utile in aree con risorse mediche limitate[^2202.11216v1], o l'uso di reti neurali profonde con dropout per ridurre l'overfitting nei dataset come quello dei Pima Indians[^1707.08386v1]. Un approccio ibrido che combina ensemble training con algoritmi genetici ha mostrato efficacia nella diagnosi[^2103.08186v1].

L'integrazione di fattori socio-economici è anche cruciale: uno studio ha analizzato l'impatto del reddito e di altri indicatori di salute (pressione, colesterolo, BMI) utilizzando dati BBRSS, evidenziando come i redditi più bassi siano associati a una maggiore incidenza di diabete[^2404.13260v1]. Inoltre, l'analisi di dati "360-degree" su milioni di clienti ha permesso di sviluppare modelli di classificazione per la predizione del diabete cronico[^2109.01863v1].

Sistemi di supporto alle decisioni cliniche (AI-CDSS) stanno emergendo come strumenti vitali per i medici di base. Un recente studio ha sviluppato un AI-CDSS ibrido che ha mostrato una precisione elevata nella predizione del diabete di tipo 2, superando significativamente i non-endocrinologi[^2602.11237v1].

Recenti ricerche hanno ulteriormente ampliato il panorama predittivo. L'uso di *Ensemble Classifier* basati su dati di sondaggi e stile di vita (NHANES) ha dimostrato alte prestazioni nella predizione dell'insorgenza del diabete di tipo II[^1708.07480v1]. Un altro studio ha proposto un modello ensemble pesato (soft voting) che ha migliorato la capacità di recupero delle previsioni errate rispetto ai singoli algoritmi[^1910.09356v1]. Inoltre, l'integrazione di ontologie con algoritmi di machine learning ha mostrato che i classificatori basati su ontologie, combinati con SVM, offrono la migliore accuratezza nella diagnosi[^1205.5921v2]. Per affrontare lo sbilanciamento dei dati, tecniche avanzate come *CopulaSMOTE* hanno dimostrato di migliorare il recupero della classe minoritaria nei dataset tabellari di diabete[^2506.17326v3].

Nuovi approcci includono l'uso di *Task-wise Split Gradient Boosting Trees* (TSGB) per la predizione multi-centro, che affronta l'eterogeneità dei dati e l'insufficienza dei casi in singoli centri sanitari, superando i metodi standard di GBDT[^2108.07107v1]. Studi comparativi su classificatori tradizionali e ensemble avanzati (come DNet, un ibrido CNN-LSTM) hanno mostrato accuracie fino al 99.79%, evidenziando il potenziale delle architetture ibride[^2505.07036v1]. L'analisi dei Record Sanitari Elettronici (EHR) tramite modelli come BiLSTM-CRF combinato con XGBoost ha permesso di identificare pattern temporali latenti per una prognosi più precisa[^2412.03961v1]. Inoltre, l'uso di algoritmi di apprendimento strutturale per creare Reti Bayesiane Causalì ha offerto insight sulle vie causali dei fattori di rischio, supportando decisioni cliniche più informate[^2403.14327v1]. La predizione del diabete post-trapianto di fegato è stata affrontata con modelli di sopravvivenza (Cox, Random Forest) che integrano dati storici per stimare il rischio nei primi anni post-operatori[^1812.00506v2]. Studi demografici hanno anche evidenziato differenze di genere nei fattori di rischio, mostrando come BMI e WhtR abbiano impatti diversi su maschi e femmine, suggerendo la necessità di modelli personalizzati[^2311.10731v1]. Infine, framework XAI (Explainable AI) sono stati integrati per garantire trasparenza nelle predizioni, identificando BMI, età e attività fisica come predittori chiave[^2501.18071v2].

## Monitoraggio e Gestione Digitale

La gestione del diabete sta beneficiando di piattaforme digitali e dispositivi indossabili. *Diabetes Link* è una piattaforma completa che permette il monitoraggio dei parametri clinici e la connessione con supervisori, offrendo funzionalità superiori rispetto ad altre proposte[^2011.02286v1].

Per i pazienti in terapia insulinica, la sicurezza alla guida è un tema critico. Uno studio ha dimostrato che l'iperglicemia acuta aumenta significativamente il rischio di arresti non sicuri agli incroci nei conducenti con diabete di tipo 1, sottolineando la necessità di valutare la fisiologia nei criteri di licenza[^2104.03735v2].

Dispositivi indossabili intelligenti, come gli smartwatch, possono essere utilizzati per rilevare condizioni di emergenza come il coma diabetico, analizzando mobilità, frequenza cardiaca e umidità cutanea per allertare i soccorsi[^1510.02196v1]. Un altro sistema, *The Diabetic Buddy*, integra sensori per il monitoraggio continuo del glucosio e riconoscimento del cibo tramite deep learning, sviluppato con un dataset specifico per la dieta mediorientale[^2101.03203v1].

In contesti di pandemia, soluzioni di smart healthcare sono state proposte per il controllo glicemico e insulinico dei pazienti diabetici, considerati ad alto rischio per il COVID-19[^2008.11153v1].

L'evoluzione verso agenti conversazionali basati su LLM sta rivoluzionando l'assistenza personalizzata. *DM-Bench* ha introdotto un benchmark specifico per valutare le prestazioni dei LLM nelle decisioni quotidiane per i pazienti diabetici, evidenziando la variabilità delle prestazioni tra i modelli attuali[^2510.00038v2]. Un approccio *Knowledge-Infused* ha proposto un agente conversazionale (CHA) potenziato da linee guida dietetiche e strumenti analitici, dimostrando prestazioni superiori nella gestione dei nutrienti[^2402.10153v2]. Inoltre, framework come *HealthEdge* integrano IoT, edge e cloud computing per la predizione del diabete di tipo 2, mostrando come il Random Forest possa superare la Regressione Logistica in accuratezza[^2301.10450v1]. La gestione dell'esercizio fisico è stata affrontata con modelli di controllo robusti a ciclo chiuso per la progressione a lungo termine del diabete di tipo 2[^2501.12892v1], mentre l'analisi dei fattori che influenzano la durata del ricovero ospedaliero ha offerto insight per una migliore gestione delle risorse[^2406.05189v2]. Anche la riabilitazione fisica è stata modellata matematicamente tramite FAHP per personalizzare le prescrizioni di esercizio[^2201.07884v1]. Infine, fattori culturali influenzano l'adozione delle app di auto-gestione, come evidenziato in studi condotti in Sudafrica[^2108.09953v1].

Il monitoraggio continuo del glucosio (CGM) è stato potenziato da modelli di previsione basati su reti neurali e approcci bayesiani. Un sistema basato su Bayesian Structural Time Series (BSTS) ha integrato dati CGM, dieta e informazioni individuali per prevedere i livelli di glucosio con alta precisione (MAE 6.41 mg/dL) per il diabete di tipo 2[^2409.07315v1]. Per il diabete di tipo 1, modelli di deep reinforcement learning e ensemble regressori hanno migliorato la previsione a 30 minuti, supportando decisioni più tempestive sull'insulina[^2502.00065v1]. L'incertezza nelle previsioni è stata affrontata con modelli basati su Transformer e output evidenziali, che forniscono stime di incertezza calibrate, cruciali per la sicurezza clinica[^2603.04955v2]. Dashboard cliniche integrate in sistemi come OpenMRS hanno semplificato la visualizzazione dei dati di laboratorio (glicemia, funzione renale) per i medici, migliorando il processo decisionale[^1910.11437v1].

## Complicanze, Comorbidità e Fattori Ambientali

Il diabete interagisce complessamente con altre condizioni e fattori ambientali. L'inquinamento atmosferico (PM2.5) è stato oggetto di studio per valutare il suo legame con la crescita della popolazione diabetica in diversi paesi, suggerendo un possibile impatto ambientale[^2307.16417v1].

L'interazione tra diabete e malattie infettive è un'altra area di studio. Un modello epidemiologico ha mostrato che i pazienti diabetici hanno un rischio significativamente più alto di contrarre la malaria, con un odds ratio significativamente superiore rispetto ai non diabetici, specialmente in contesti di cambiamento climatico[^2511.08562v2]. Modelli matematici hanno anche analizzato la comorbidità diabete-COVID-19, evidenziando come i pazienti diabetici abbiano un rischio di morte significativamente più alto e come le misure di controllo (lockdown, vaccinazione) siano cruciali[^2201.08224v2]. Studi multinomiali hanno inoltre esaminato le comorbidità tra diabete, CVD e obesità, trovando forti gradienti socio-economici nella prevalenza di queste combinazioni di malattie[^1411.2514v2].

Nanotecnologie, come le nanoparticelle di ossido di zinco (ZnO NPs), stanno sendo esplorate per le loro proprietà antidiabetiche e di miglioramento della sensibilità all'insulina, sebbene la tossicità a lungo termine richieda ulteriori indagini[^2409.04486v1]. Anche l'uso della luce (TLS) è stato teorizzato come potenziale trattamento per obesità e diabete, mimando gli uncouplers chimici senza effetti collaterali pericolosi[^1804.04500v1].

L'analisi dei social media, in particolare Twitter, rivela come il diabete sia spesso discusso in correlazione con obesità, dieta ed esercizio fisico, con temi emergenti come la pressione sanguigna e l'Alzheimer[^1709.07916v1] e una rete complessa di autori influenti (blog, ONG) che guidano la conversazione[^1508.05764v4]. Studi sull' discourse sui social media hanno evidenziato la presenza di disinformazione e fat-shaming, sottolineando la necessità di fonti affidabili[^1804.02850v1].

Le complicanze oftalmiche, come la retinopatia diabetica, sono state analizzate attraverso l'uso di reti bayesiane per comprendere le relazioni tra biomarcatori[^2406.17090v1]. Metodi di spiegabilità (XAI) basati su concetti (CAV e Concept Bottleneck) sono stati applicati per migliorare l'interpretabilità delle reti neurali nella classificazione della retinopatia[^2410.03188v1]. L'uso di ensemble di classificatori su immagini del fondo oculare ha migliorato il rilevamento della gravità della retinopatia[^2307.16622v1], mentre l'analisi di foto esterne dell'occhio ha rivelato segnali nascosti di controllo glicemico e retinopatia[^2011.11732v1]. La fusione multimodale di dati OCT, OCTA e LSO ha mostrato potenziale per la diagnosi automatica della retinopatia proliferativa[^2304.00003v1]. Inoltre, l'uso di CNN pre-addestrate (come VGG-16) ha raggiunto l'82% di accuratezza nel rilevamento della retinopatia[^2001.05835v1], e un approccio di transfer learning multistadio ha ottenuto sensibilità e specificità del 99% nella rilevazione dello stadio della malattia[^2003.02261v1].

Lo studio della morfologia del pancreas su larga scala ha confermato che le dimensioni e la forma del pancreas sono alterate nel diabete di tipo 2[^2508.14878v1], e l'interazione tra diabete e ictro è stata esaminata per identificare target terapeutici comuni[^2011.06962v1]. La predizione precoce della nefropatia diabetica (albuminuria) è stata affrontata con modelli di apprendimento supervisionato (MLP, SVM, Random Forest), dove il MLP ha mostrato le migliori prestazioni per lo screening[^2309.16742v4].

## Infrastruttura Dati e Metodi Non Invasivi

La standardizzazione dei dati è fondamentale per la ricerca. Il formato *DIAX* (DIAbetes eXchange) propone uno standard JSON unificato per i dati temporali del diabete (CGM, insulina, pasti), facilitando l'interoperabilità e la ricerca su grandi dataset[^2604.11944v1]. La collezione *Glucose-ML* fornisce dataset pubblici per lo sviluppo di AI robuste, evidenziando come le prestazioni degli algoritmi varino significativamente tra dataset diversi[^2507.14077v1]. Dataset integrati come *DiaData* (2510 soggetti, 149 milioni di misurazioni) e *DiaTrend* (dati da dispositivi clinici) stanno abilitando nuove ricerche su pattern glicemici e predizione di eventi avversi[^2508.09160v2][^2304.06506v1]. Studi su attributi demografici multi-etichetta hanno anche esplorato l'uso di dati demografici per la privacy-preserving data mining e la valutazione del rischio di identificazione nei pazienti diabetici[^1503.07795v1].

Metodi diagnostici non invasivi stanno guadagnando attenzione. L'uso di segnali di fotopletismografia (PPG) combinati con machine learning (Logistic Regression, XGBoost) ha mostrato potenziale per il rilevamento remoto del diabete, sebbene con accuratezze ancora da migliorare[^2308.01930v1].

L'analisi del respiro per il rilevamento di biomarcatori come l'acetone sta emergendo come metodo non invasivo. Sensori a nanofili di ossido di indio-fosfuro funzionalizzati con chitosano hanno permesso il rilevamento ultra-sensibile dell'acetone nel respiro, utile per il monitoraggio della chetoacidosi[^2312.00510v1]. Studi causali hanno investigato l'influenza dei composti organici volatili (VOC) sui livelli di glucosio, proponendo classificatori per lo screening precoce[^2605.22075v1]. Inoltre, l'indice *maxSpeed* (velocità massima di cambiamento del glucosio) derivato dai dati CGM ha dimostrato di distinguere significativamente tra prediabete e diabete[^2506.12567v1].

L'analisi del microbiota intestinale ha identificato nucleotidi 9-meri con frequenze significativamente diverse nei pazienti diabetici, offrendo potenziali biomarcatori per la diagnosi precoce[^1505.00476v1]. L'analisi delle variazioni della frequenza cardiaca (HRV) tramite plot di Poincaré e analisi spettrale ha rivelato alterazioni nel sistema di regolazione cardiaca nei pazienti diabetici, con potenziali applicazioni nella valutazione delle complicanze cardiovascolari[^1005.5221v1]. L'analisi del flusso sanguigno microvascolare nel piede tramite flowmetry laser e test termici ha mostrato differenze spettrali significative, utili per diagnosticare precocemente le anomalie microcircolatorie[^1707.02110v1].

L'uso di elettrocardiogrammi (ECG) a 12 derivazioni, combinato con informazioni demografiche e deep learning, ha dimostrato potenziale nel rilevare il diabete di nuova insorgenza, offrendo un metodo automatizzato per lo screening su larga scala[^2205.02900v3]. L'analisi di fenotipi addominali tramite imaging CT e AI ha identificato firme di composizione corporea (grasso viscerale, muscolo scheletrico grasso) associate al rischio di diabete di tipo 2, indipendentemente dal BMI[^2508.11063v1]. Dispositivi indossabili innovativi, come i "Smart Diabetic Socks", utilizzano sensori di pressione e modelli agli elementi finiti per prevenire ulcere da pressione nei piedi diabetici, inviando alert in caso di rischio[^1404.3993v1].

## Riferimenti Bibliografici

[^2409.04486v1]: The Current and Future Perspectives of Zinc Oxide Nanoparticles in the Treatment of Diabetes Mellitus
[^1510.02196v1]: Algorithm and Related Application for Smart Wearable Devices to Reduce the Risk of Death and Brain Damage in Diabetic Coma
[^2509.12259v1]: Quantum-Inspired Stacked Integrated Concept Graph Model (QISICGM) for Diabetes Risk Prediction
[^1812.02852v1]: Automatically Explaining Machine Learning Prediction Results: A Demonstration on Type 2 Diabetes Risk Prediction
[^2011.02286v1]: Diabetes Link: Platform for Self-Control and Monitoring People with Diabetes
[^2105.09379v1]: Using Machine Learning Techniques to Identify Key Risk Factors for Diabetes and Undiagnosed Diabetes
[^2101.03203v1]: The Diabetic Buddy: A Diet Regulator andTracking System for Diabetics
[^2307.16417v1]: Effect of air pollution on the growth of diabetic population
[^2102.12984v1]: Variable Weights Neural Network For Diabetes Classification
[^2202.11216v1]: Early Stage Diabetes Prediction via Extreme Learning Machine
[^2008.11153v1]: Smart Healthcare for Diabetes: A COVID-19 Perspective
[^2506.11501v1]: Diabetes Prediction and Management Using Machine Learning Approaches
[^2506.10180v1]: A Comparative Study of Machine Learning Techniques for Early Prediction of Diabetes
[^2602.11237v1]: AI-Driven Clinical Decision Support System for Enhanced Diabetes Diagnosis and Management
[^2604.11944v1]: A unified data format for managing diabetes time-series data: DIAbetes eXchange (DIAX)
[^2403.07483v2]: DiabetesNet: A Deep Learning Approach to Diabetes Diagnosis
[^2404.13260v1]: Predicting Diabetes with Machine Learning Analysis of Income and Health Factors
[^2511.08562v2]: Climate Driven Interactions Between Malaria Transmission and Diabetes Prevalence
[^2507.14077v1]: Glucose-ML: A collection of longitudinal diabetes datasets for development of robust AI solutions
[^1707.08386v1]: Reduction of Overfitting in Diabetes Prediction Using Deep Learning Neural Network
[^1804.04500v1]: Can the light be used to treat obesity and diabetes?
[^2104.03735v2]: Sugar and Stops in Drivers with Insulin-Dependent Type 1 Diabetes
[^1709.07916v1]: Characterizing Diabetes, Diet, Exercise, and Obesity Comments on Twitter
[^2109.01863v1]: Customer 360-degree Insights in Predicting Chronic Diabetes
[^1904.09884v1]: Health Behaviour Change Techniques in Diabetes Management Applications: A Systematic Review
[^2012.15025v1]: A Review of Machine Learning Techniques for Applied Eye Fundus and Tongue Digital Image Processing with Diabetes Management System
[^2308.01930v1]: Machine Learning-Based Diabetes Detection Using Photoplethysmography Signal Features
[^2103.08186v1]: Hybrid stacked ensemble combined with genetic algorithms for Prediction of Diabetes
[^1508.05764v4]: The 'who' and 'what' of #diabetes on Twitter
[^1901.10530v1]: An Advanced Conceptual Diagnostic Healthcare Framework for Diabetes and Cardiovascular Disorders
[^2409.13191v2]: Diabetica: Adapting Large Language Model to Enhance Multiple Medical Tasks in Diabetes Care and Management
[^2104.07820v2]: Machine Learning Approaches for Type 2 Diabetes Prediction and Care Management
[^2406.00993v1]: Detection of Acetone as a Gas Biomarker for Diabetes Based on Gas Sensor Technology
[^2406.05189v2]: Analyzing the factors that are involved in length of inpatient stay at the hospital for diabetes patients
[^2406.17090v1]: Exploring Biomarker Relationships in Both Type 1 and Type 2 Diabetes Mellitus Through a Bayesian Network Analysis Approach
[^2506.17326v3]: CopulaSMOTE: A Copula-Based Oversampling Approach for Imbalanced Classification in Diabetes Prediction
[^1910.09356v1]: Supervised Machine Learning based Ensemble Model for Accurate Prediction of Type 2 Diabetes
[^1708.07480v1]: An Ensemble Classifier for Predicting the Onset of Type II Diabetes
[^2101.07350v1]: Update on the genetic and epigenetic etiology of gestational diabetes mellitus: a review
[^2410.03188v1]: Looking into Concept Explanation Methods for Diabetic Retinopathy Classification
[^2201.07884v1]: FAHP-based Mathematical Model for Exercise Rehabilitation Management of Diabetes Mellitus
[^2307.16622v1]: Detecting diabetic retinopathy severity through fundus images using an ensemble of classifiers
[^2011.11732v1]: Detecting hidden signs of diabetes in external eye photographs
[^2510.00038v2]: DM-Bench: Benchmarking LLMs for Personalized Decision Making in Diabetes Management
[^2402.10153v2]: Knowledge-Infused LLM-Powered Conversational Health Agent: A Case Study for Diabetes Patients
[^2506.12567v1]: Maximal Speed of Glucose Change Significantly Distinguishes Prediabetes from Diabetes
[^2411.00858v1]: DiabML: AI-assisted diabetes diagnosis method with meta-heuristic-based feature selection
[^2508.14878v1]: Lifespan Pancreas Morphology for Control vs Type 2 Diabetes using AI on Largescale Clinical Imaging
[^2208.06354v1]: A novel solution of deep learning for enhanced support vector machine for predicting the onset of type 2 diabetes
[^2301.03093v1]: Prognosis and Treatment Prediction of Type-2 Diabetes Using Deep Neural Network and Machine Learning Classifiers
[^1205.5921v2]: Diabetes prediction using Machine Learning algorithms and ontology
[^1810.03044v3]: Artificial Intelligence for Diabetes Case Management: The Intersection of Physical and Mental Health
[^2011.06962v1]: Bridging the Gap Between Diabetes and Stroke in Search of High Clinical Relevance Therapeutic Targets
[^2605.22075v1]: Can Breath Biomarkers Causally Influence Blood Glucose? Investigating VOC-Mediated Modulation in Diabetes
[^2312.00510v1]: Nanowire Array Breath Acetone Sensor for Diabetes Monitoring
[^2501.12892v1]: Closed-loop robust control of long-term diabetes progression via physical activity management
[^2304.00003v1]: Multimodal Information Fusion For The Diagnosis Of Diabetic Retinopathy
[^1502.03774v1]: Diagnosis of diabetes using classification mining techniques
[^2301.10450v1]: HealthEdge: A Machine Learning-Based Smart Healthcare Framework for Prediction of Type 2 Diabetes in an Integrated IoT, Edge, and Cloud Computing System
[^2108.09953v1]: Impact of Culture on the Adoption of Diabetes Self-Management Applications: Cape Flats, South Africa
[^2001.05835v1]: Diabetic Retinopathy detection by retinal image recognizing
[^1411.2514v2]: A Multinomial Model for Comorbidity in England of Longstanding CVD, Diabetes, and Obesity
[^2108.07107v1]: Task-wise Split Gradient Boosting Trees for Multi-center Diabetes Prediction
[^2505.07036v1]: Predicting Diabetes Using Machine Learning: A Comparative Study of Classifiers
[^2003.02261v1]: Deep Learning Approach to Diabetic Retinopathy Detection
[^2409.07315v1]: Integrating Bayesian Approaches and Expert Knowledge for Forecasting Continuous Glucose Monitoring Values in Type 2 Diabetes Mellitus
[^2603.04955v2]: Uncertainty quantification in neural network-based glucose prediction for diabetes
[^1910.11437v1]: Development and Implementation of a Dashboard for Diabetes Care Management in OpenMRS
[^2309.16742v4]: Supervised Learning Models for Early Detection of Albuminuria Risk in Type-2 Diabetes Mellitus Patients
[^2201.08224v2]: A Mathematical Model of Transmission Dynamics of SARS-Cov-2 (Covid-19) with an Underlying Condition of Diabetes
[^2508.09160v2]: Presenting DiaData for Research on Type 1 Diabetes
[^2412.03961v1]: Electronic Health Records-Based Data-Driven Diabetes Knowledge Unveiling and Risk Prognosis
[^1505.00476v1]: Nucleotide 9-mers Characterize the Type II Diabetic Gut Metagenome
[^2508.11063v1]: Data-Driven Abdominal Phenotypes of Type 2 Diabetes in Lean, Overweight, and Obese Cohorts
[^2403.14327v1]: Investigating the validity of structure learning algorithms in identifying risk factors for intervention in patients with diabetes
[^1804.02850v1]: Information Sources and Needs in the Obesity and Diabetes Twitter Discourse
[^2502.00065v1]: Blood Glucose Level Prediction in Type 1 Diabetes Using Machine Learning
[^2402.02188v1]: Diabetes detection using deep learning techniques with oversampling and feature augmentation
[^2105.09490v1]: Designing AI-based Conversational Agent for Diabetes Care in a Multilingual Context
[^1812.00506v2]: Prediction of New Onset Diabetes after Liver Transplant
[^1005.5221v1]: Lagged Poincaré and auto-correlation analysis of Heart rate variability in diabetes
[^2311.10731v1]: Gender-Based Comparative Study of Type 2 Diabetes Risk Factors in Kolkata, India: A Machine Learning Approach
[^2304.06506v1]: DiaTrend: A dataset from advanced diabetes technology to enable development of novel analytic solutions
[^2606.12699v1]: LLM-Powered Personalized Glycemic Assessment in Type 2 Diabetes with Wearable Sensor Data
[^1404.3993v1]: Smart Diabetic Socks: Embedded device for diabetic foot prevention
[^2205.02900v3]: New-Onset Diabetes Assessment Using Artificial Intelligence-Enhanced Electrocardiography
[^1503.07795v1]: Multi-Labeled Classification of Demographic Attributes of Patients: a case study of diabetics patients
[^1707.02110v1]: Spectral analysis of the blood flow in the foot microvascular bed during thermal testing in patients with diabetes mellitus
[^2501.18071v2]: Towards Transparent and Accurate Diabetes Prediction Using Machine Learning and Explainable Artificial Intelligence
