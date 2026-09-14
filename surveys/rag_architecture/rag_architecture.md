# Living Survey: rag_architecture

## Introduction

This document collects the scientific literature regarding **rag_architecture**.

## Recent Advances in RAG Architectures

Recent literature has significantly expanded the architectural paradigms of Retrieval-Augmented Generation (RAG), focusing on hybridization, dynamic optimization, and multi-agent filtering. 

The integration of Knowledge Graphs (KGs) with RAG has emerged as a robust strategy to improve traceability and experimental repeatability in LLM workflows. By prioritizing flexibility and traceability, such architectures enable more accurate and explainable outputs, particularly when dealing with closed-access models via web APIs [^10.1016_j.websem.2024.100853]. Similarly, layered RAG pipelines that synthesize textual entity knowledge graphs, community summaries, and structural link navigation have been proposed to enhance complex LLM reasoning, capturing comprehensive context to generate well-structured responses [^10.36838_v6i12.11]. GraphRAG frameworks specifically leverage the intrinsic relational nature of graphs to encode massive heterogeneous information, addressing unique challenges in designing retrievers and organizers for domain-specific data [^10.48550_arxiv.2501.00309].

To mitigate noise and improve retrieval quality, training-free multi-agent filtering mechanisms have been introduced. MAIN-RAG dynamically adjusts relevance thresholds based on score distributions and leverages inter-agent consensus to minimize irrelevant documents while maintaining high recall, resulting in superior response consistency and accuracy [^10.48550_arxiv.2501.00332]. Furthermore, optimizing the retrieval pipeline itself through dynamic chunking for contextual coherence, combined with advanced embedding models and cross-encoder re-ranking, has proven effective in bridging the gap between large-scale language models and domain-specific information needs [^10.56038_oprd.v5i1.516].

Architectural innovations also extend to instruction tuning and token generation efficiency. RAG-Instruct synthesizes diverse instruction data across five RAG paradigms to enhance LLM capabilities in zero-shot scenarios, addressing the lack of general RAG datasets [^10.48550_arxiv.2501.00353]. On the generation side, Chunk-Distilled Language Modeling (CD-LM) combines deep networks with a retrieval module to generate multi-token text chunks in a single decoding step, improving efficiency and adaptability to new knowledge without additional training [^10.48550_arxiv.2501.00343].

Beyond core architecture, RAG systems are being optimized for specific application domains and evaluation metrics. In human-centered AI, RAG configurations are tuned via multi-criteria decision-making to ensure fairness and reduce carbon emissions while maintaining non-discriminatory responses for vulnerable populations [^10.3390_app15010325]. For automated document classification, RAG structures utilizing LLMs demonstrate high accuracy even with limited labeled data, outperforming traditional supervised models [^10.56977_jicce.2024.22.4.280]. Additionally, recent reviews emphasize that RAG frameworks, alongside advanced prompting, are critical for mitigating hallucinations and improving faithfulness in open-ended generation tasks [^10.48550_arxiv.2501.00269].
