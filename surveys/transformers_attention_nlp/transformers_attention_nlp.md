# Living Survey: transformers attention NLP

## Introduction

This document collects the scientific literature regarding **transformers attention NLP**.

## Recent Advances in Transformer Architectures and Attention Mechanisms (2019)

The year 2019 witnessed significant theoretical and practical advancements in Transformer-based models and attention mechanisms. Theoretical foundations were strengthened by work demonstrating that Transformer models act as universal approximators of continuous permutation-equivariant sequence-to-sequence functions, with fixed-width self-attention layers playing a pivotal role in computing contextual mappings [^10.48550_arxiv.1912.10077]. 

In the domain of text summarization, researchers explored novel ways to handle long-range dependencies and leverage inherent data biases. A history aggregation mechanism based on the Transformer was proposed to enhance encoder memory capacity for abstractive summarization [^10.48550_arxiv.1912.11046]. Furthermore, the exploitation of lead bias in journalistic articles enabled effective zero-shot abstractive summarization using BART and T5, yielding state-of-the-art results without fine-tuning [^10.48550_arxiv.1912.11602].

The integration of pre-trained language models into downstream tasks continued to expand. An end-to-end framework for joint named entity recognition and relation extraction was introduced, utilizing large pre-trained models to eliminate dependency on external NLP tools like dependency parsers [^10.48550_arxiv.1912.13415]. Similarly, a weakly supervised pretraining objective was developed to explicitly inject real-world knowledge into models like BERT, significantly boosting performance on fact completion and entity-related question answering [^10.48550_arxiv.1912.09637].

Attention mechanisms were also adapted for specialized and multimodal contexts. A multimodal target-source classifier with attention branches (MTCM-AB) was designed to resolve ambiguities in domestic robot fetching instructions by effectively aligning linguistic and visual inputs [^10.48550_arxiv.1912.10675]. In the clinical domain, Clinical XLNet was developed to model sequential clinical notes by leveraging temporal information, outperforming baselines in predicting prolonged mechanical ventilation [^10.48550_arxiv.1912.11975]. Additionally, attention models were successfully applied to goal-oriented dialog systems, improving intent recognition and dialog action prediction even with limited training data [^10.48550_arxiv.1912.10130].
