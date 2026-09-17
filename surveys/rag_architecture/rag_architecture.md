# Living Survey: rag_architecture

## Introduction

This document collects the scientific literature regarding **rag_architecture**.

## Recent Advances in RAG Architectures

The field of Retrieval-Augmented Generation (RAG) has seen rapid evolution in 2024, with significant strides in graph integration, multi-agent filtering, instruction tuning, and dynamic chunking.

**Graph-Enhanced and Knowledge Graph Integration**
Integrating Knowledge Graphs (KGs) with RAG has emerged as a powerful strategy to improve traceability and factual accuracy. A recent study proposes a software architecture that prioritizes flexibility and traceability by combining LLMs with RAG and KGs, demonstrating improved robustness in experimental workflows[^10.1016_j.websem.2024.100853]. Furthermore, a comprehensive survey on GraphRAG highlights the unique challenges of designing retrievers and generators in the neural-embedding space for graph-structured data, proposing a holistic framework comprising query processors, retrievers, organizers, generators, and domain-specific data sources[^10.48550_arxiv.2501.00309]. Another approach synthesizes layered RAG pipelines by extracting unstructured and structured text properties, combining textual entity KG extraction, community summaries, and structural link navigation to enhance complex reasoning tasks[^10.36838_v6i12.11].

**Multi-Agent and Filtering Mechanisms**
To address noise and irrelevant documents in retrieval, the MAIN-RAG framework introduces a training-free approach leveraging multiple LLM agents to collaboratively filter and score retrieved documents. It employs an adaptive filtering mechanism that dynamically adjusts relevance thresholds based on score distributions, achieving significant improvements in answer accuracy and consistency without requiring fine-tuning[^10.48550_arxiv.2501.00332].

**Instruction Tuning and Data Synthesis**
RAG-Instruct addresses the limitation of limited task diversity in current RAG methods by synthesizing a 40K instruction dataset from Wikipedia. It leverages five distinct RAG paradigms and instruction simulation to enhance LLMs' RAG capabilities, demonstrating strong zero-shot performance across diverse tasks[^10.48550_arxiv.2501.00353].

**Optimization of Retrieval Components**
Enhancing the retrieval phase is critical for RAG performance. A recent study investigates dynamic chunking for contextual coherence, utilizing Sentence-Transformers for embeddings and cross-encoder-based re-ranking. By integrating the FAISS HNSW index with re-ranking, the proposed architecture improves response fidelity and context precision without compromising efficiency[^10.56038_oprd.v5i1.516]. Additionally, RAG has been effectively applied to domain-specific classification tasks, such as automatically classifying scientific papers, where it outperforms traditional BERT-based models even with limited labeled data[^10.56977_jicce.2024.22.4.280].

**Evaluation and Applications**
Evaluating faithfulness remains crucial for mitigating hallucinations. A review of faithfulness metrics indicates that LLMs as evaluators correlate highly with human judgment, and both RAG and advanced prompting frameworks significantly improve faithfulness in open-ended generation[^10.48550_arxiv.2501.00269]. In practical applications, RAG has been optimized for human-centered AI, such as migrant integration systems. By tuning LLM and RAG hyperparameters using multi-criteria decision-making, researchers achieved a 20.1% reduction in carbon emissions and an 11.3% decrease in bias metrics, ensuring fair and equitable AI outputs[^10.3390_app15010325].
