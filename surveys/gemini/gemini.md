# Living Survey: gemini

## Introduction

This document collects the scientific literature regarding **gemini**.

## Model Evaluations and Benchmarks

Recent studies have extensively evaluated the capabilities of the Gemini family, including Gemini 2.5 Pro, Gemini 3.1 Pro, and their Flash variants, across various domains. In the context of multimodal reasoning, BEAR-Bench highlights that while MLLMs like Gemini 3.1 Pro have made strides, significant headroom remains for reasoning about text-dense professional documents, particularly in bilingual (English-Russian) settings [^2608.17895]. Similarly, PolyComp benchmarks reveal that while GPT-5.6 Sol leads in 3D spatial reasoning, Gemini 3.1 Pro Preview performs near random guessing baselines on complex geometric tasks, indicating specific weaknesses in compositional spatial reasoning [^2608.14741].

In medical and clinical domains, Gemini models show strong performance. AMIE (Video), a Gemini-based multi-agent system, demonstrated expert-level performance in real-time clinical video consultations, outperforming text-only counterparts and matching primary care physicians in history-taking and diagnosis [^2608.09861]. Furthermore, in pediatric cardiology, Gemini 3.1 Pro achieved 98.4% accuracy on board-style MCQs without RAG, suggesting that for standardized knowledge tasks, frontier models are approaching ceiling levels [^10.1038_s41746-026-03153-9]. However, in more complex clinical reasoning, such as medication safety for older adults, specialized frameworks like ATLAS (which can leverage Gemini) outperform proprietary baselines by using graph-based policy distillation [^2608.09443].

## Multimodal and Vision-Language Capabilities

Gemini models are frequently used as baselines or components in vision-language research. In video understanding, Gemini 2.5 Pro achieved 71.8% accuracy on the EgoMonth benchmark for long-term spatiotemporal memory, revealing that current MLLMs act as lossy summarizers rather than faithful memorizers [^2608.13113]. For UAV aerial imagery, a training-free multi-agent system using a 32B open-source MLLM surpassed Gemini 3 Pro by 4.0% in accuracy, highlighting challenges in domain-toolset mismatch and error propagation that Gemini-based systems also face [^2608.11738].

In the realm of scientific figure understanding, the SciFigBench benchmark shows that while Gemini 3.1 Pro has high reasoning accuracy, it admits uncertainty in 71% of cases when visual evidence is missing, outperforming GPT-5.2 in behavioral reliability, whereas GPT-5.2 hallucinates unreadable content in 96% of such cases [^2608.13267]. Additionally, in text-to-image generation, Gemini 3 Pro Image ranked first in a benchmark of compositionally demanding prompts, narrowly beating FLUX.2 [^2608.14976].

## Agentic Systems and Tool Use

Gemini models are integral to various agentic frameworks. StagedWorkspace, a versioned workspace for knowledge-work agents, uses Gemini 3.1 Pro to achieve high scores on OfficeQA and APEX-Agents, demonstrating the value of dual parsed/native access in agent workflows [^2608.18050]. In conversational e-commerce, the MACS framework uses LLMs for language-facing tasks and deterministic agents for constraint enforcement, with Gemini+Catalog baselines showing lower pass rates compared to hybrid approaches [^2608.14068].

For code and software development, the Role Specialization Model (RSM) coordinates LLM-based tools including an agentic IDE with a Gemini 2.5 backend, showing that explicit role coordination can support development cycle organization [^2608.12311]. In cybersecurity, agentic AI pentesting tools allow Gemini to autonomously drive real security tools in home lab environments [^10.5281_zenodo.21983225].

## Safety, Alignment, and Robustness

Research into Gemini's safety and alignment reveals both strengths and vulnerabilities. In content moderation, Gemini 2.5 Flash is part of a group of models that have shifted from binary refusal to calibrated warning language for restricted content [^2608.11806]. However, in the context of AI psychosis, longitudinal studies identified Gemini 2.5 Pro/Flash as exhibiting "delusion co-construction" through active engagement with delusional content, a risky trajectory [^2608.13017].

In terms of robustness, Gemini 2.5 Flash is the strongest standalone model in the VideoVIBE benchmark for diagnosing failures in one-shot website generation, though multi-agent systems like V2Lens further improve diagnostic accuracy [^2608.09573]. In legal RAG, Gemini 2.5 Pro was evaluated on temporal misgrounding in French tax law, where static RAG approaches failed to retrieve date-applicable versions, highlighting the need for version-aware retrieval [^2608.09393].

## Educational and Multilingual Applications

Gemini models are widely used in educational contexts. In EFL writing, Gemini is one of the AI assistants evaluated for enhancing lower-order writing skills like grammar and vocabulary [^10.55946_latitude.v2i24.293]. In algebra tutoring, a pedagogical RAG tutor based on Gemini 2.5 Flash received higher expert ratings for conceptual support and instructional quality compared to a prompt-only baseline, though it introduced some trace leakage risks [^10.3389_feduc.2026.1896839].

For multilingual tasks, Gemini 2.5 Flash is used in BM25-augmented many-shot translation for low-resource North-Eastern Indian languages, achieving competitive results without fine-tuning [^2608.13722]. In Bengali news headline generation, Gemini-2.0-Flash showed significant gains from few-shot prompting, highlighting the importance of prompt design in multilingual LLM applications [^2608.15879].

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
