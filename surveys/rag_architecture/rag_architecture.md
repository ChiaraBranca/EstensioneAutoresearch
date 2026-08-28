# Living Survey: rag architecture

## Introduction

This document collects the scientific literature regarding **rag architecture**.

## RAG Architectures and Frameworks

Recent advancements have focused on structuring RAG systems to improve reliability, traceability, and domain specificity. The integration of Knowledge Graphs (KGs) with RAG, known as GraphRAG, has emerged as a significant area of research, addressing the limitations of conventional neural-embedding spaces by leveraging the relational nature of graph data [[10.48550_arxiv.2501.00309]]. To enhance reasoning capabilities, hybrid approaches combining layered RAG pipelines with knowledge graph synthesis have been proposed, aiming to reduce hallucinations and structural incoherence in knowledge-intensive tasks [[10.36838_v6i12.11]]. Furthermore, frameworks like MAIN-RAG utilize multi-agent filtering to dynamically adjust relevance thresholds, reducing noise and improving answer accuracy without requiring additional training [[10.48550_arxiv.2501.00332]].

## Optimization and Efficiency

Optimizing RAG systems involves balancing performance with computational and environmental costs. Research indicates that optimizing hyperparameters for LLMs and RAG can significantly reduce carbon emissions and bias, supporting human-centered AI goals [[10.3390_app15010325]]. In resource-constrained environments, EdgeRAG addresses memory limitations on edge devices by pruning embeddings and generating them on-demand, achieving latency reductions while maintaining generation quality [[10.48550_arxiv.2412.21023]]. Additionally, dynamic chunking strategies combined with optimized vector search and re-ranking have been shown to improve response fidelity and context precision in RAG systems [[10.56038_oprd.v5i1.516]].

## Domain-Specific Applications

RAG architectures are being adapted for diverse domains beyond general text generation. In materials science, agents like MOFsyn Agent use RAG to guide the synthesis of Metal-Organic Frameworks, integrating data analysis with external knowledge bases [[10.26434_chemrxiv-2024-7kds2]]. In cybersecurity, RAG is employed to secure Web Application Firewalls against SQL injection by generating and validating payloads using LLMs [[10.3390_fi17010008]]. Other applications include criminal investigation support systems that provide knowledge-based Q&A [[10.12972_jdfr.2024.1.1.4]], and power standard knowledge generation [[10.52152_4073]].

## Multimodal and Specialized RAG

The scope of RAG is expanding into multimodal and specialized data types. Enhanced Multimodal RAG-LLM frameworks introduce structured scene graphs to improve visual question answering and object recognition in complex scenes [[10.48550_arxiv.2412.20927]]. For time series forecasting, TimeRAF employs a retrieval-augmented foundation model to enhance zero-shot prediction by accessing customized knowledge bases [[10.48550_arxiv.2412.20810]]. Similarly, RAG is applied in mobile edge computing to optimize resource allocation in dynamic wireless systems [[10.48550_arxiv.2412.20820]].

## Security and Robustness

As RAG systems become more prevalent, their security and robustness are critical concerns. Research has highlighted vulnerabilities in dense embedding-based search, demonstrating that search-engine optimization (SEO) attacks can manipulate retrieval results [[10.48550_arxiv.2412.20953]]. Evaluating the faithfulness of RAG outputs is also crucial, with LLMs serving as evaluators showing high correlation with human judgment in assessing hallucinations [[10.48550_arxiv.2501.00269]].

## Instruction Tuning and Data Synthesis

To improve the general RAG capabilities of LLMs, methods like RAG-Instruct synthesize diverse instruction data covering various RAG paradigms, enabling better zero-shot performance across tasks [[10.48550_arxiv.2501.00353]]. Additionally, vector search technologies are evolving to better capture semantic meaning, transforming information retrieval in industries like healthcare and e-commerce [[10.14445_22312803_ijctt-v72i12p101]].

## Agent-Based RAG

LLM agents are increasingly integrated with RAG to handle complex, multi-step tasks. In virtual reality, conversational avatars use RAG for context-grounded responses [[10.48550_arxiv.2501.00168]]. Agents like those in the Aviary framework use LLMs to access scientific literature for research questions [[10.48550_arxiv.2412.21154]], and Plancraft evaluates LLM agents' planning capabilities using RAG for tool use [[10.48550_arxiv.2412.21033]]. Dialogue Director uses RAG to bridge the gap in dialogue visualization for storytelling [[10.48550_arxiv.2412.20725]].

## Knowledge Graph Integration

Beyond GraphRAG, specific frameworks like KARPA use knowledge graphs to assist reasoning path aggregation in LLMs, avoiding stepwise traversal and improving efficiency in knowledge graph question answering [[10.48550_arxiv.2412.20995]].
