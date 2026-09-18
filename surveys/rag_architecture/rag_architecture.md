# Living Survey: rag_architecture

## Introduction

This document collects the scientific literature regarding **rag_architecture**.

## Knowledge Graph Integration in RAG
Recent advancements have focused on hybridizing Retrieval-Augmented Generation with Knowledge Graphs (KGs) to mitigate hallucinations and improve structural coherence in complex reasoning tasks. GraphRAG frameworks leverage the intrinsic relational nature of graphs to encode heterogeneous information, making it a golden resource for RAG applications [^10.48550_arxiv.2501.00309]. Furthermore, layered RAG pipelines that synthesize textual entity extraction, community summaries, and structural link navigation have been proposed to capture comprehensive contexts and mitigate hallucinations in knowledge-intensive domains [^10.36838_v6i12.11]. These approaches also extend to experimental software architectures that prioritize flexibility and traceability, integrating LLMs with RAG and KGs to improve management and verification of AI workflows [^10.1016_j.websem.2024.100853].

## Optimization and Filtering Mechanisms
To address the degradation of performance caused by irrelevant or noisy retrieved documents, novel filtering and scoring mechanisms have been introduced. MAIN-RAG employs a training-free, multi-agent framework that collaboratively filters and scores retrieved documents using an adaptive relevance threshold, effectively minimizing noise while maintaining high recall and improving answer accuracy across QA benchmarks [^10.48550_arxiv.2501.00332]. Additionally, optimizing the retrieval pipeline through dynamic chunking strategies and advanced vector search indices, such as FAISS HNSW combined with cross-encoder re-ranking, has proven effective in preserving contextual coherence and enhancing response fidelity without sacrificing computational efficiency [^10.56038_oprd.v5i1.516].

## Instruction Tuning for RAG
Expanding the applicability of RAG beyond limited scenarios requires diverse and high-quality instruction data. RAG-Instruct addresses this by synthesizing a comprehensive instruction dataset based on five distinct RAG paradigms and instruction simulation techniques, significantly boosting LLMs' zero-shot RAG capabilities across a wide range of tasks [^10.48550_arxiv.2501.00353]. This methodology demonstrates that structured instruction tuning can effectively enhance zero-shot RAG performance across diverse tasks.

## Human-Centered and Applied RAG
The practical deployment of RAG architectures is increasingly being evaluated through human-centered and domain-specific lenses. In scientific literature classification, RAG-enhanced LLMs have demonstrated superior accuracy over traditional supervised models, even with limited labeled data, highlighting their adaptability to specialized linguistic corpora [^10.56977_jicce.2024.22.4.280]. Moreover, in humanitarian contexts, optimizing RAG hyperparameters through multi-criteria decision-making has shown promise in reducing carbon emissions and bias while ensuring fair, equitable, and non-discriminatory responses for vulnerable populations [^10.3390_app15010325].
