# Living Survey: diabetes

## Introduzione

Questo documento raccoglie la letteratura scientifica sul tema **diabetes**.

## Intelligenza Artificiale e Predizione del Diabete

L'uso dell'intelligenza artificiale e del machine learning per la predizione e la diagnosi del diabete è un'area di ricerca estremamente attiva. Diversi studi recenti hanno proposto modelli avanzati per migliorare l'accuratezza e l'efficienza.

Il modello *Quantum-Inspired Stacked Integrated Concept Graph Model* (QISICGM) rappresenta un approccio innovativo che combina tecniche ispirate alla quantistica con ensemble di machine learning (Random Forest, Extra Trees, Transformers, CNN e FFNN) per predire il rischio di diabete con un punteggio F1 di 0.8933, superando i metodi tradizionali[^2509.12259v1]. Analogamente, *DiabetesNet* propone una rete neurale a retropropagazione con normalizzazione di batch e bilanciamento dei dati, raggiungendo accuracie fino al 95.28% su dataset specifici, affrontando le sfide dei dati sbilanciati[^2403.07483v2].

Altri studi si concentrano su tecniche specifiche come le *Extreme Learning Machines* per la predizione precoce basata su questionari, utile in aree con risorse mediche limitate[^2202.11216v1], o l'uso di reti neurali profonde con dropout per ridurre l'overfitting nei dataset come quello dei Pima Indians[^1707.08386v1]. Un approccio ibrido che combina ensemble training con algoritmi genetici ha riportato accuracie fino al 99% nella diagnosi[^2103.08186v1].

L'integrazione di fattori socio-economici è anche cruciale: uno studio ha analizzato l'impatto del reddito e di altri indicatori di salute (pressione, colesterolo, BMI) utilizzando dati BRFSS, evidenziando come i redditi più bassi siano associati a una maggiore incidenza di diabete[^2404.13260v1]. Inoltre, l'analisi di dati "360-degree" su milioni di clienti ha permesso di sviluppare modelli di classificazione con l'80% di accuratezza per la predizione del diabete cronico[^2109.01863v1].

Sistemi di supporto alle decisioni cliniche (AI-CDSS) stanno emergendo come strumenti vitali per i medici di base. Un recente studio ha sviluppato un AI-CDSS ibrido che ha raggiunto una precisione del 99.8% nella predizione del diabete di tipo 2, superando significativamente i non-endocrinologi[^2602.11237v1].

Recenti ricerche hanno ulteriormente ampliato il panorama predittivo. L'uso di *Ensemble Classifier* basati su dati di sondaggi e stile di vita (NHANES) ha dimostrato alte prestazioni (AUC 0.834) nella predizione dell'insorgenza del diabete di tipo II[^1708.07480v1]. Un altro studio ha proposto un modello ensemble pesato (soft voting) che ha raggiunto l'85% di accuratezza nel predire il diabete di tipo 2, migliorando la capacità di recupero delle previsioni errate rispetto ai singoli algoritmi[^1910.09356v1]. Inoltre, l'integrazione di ontologie con algoritmi di machine learning ha mostrato che i classificatori basati su ontologie, combinati con SVM, offrono la migliore accuratezza nella diagnosi[^1205.5921v2]. Per affrontare lo sbilanciamento dei dati, tecniche avanzate come *CopulaSMOTE* hanno dimostrato di migliorare il recupero della classe minoritaria nei dataset tabellari di diabete[^2506.17326v3].

## Monitoraggio e Gestione Digitale

La gestione del diabete sta beneficiando di piattaforme digitali e dispositivi indossabili. *Diabetes Link* è una piattaforma completa che permette il monitoraggio dei parametri clinici e la connessione con supervisori, offrendo funzionalità superiori rispetto ad altre proposte[^2011.02286v1].

Per i pazienti in terapia insulinica, la sicurezza alla guida è un tema critico. Uno studio ha dimostrato che l'iperglicemia acuta aumenta significativamente il rischio di arresti non sicuri agli incroci nei conducenti con diabete di tipo 1, sottolineando la necessità di valutare la fisiologia nei criteri di licenza[^2104.03735v2].

Dispositivi indossabili intelligenti, come gli smartwatch, possono essere utilizzati per rilevare condizioni di emergenza come il coma diabetico, analizzando mobilità, frequenza cardiaca e umidità cutanea per allertare i soccorsi[^1510.02196v1]. Un altro sistema, *The Diabetic Buddy*, integra sensori per il monitoraggio continuo del glucosio e riconoscimento del cibo tramite deep learning, sviluppato con un dataset specifico per la dieta mediorientale[^2101.03203v1].

In contesti di pandemia, soluzioni di smart healthcare sono state proposte per il controllo glicemico e insulinico dei pazienti diabetici, considerati ad alto rischio per il COVID-19[^2008.11153v1].

L'evoluzione verso agenti conversazionali basati su LLM sta rivoluzionando l'assistenza personalizzata. *DM-Bench* ha introdotto un benchmark specifico per valutare le prestazioni dei LLM nelle decisioni quotidiane per i pazienti diabetici, evidenziando la variabilità delle prestazioni tra i modelli attuali[^2510.00038v2]. Un approccio *Knowledge-Infused* ha proposto un agente conversazionale (CHA) potenziato da linee guida dietetiche e strumenti analitici, dimostrando prestazioni superiori nella gestione dei nutrienti rispetto a GPT-4[^2402.10153v2]. Inoltre, framework come *HealthEdge* integrano IoT, edge e cloud computing per la predizione del diabete di tipo 2, mostrando come il Random Forest possa superare la Regressione Logistica in accuratezza[^2301.10450v1]. La gestione dell'esercizio fisico è stata affrontata con modelli di controllo robusti a ciclo chiuso per la progressione a lungo termine del diabete di tipo 2[^2501.12892v1], mentre l'analisi dei fattori che influenzano la durata del ricovero ospedaliero ha offerto insight per una migliore gestione delle risorse[^2406.05189v2]. Anche la riabilitazione fisica è stata modellata matematicamente tramite FAHP per personalizzare le prescrizioni di esercizio[^2201.07884v1]. Infine, fattori culturali influenzano l'adozione delle app di auto-gestione, come evidenziato in studi condotti in Sudafrica[^2108.09953v1].

## Complicanze, Comorbidità e Fattori Ambientali

Il diabete interagisce complessamente con altre condizioni e fattori ambientali. L'inquinamento atmosferico (PM2.5) è stato oggetto di studio per valutare il suo legame con la crescita della popolazione diabetica in diversi paesi, suggerendo un possibile impatto ambientale[^2307.16417v1].

L'interazione tra diabete e malattie infettive è un'altra area di studio. Un modello epidemiologico ha mostrato che i pazienti diabetici hanno un rischio significativamente più alto di contrarre la malaria, con un'odds ratio 1.8-4.0 volte superiore rispetto ai non diabetici, specialmente in contesti di cambiamento climatico[^2511.08562v2].

Nanotecnologie, come le nanoparticelle di ossido di zinco (ZnO NPs), stanno sendo esplorate per le loro proprietà antidiabetiche e di miglioramento della sensibilità all'insulina, sebbene la tossicità a lungo termine richieda ulteriori indagini[^2409.04486v1]. Anche l'uso della luce (TLS) è stato teorizzato come potenziale trattamento per obesità e diabete, mimando gli uncouplers chimici senza effetti collaterali pericolosi[^1804.04500v1].

L'analisi dei social media, in particolare Twitter, rivela come il diabete sia spesso discusso in correlazione con obesità, dieta ed esercizio fisico, con temi emergenti come la pressione sanguigna e l'Alzheimer[^1709.07916v1] e una rete complessa di autori influenti (blog, ONG) che guidano la conversazione[^1508.05764v4].

Le complicanze oftalmiche, come la retinopatia diabetica, sono state analizzate attraverso l'uso di reti bayesiane per comprendere le relazioni tra biomarcatori[^2406.17090v1]. Metodi di spiegabilità (XAI) basati su concetti (CAV e Concept Bottleneck) sono stati applicati per migliorare l'interpretabilità delle reti neurali nella classificazione della retinopatia[^2410.03188v1]. L'uso di ensemble di classificatori su immagini del fondo oculare ha migliorato il rilevamento della gravità della retinopatia[^2307.16622v1], mentre l'analisi di foto esterne dell'occhio ha rivelato segnali nascosti di controllo glicemico e retinopatia[^2011.11732v1]. La fusione multimodale di dati OCT, OCTA e LSO ha mostrato potenziale per la diagnosi automatica della retinopatia proliferativa[^2304.00003v1]. Inoltre, lo studio della morfologia del pancreas su larga scala ha confermato che le dimensioni e la forma del pancreas sono alterate nel diabete di tipo 2[^2508.14878v1], e l'interazione tra diabete e ictro è stata esaminata per identificare target terapeutici comuni[^2011.06962v1].

## Infrastruttura Dati e Metodi Non Invasivi

La standardizzazione dei dati è fondamentale per la ricerca. Il formato *DIAX* (DIAbetes eXchange) propone uno standard JSON unificato per i dati temporali del diabete (CGM, insulina, pasti), facilitando l'interoperabilità e la ricerca su grandi dataset[^2604.11944v1]. La collezione *Glucose-ML* fornisce dataset pubblici per lo sviluppo di AI robuste, evidenziando come le prestazioni degli algoritmi varino significativamente tra dataset diversi[^2507.14077v1].

Metodi diagnostici non invasivi stanno guadagnando attenzione. L'uso di segnali di fotopletismografia (PPG) combinati con machine learning (Logistic Regression, XGBoost) ha mostrato potenziale per il rilevamento remoto del diabete, sebbene con accuratezze ancora da migliorare[^2308.01930v1].

L'analisi del respiro per il rilevamento di biomarcatori come l'acetone sta emergendo come metodo non invasivo. Sensori a nanofili di ossido di indio-fosfuro funzionalizzati con chitosano hanno permesso il rilevamento ultra-sensibile dell'acetone nel respiro, utile per il monitoraggio della chetoacidosi[^2312.00510v1]. Studi causali hanno investigato l'influenza dei composti organici volatili (VOC) sui livelli di glucosio, proponendo classificatori per lo screening precoce[^2605.22075v1]. Inoltre, l'indice *maxSpeed* (velocità massima di cambiamento del glucosio) derivato dai dati CGM ha dimostrato di distinguere significativamente tra prediabete e diabete[^2506.12567v1].

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
