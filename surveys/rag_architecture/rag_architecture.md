# Living Survey: rag_architecture

## Introduction

This document collects the scientific literature regarding **rag_architecture**.

## GraphRAG and Knowledge Graph Integration

The integration of Knowledge Graphs (KGs) with Retrieval-Augmented Generation has emerged as a powerful paradigm to enhance structural coherence and reduce hallucinations in knowledge-intensive tasks. Recent work proposes a holistic GraphRAG framework that defines key components including query processors, retrievers, organizers, and generators, tailored to domain-specific relational patterns[^10.48550_arxiv.2501.00309]. Furthermore, hybrid approaches that layer Textual Entity RAG, community summary generation, and structural link navigation have been shown to capture comprehensive contexts, enabling well-structured responses that reflect all relevant text attributes[^10.36838_v6i12.11]. Architectural designs that prioritize flexibility and traceability by integrating LLMs with RAG and KGs also demonstrate improved experiment management and verification capabilities[^10.1016_j.websem.2024.100853].

## Multi-Agent and Filtering Mechanisms

To address the degradation of performance caused by noisy or irrelevant retrieved documents, multi-agent filtering architectures have been introduced. The MAIN-RAG framework leverages multiple LLM agents to collaboratively filter and score retrieved documents without requiring additional training data. It employs an adaptive filtering mechanism that dynamically adjusts relevance thresholds based on score distributions, utilizing inter-agent consensus to ensure robust document selection and improve answer accuracy[^10.48550_arxiv.2501.00332].

## Instruction Tuning and Data Synthesis

Advancements in RAG architectures also focus on enhancing model capabilities through diverse instruction data. The RAG-Instruct method synthesizes high-quality instruction datasets covering various RAG paradigms and query-document relationships. By leveraging instruction simulation, this approach significantly boosts LLMs' zero-shot RAG performance across diverse tasks, addressing the limitation of scarce general RAG datasets[^10.48550_arxiv.2501.00353]. Additionally, retrieval frameworks that combine deep network-based LLMs with flexible retrieval modules allow for the generation of multi-token text chunks at single decoding steps, enabling flexible datastore construction and enhanced control over model distributions without extensive retraining[^10.48550_arxiv.2501.00343].

## Retrieval Optimization and Chunking Strategies

Optimizing the retrieval component is critical for RAG system fidelity. Research highlights the significant impact of index choice and retrieval refinement techniques. A proposed architecture integrating dynamic chunking for contextual coherence, Sentence-Transformers for high-quality embeddings, and cross-encoder-based re-ranking demonstrates that combining FAISS HNSW indexes with re-ranking improves response fidelity without compromising efficiency[^10.56038_oprd.v5i1.516]. These optimizations bridge the gap between large-scale language models and domain-specific information needs.

## Domain-Specific and Human-Centered Applications

RAG architectures are increasingly being adapted for specialized domains and human-centered AI applications. In materials science, frameworks like MOFsyn Agent utilize RAG to access external knowledge bases in real-time, guiding data analysis and synthesis optimization through natural language commands[^10.26434_chemrxiv-2024-7kds2]. In the social domain, human-centered AI systems leverage RAG to bridge gaps for vulnerable populations, such as migrants and refugees, by integrating legislative and regulatory corpora. Multi-criteria decision-making methods are employed to optimize RAG hyperparameters, ensuring fair, equitable, and non-discriminatory outputs while reducing carbon emissions[^10.3390_app15010325]. Furthermore, RAG is being explored to support automated implementation generation for open-ended problems, moving beyond static domain knowledge to handle problem framing and advanced assessment[^10.48550_arxiv.2501.00562].

## Evaluation and Faithfulness Metrics

Evaluating RAG systems requires robust metrics to assess faithfulness and mitigate hallucinations. Reviews of faithfulness metrics indicate that LLM-based evaluators are highly correlated with human judgment, with both RAG and advanced prompting frameworks showing superior faithfulness in open-ended generation tasks[^10.48550_arxiv.2501.00269]. Additionally, RAG architectures are being applied to automate document classification tasks, demonstrating that systems utilizing LLMs and RAG can achieve high accuracy even with limited labeled data, outperforming traditional supervised learning models[^10.56977_jicce.2024.22.4.280].
