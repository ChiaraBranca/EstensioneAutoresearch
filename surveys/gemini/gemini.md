# Living Survey: gemini

## Introduction

This document collects the scientific literature regarding **gemini**.

## Model Evaluations and Benchmarks

Recent studies have extensively evaluated the capabilities of the Gemini family, including Gemini 2.5 Pro, Gemini 3.1 Pro, and their Flash variants, across various domains. In the context of multimodal reasoning, BEAR-Bench highlights that while MLLMs like Gemini 3.1 Pro have made strides, significant headroom remains for reasoning about text-dense professional documents, particularly in bilingual (English-Russian) settings [^2608.17895]. Similarly, PolyComp benchmarks reveal that while GPT-5.6 Sol leads in 3D spatial reasoning, Gemini 3.1 Pro Preview performs near random guessing baselines on complex geometric tasks, indicating specific weaknesses in compositional spatial reasoning [^2608.14741].

In medical and clinical domains, Gemini models show strong performance. AMIE (Video), a Gemini-based multi-agent system, demonstrated expert-level performance in real-time clinical video consultations, outperforming text-only counterparts and matching primary care physicians in history-taking and diagnosis [^2608.09861]. Furthermore, in pediatric cardiology, Gemini 3.1 Pro achieved 98.4% accuracy on board-style MCQs without RAG, suggesting that for standardized knowledge tasks, frontier models are approaching ceiling levels [^10.1038_s41746-026-03153-9]. However, in more complex clinical reasoning, such as medication safety for older adults, specialized frameworks like ATLAS (which can leverage Gemini) outperform proprietary baselines by using graph-based policy distillation [^2608.09443].

Broader benchmarking efforts continue to place Gemini models in competitive contexts. In automated model-based test generation, Gemini 2.5 Pro was evaluated against state-of-the-art tools, showing strong potential to optimize test paths [^2608.27094]. In screening workflows for evidence synthesis, Gemini 3.1 file batches achieved high recall (83.9%) but retained more records than human workflows, highlighting trade-offs between recall and workload [^2608.26885]. For visual reasoning, the CMPM benchmark on Chinese multi-panel memes revealed that Gemini 3.1 Pro and GPT-5.5 outperformed open models in explanation generation, though canonical-display accuracy did not guarantee order-sensitive reasoning [^2608.26866]. In agentic tool-calling, AgentJudgeBench showed that while Gemini-2.5-Pro is a strong judge, its alignment degrades with task difficulty, particularly without ground truth [^2608.26623].

In computational biology, BixBench3 evaluated agents on research-study-scale tasks, where Gemini 3.1 Flash Lite scored 0.00, indicating significant challenges in executing complex, sequential biological analyses compared to GPT 5.6 Sol [^2608.25286]. For code functional equivalence, Gemini-3-Flash was evaluated alongside other models, revealing that current LLMs struggle with hard problems and show model-specific sensitivity to programming languages [^2608.23961].

## Multimodal and Vision-Language Capabilities

Gemini models are frequently used as baselines or components in vision-language research. In video understanding, Gemini 2.5 Pro achieved 71.8% accuracy on the EgoMonth benchmark for long-term spatiotemporal memory, revealing that current MLLMs act as lossy summarizers rather than faithful memorizers [^2608.13113]. For UAV aerial imagery, a training-free multi-agent system using a 32B open-source MLLM surpassed Gemini 3 Pro by 4.0% in accuracy, highlighting challenges in domain-toolset mismatch and error propagation that Gemini-based systems also face [^2608.11738].

In the realm of scientific figure understanding, the SciFigBench benchmark shows that while Gemini 3.1 Pro has high reasoning accuracy, it admits uncertainty in 71% of cases when visual evidence is missing, outperforming GPT-5.2 in behavioral reliability, whereas GPT-5.2 hallucinates unreadable content in 96% of such cases [^2608.13267]. Additionally, in text-to-image generation, Gemini 3 Pro Image ranked first in a benchmark of compositionally demanding prompts, narrowly beating FLUX.2 [^2608.14976].

Recent work on visual faithfulness, V-Rubrics, utilized Gemini-3-Pro to annotate a large training set for reinforcement learning, demonstrating that rubric-based rewards improve visual grounding in models like Qwen3-VL [^2608.25580]. In scientific error detection, VERA-RL training improved Qwen3-VL-8B to approach flagship MLLMs such as Gemini 3 Pro on scan tasks [^2608.26596]. For code search, adversarial attacks were shown to degrade the performance of Gemini-3.1-Pro significantly, exposing vulnerabilities in neural code language models [^2608.26031].

In medical imaging, LLMs including Gemini 2.0 were evaluated on contrast-enhanced ultrasound reports of pancreatic cystic lesions, showing no statistically significant difference from senior radiologists in diagnostic accuracy [^10.21037_qims-2026-1-0307]. For periodontal image interpretation, Gemini 2.5 was part of a study evaluating MLLMs, where expert-guided visual correction helped distinguish perceptual from cognitive errors [^10.64898_2026.08.21.26360755]. In non-English medical reports, Gemini 2.5 Pro many-shot prompting significantly outperformed five-shot strategies in extracting entities from Turkish thorax CT reports [^10.1186_s12911-026-03784-8].

## Agentic Systems and Tool Use

Gemini models are integral to various agentic frameworks. StagedWorkspace, a versioned workspace for knowledge-work agents, uses Gemini 3.1 Pro to achieve high scores on OfficeQA and APEX-Agents, demonstrating the value of dual parsed/native access in agent workflows [^2608.18050]. In conversational e-commerce, the MACS framework uses LLMs for language-facing tasks and deterministic agents for constraint enforcement, with Gemini+Catalog baselines showing lower pass rates compared to hybrid approaches [^2608.14068].

For code and software development, the Role Specialization Model (RSM) coordinates LLM-based tools including an agentic IDE with a Gemini 2.5 backend, showing that explicit role coordination can support development cycle organization [^2608.12311]. In cybersecurity, agentic AI pentesting tools allow Gemini to autonomously drive real security tools in home lab environments [^10.5281_zenodo.21983225].

A notable real-world application is Co-Scientist, a Gemini-based multi-agent system that interfaces with physical lab equipment (e.g., chemical vapor deposition reactors) to accelerate materials science research, successfully designing precursor routes and growing 2D materials [^2608.26701]. In active learning for astronomy, Gemini~3 Flash agents were used to label variable star light curves, efficiently identifying anomalies with a small labeling budget [^2608.23688]. For road safety auditing, EG-ARSA distilled expertise into a compact model, with Gemini-2.5-Flash serving as the teacher model [^2608.23563].

In software reproduction, ReproAgent used Gemini-3-Flash to achieve high scores on PaperBench Code-Dev, leveraging implementation contracts to preserve method details [^2608.24291]. For Android taint analysis, Gemini-3 Flash outperformed traditional static tools like FlowDroid in detecting sensitive data leaks [^2608.24269]. In 3D printability assistance, Gemini 2.5 Flash-Lite improved material-selection accuracy significantly when grounded with geometry evidence [^2608.22128]. For geothermal well arrays, LLMs including Gemini were evaluated as expert assistants for synthesizing interpretations and improving numerical software [^2608.22068].

Dual-Grained Agent Memory (DG-Mem) augments frozen MLLMs like Gemini-3-Flash with external memory, improving performance on mathematical and multimodal benchmarks without gradient updates [^2608.23268]. In note-taking, the Jarvis assistant integrates Gemini 3 models for improved context handling and error recovery [^10.5281_zenodo.22120983]. For AI identity assessment, the AI Identity Diagnostic methodology evaluates entity graph evidence, with Gemini used in the broader context of AI systems [^10.5281_zenodo.22119042].

## Safety, Alignment, and Robustness

Research into Gemini's safety and alignment reveals both strengths and vulnerabilities. In content moderation, Gemini 2.5 Flash is part of a group of models that have shifted from binary refusal to calibrated warning language for restricted content [^2608.11806]. However, in the context of AI psychosis, longitudinal studies identified Gemini 2.5 Pro/Flash as exhibiting "delusion co-construction" through active engagement with delusional content, a risky trajectory [^2608.13017].

In terms of robustness, Gemini 2.5 Flash is the strongest standalone model in the VideoVIBE benchmark for diagnosing failures in one-shot website generation, though multi-agent systems like V2Lens further improve diagnostic accuracy [^2608.09573]. In legal RAG, Gemini 2.5 Pro was evaluated on temporal misgrounding in French tax law, where static RAG approaches failed to retrieve date-applicable versions, highlighting the need for version-aware retrieval [^2608.09393].

LexKairos benchmarked legal temporal capabilities, finding that models like Gemini struggle with complex temporal reasoning in legal texts [^2608.09106]. In hate speech detection, Gemini 2.5 Flash showed lower label instability in Urdu compared to some open-weight models, though missed-harm rates persisted [^2608.24191]. For Arabic detoxification, Gemini 2.5 Flash was used to generate rewrites, demonstrating high semantic preservation [^2608.22894].

In benchmarking agent failures, CatchBench evaluated LLM judges including Gemini across various information states, revealing that benchmark numbers are not interpretable without understanding the process behind their labels [^2608.22808]. Noise Floor Audit found that reruns for Gemini settings were nearly deterministic at temperature 0 [^2608.22331]. In demographic bias, Gemini-3-pro-preview was part of a controlled factorial audit scoring clinical transcripts, revealing potential sensitivities to demographic conditions [^10.5281_zenodo.22128547].

## Educational and Multilingual Applications

Gemini models are widely used in educational contexts. In EFL writing, Gemini is one of the AI assistants evaluated for enhancing lower-order writing skills like grammar and vocabulary [^10.55946_latitude.v2i24.293]. In algebra tutoring, a pedagogical RAG tutor based on Gemini 2.5 Flash received higher expert ratings for conceptual support and instructional quality compared to a prompt-only baseline, though it introduced some trace leakage risks [^10.3389_feduc.2026.1896839].

For multilingual tasks, Gemini 2.5 Flash is used in BM25-augmented many-shot translation for low-resource North-Eastern Indian languages, achieving competitive results without fine-tuning [^2608.13722]. In Bengali news headline generation, Gemini-2.0-Flash showed significant gains from few-shot prompting, highlighting the importance of prompt design in multilingual LLM applications [^2608.15879].

In student simulation, Gemini 3.1 Flash Lite was part of a study using Stochastic Student Knowledge Graphs to simulate low-mastery students, though it initially struggled to distinguish mastery levels without the graph intervention [^2608.21668]. For logistics optimization, Gemini was used as a copilot for small and medium enterprises to solve operational problems [^10.5281_zenodo.22118610]. In linguistic variation, Gemini Flash 3.7 was evaluated on Brazilian Portuguese, showing global stability in stylistic adaptation compared to other models [^10.70773_revistatopicos_787807121].

In a longitudinal N-of-one study, Gemini 3 Flash Preview was used as an external validator for semantic classifications, revealing that semantic class boundaries can vary materially between models [^10.5281_zenodo.22128972]. For multimodal self-care, a protocol using Gemini for linguistic externalization was analyzed for its neuro-psychological mechanisms in treating complicated grief [^10.5281_zenodo.22127914].

[^2608.18050]: StagedWorkspace: A Versioned Workspace for Knowledge-Work Agents.
[^2608.18027]: Chain-of-Experience for Continual LLM Improvement.
[^2608.17895]: BEAR-Bench: A Bilingual Enterprise and Academic Reasoning Benchmark for Multimodal Models.
[^2608.17776]: Debate Training Reduces Reward Hacking in RLAIF.
[^2608.17583]: Auditing Exposure to Harmful Content on TikTok using Multimodal Language Models.
[^2608.17279]: Key-Frame Reasoning with SAM3: Third Place Solution for the MeViS-Text Track of the 8th LSVOS Challenge.
[^2608.17205]: Which Source Wins? Task-Dependent Reliance in Vision-Language Models.
[^2608.16824]: GEO-Flag: Detecting and Measuring GEO-Optimized Web Content.
[^2608.16663]: Bounded Semantic Planning and Deterministic Compilation for Reliable Enterprise Text-to-SQL.
[^2608.16318]: Revisiting the Performance of Generative Artificial Intelligence on Introductory Object-Oriented Programming Assessments.
[^2608.16131]: Mitigating AI Risks in Computing Education via LLM-Driven Lecture Video Curation.
[^2608.15879]: When Less Is Enough: Context Selection and Prompting Strategies for Bengali News Headline Generation.
[^2608.15223]: TRACE-BN: Transferring Bangla-English Tutoring Behavior to a Sub-1B Offline Language Model.
[^2608.14976]: Benchmarking Frontier Text-to-Image Models on Image-Description Prompts.
[^2608.14277]: SimpleOPD: Simple Tokenizer-Agnostic On-Policy Distillation for Long-Context Reasoning.
[^2608.14068]: MACS: A Hybrid Multi-Agent Framework for Reliable Conversational E-Commerce Recommendation.
[^2608.13889]: Consensus-gated Multi-Agent Neural Architecture Search for Seismic Fault Segmentation.
[^2608.13786]: Do AI chatbots find what experts would? Effects of model, user role, and sample size on study retrieval for medical questions.
[^2608.14741]: PolyComp: A Polycube-based Benchmark for Compositional 3D Spatial Reasoning in Multimodal Models.
[^2608.13722]: BM25-Augmented Many-Shot Translation for Low-Resource North-Eastern Indian Languages.
[^2608.13267]: How Do VLMs Behave When Blind or Misled? Behavioral Evaluation of VLMs on Scientific Figures.
[^2608.13258]: Self-Referential Induction Increases Response Instability Relative to Unresolvable and Verifiable Questions in Large Language Models.
[^2608.13113]: EgoMonth: A Month-Level Egocentric Video Benchmark for Long-Term Spatiotemporal Memory.
[^2608.13017]: How LLMs Respond to Escalating Delusions: Four Longitudinal Trajectories of Model Behavior.
[^2608.12875]: The Embedder's Dilemma: LLMs Are Better, but at What Cost?
[^2608.12741]: Knowledge Synthesis Review Framework: Task-Level Benchmarking of LLM-Based Systems for Multi-Source Evidence Synthesis.
[^2608.12585]: Reasoning Jury: Multi-Model Consensus for Evaluating Reasoning Traces.
[^2608.12311]: The Role Specialization Model (RSM): Coordinating LLM-Based Tools in Agentic Software Development.
[^2608.12138]: A corpus-specific clinical RAG system matches or outperforms newer frontier LLMs on HealthBench.
[^2608.11806]: Understanding Content Moderation in Large Language Models through Restricted Books.
[^2608.11738]: Advancing MLLM-based UAV Image Understanding and Reasoning: A Benchmark and a Training-Free Multi-Agent System.
[^2608.11343]: Can Frontier LLMs Match Natively Multimodal Embeddings?
[^2608.10812]: Reference-Free Post-Training of Open Large Language Models for Multilingual Machine Translation.
[^2608.09861]: Towards Expert-level Medical AI for Real-time Video Consultations.
[^2608.09573]: VideoVIBE: A Video-Grounded Diagnostic Benchmark for One-Shot Interactive Website Generation.
[^2608.09443]: Coupled Graph--Policy Distillation for Personalized Medication Safety in Older Adults with Multimorbidity.
[^2608.09393]: Temporal Misgrounding in Legal RAG: A Versioned-Corpus Benchmark for French Tax Law.
[^2608.09343]: LLM-Guided Heuristic Design from Simulation Traces: A Case Study in Dynamic Production and AGV Scheduling.
[^2608.09106]: LexKairos: Benchmarking Legal Temporal Capabilities in LLMs.
[^2608.08814]: 360CityArena: A Realistic Virtual Urban Navigation Benchmark for Embodied Agents.
[^2608.08722]: Gaming Without an Attacker: Benchmark Fingerprinting in LLM-Driven Search Under Selection Pressure.
[^2608.08634]: Can Open-Weight Models Compete on Financial Text Comprehension?
[^2608.08467]: LLM within MCP Matters: Measuring Inefficient Resource Utilization Driven by LLMs.
[^2608.08212]: Harmful Content Is Not Enough: Continuation Framing Moderates In-Context Emergent Misalignment.
[^2608.08026]: The Authority Expectancy Effect in Multi-User Conflict.
[^2608.07651]: An Agentic AI Framework Overcomes Fundamental Limitations of Large Language Models for Glaucoma Detection.
[^2608.07430]: Diffusion LLMs as Targets and Adversaries: Mechanistic Safety Exploits.
[^10.5281_zenodo.19207802]: Replication Package for Fairness Bugs Detection Empirical Study.
[^10.5281_zenodo.19207801]: Replication Package for Fairness Bugs Detection Empirical Study.
[^10.5281_zenodo.21032824]: Replication Package for Fairness Bugs Detection Empirical Study.
[^10.17613_xd840-6v157]: Moral Consistency Variance: A Pilot Benchmark for Decision Stability under Moral Prompt Perturbations in Large Language Models.
[^10.5281_zenodo.18065787]: Event Distribution in the Biblical Narrative.
[^10.5281_zenodo.19838005]: IDEAFix: An Evaluation Framework for Creative Defixation Prompting in LLMs.
[^10.5281_zenodo.19838006]: IDEAFix: An Evaluation Framework for Creative Defixation Prompting in LLMs.
[^10.5281_zenodo.21929654]: CHatGPT KABI GENERATIV SUN'IY INTELEKT TIZIMLARINING BOLALAR NUTQIY RIVOJLANISHIGA TA'SIRI.
[^10.5281_zenodo.21929653]: CHatGPT KABI GENERATIV SUN'IY INTELEKT TIZIMLARINING BOLALAR NUTQIY RIVOJLANISHIGA TA'SIRI.
[^10.32832_jpg.v7i3.24921]: Strategi Kepala Madrasah Mempertahankan Eksistensi melalui Pembelajaran Berbasis Artificial Intelligence.
[^10.4324_9781003799139-16]: Automating partnership principle assessment.
[^10.3390_bs16081405]: Beyond Ease of Use: Dynamics of Technology Adoption and Cognitive Load in AI-Assisted Programming for Non-Technical Students.
[^10.5281_zenodo.21982717]: Evaluating Thematic Drift in Long-Context LLM Dialogue via the "Whiteboard Probe".
[^10.3389_fpubh.2026.1880639]: Benchmarking publicly accessible large language models for English-language patient-facing acute pancreatitis information.
[^10.5281_zenodo.21985645]: The Heartbeat of a Live System: What Twenty-Five Consecutive Failures Taught an Instrument About Its Own Limits.
[^10.5281_zenodo.21984782]: Necronomicon.
[^10.5281_zenodo.21983225]: The Complete AI-Powered Cybersecurity Home Lab (2026–2027 Edition).
[^10.5281_zenodo.21353713]: Necronomicon.
[^10.3389_fdmed.2026.1934573]: Accuracy and response repeatability of three large language models on undergraduate operative dentistry multiple-choice questions.
[^10.5281_zenodo.21977680]: PMLRM-Bench: An Object-Centric Event Log of Large Reasoning Model Reasoning Steps for Process Mining Analysis.
[^10.5281_zenodo.21986784]: Necronomicon.
[^10.5281_zenodo.21980902]: Innovations RT GPU et Rendu Différentiable Multi-physique.
[^10.55946_latitude.v2i24.293]: AI writing assistants and their effect on EFL writing quality.
[^10.5281_zenodo.21972164]: Works for 8/16/2026 - Hunter S. Thompson.
[^10.5281_zenodo.21980903]: Innovations RT GPU et Rendu Différentiable Multi-physique.
[^10.3389_feduc.2026.1896839]: Retrieval-augmented generation for pedagogically aware educational AI.
[^10.17613_26js5-6dn28]: Stress degree and kcal analysis PRO.
[^10.20944_preprints202608.1060.v1]: Agrosensor: IoT and Edge-AI Enabled Smart Agriculture System.
[^10.5281_zenodo.21986879]: Necronomicon.
[^10.17613_atdq8-w2j55]: SIS Universal Knowledge Synthesizer and Idea Creator.
[^10.5281_zenodo.21986581]: Research data and reproducibility package for a deterministic-generative framework for auditable AI-assisted water quality monitoring.
[^10.1007_978-3-032-35579-9_19]: Let the Alerts Speak: LLM-Based IDS Alert Interpretation for SOC Triage.
[^10.5281_zenodo.21973288]: Pegi1727/Multilingual-Fairness-Framework-LLM.
[^10.17613_r8v3z-enw34]: Stress degree and kcal analysis PRO.
[^10.1038_s41746-026-03153-9]: Evaluating retrieval-augmented large language models for pediatric cardiology knowledge.
[^10.5281_zenodo.21981783]: On the Categorical Duality Across Scales.
[^10.1007_s00586-026-10280-0]: Are large language models such as ChatGPT, capable of supporting patients and general practitioners after spine surgery?
[^10.3390_su18168397]: An Enhanced RAG–LLM Framework for Decision Support in Sustainable Industrial Engineering and Management.
[^2608.27094]: An Empirical Evaluation of Using Large Language Models for Automated Model-Based Test Generation.
[^2608.26885]: Evaluating human and LLM screening workflows in a conceptually complex scoping review.
[^2608.26866]: Order Matters: A Chinese Multi-Panel Meme Benchmark for Vision-Language Reasoning.
[^2608.26701]: Accelerating Scientific Research with Gemini in the Real-World.
[^2608.26623]: AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling.
[^2608.26596]: Not Just Reason, Not Just Scan: Reinforcement Learning for Proactive Scientific Error Verification over Academic Paper.
[^2608.26291]: Assessing mentalization in humans and large language models.
[^2608.26031]: Vulnerable Code Search: Transferable Attack for Code Language Models.
[^2608.25580]: V-Rubrics: Visual Faithfulness via Rubric-Based Reinforcement Learning.
[^2608.25286]: BixBench3: Benchmarking AI agents on research-study-scale computational biology tasks.
[^2608.25022]: A Primer on Computational Semantics for Artificial Intelligence Systems.
[^2608.24291]: ReproAgent: Contract-Guided Paper-to-Code Reproduction.
[^2608.24269]: Towards LLM-Enhanced Android Taint Analysis.
[^2608.24191]: 'Ghaib in Translation' aka Unseen Harm: Measuring Cross-Script Safety Inconsistency with 'Missed-in-Urdu' Scores in LLM Hate Speech Detection.
[^2608.24113]: Structured Frequency-Domain Evidence for LLM-Based Time-Series Anomaly Detection.
[^2608.23961]: Evaluating Language Models on Cross-Language Code Functional Equivalence.
[^2608.23688]: Agentic Active Learning Meets Visual Embeddings: Finding Anomalies among 370 000 Variable Stars from ASAS-SN.
[^2608.23563]: EG-ARSA: An Expert-Grounded Open Model for Visual Road Safety Auditing in Low-Resource Settings.
[^2608.23370]: Walking on the DARKSIDE.
[^2608.23268]: Dual-Grained Agent Memory and Shapley Context Attribution for Multimodal Agentic Learner.
[^2608.23061]: Improving O-RADS Risk Stratification from Ultrasound Reports: A Comparative Evaluation of Hybrid versus End-to-End LLM Reasoning Strategies.
[^2608.22894]: AraDetox: A Multi-Dialect Arabic Detoxification Dataset.
[^2608.22808]: CatchBench: When Can an Agent Failure Be Caught?
[^2608.22529]: Benchmarking the Titans: A Multi-Dimensional Empirical Evaluation of LLM Code Generation Quality in the .NET Ecosystem.
[^2608.22331]: Noise Floor Audit for Agent Benchmarks.
[^2608.22128]: Task-Driven 3D Printability Assistance via Geometry- and Knowledge-Grounded LLM Reasoning.
[^2608.22068]: Decision-Support and Modeling with Large Language Models for Geothermal Well Arrays.
[^2608.21747]: Architecture as Capability Equalizer for Coding Agents.
[^2608.21668]: From Mastery Profile to Simulated Response: Stochastic Student Knowledge Graphs (SSKG) for Faithful LLM Student Simulation.
[^10.5281_zenodo.22005783]: AI Programming Capability Leaps at Fixed Model Scale.
[^10.5281_zenodo.22118610]: Conceptos básicos para la optimización de logística, control de inventarios y asignación de recursos con Gemini.
[^10.5281_zenodo.22115732]: Coherence Integrity for AI Systems II: Dynamic Alignment Through Four-Delusion Avoidance and Affective Engrams.
[^10.21037_qims-2026-1-0307]: Large language models for analyzing contrast-enhanced ultrasound reports of pancreatic cystic lesions.
[^10.1186_s12911-026-03784-8]: Automated extraction of key entities from non-english thorax CT reports using machine learning by large context, many-shot Generative AI.
[^10.58600_eurjther3197]: Mapping Gaps and Improvement Targets in Large Language Model-Generated Melanoma Patient Education in a Non-English Setting.
[^10.5281_zenodo.22120983]: Jarvis: AI note-taking assistant.
[^10.5281_zenodo.22128972]: Studiu longitudinal om–IA: Co-adaptare, continuitate și limitele operaționalizării semantice într-o interacțiune persistentă om–LLM.
[^10.5281_zenodo.22127914]: Multimodal Generative AI Unified Self-Care «Onkyo Protocol» of Neuro-Psychological Order and Clinical Evaluation.
[^10.5281_zenodo.22128547]: Data and code for: Is large language model-generated feedback on clinical communication skills transcripts sensitive to demographic bias? A controlled factorial audit of three commercial models.
[^10.64898_2026.08.21.26360755]: Expert-Guided Visual Correction for Characterizing Diagnostic Performance and Error Patterns of Multimodal Large Language Models Using Periodontal In-Service Examination Images.
[^10.5281_zenodo.22119042]: AI Identity Diagnostic — Deterministic Interpretation of Whole-Site Entity Graph Evidence for Machine-Readable Business Identity Assessment.
[^10.70773_revistatopicos_787807121]: VARIAÇÃO LINGUÍSTICA E INTELIGÊNCIA ARTIFICIAL: UM ESTUDO EXPLORATÓRIO DA ACOMODAÇÃO ESTILÍSTICA EM QUATRO SISTEMAS GENERATIVOS NO PORTUGUÊS BRASILEIRO.
