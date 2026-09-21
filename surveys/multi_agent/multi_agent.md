# Living Survey: multi_agent

## Introduction

This document collects the scientific literature regarding **multi_agent**.

## Multi-Agent Architectures and Frameworks

Recent research continues to expand the architectural paradigms available for multi-agent systems, moving towards more specialized and interoperable designs. The integration of advanced computing paradigms has shown promise in optimizing multi-agent reinforcement learning (MARL); for instance, leveraging Quantum Computing and Neuromorphic Computing can efficiently explore large solution spaces and enhance safety and reliability in autonomous robotics contexts [^2408.03884]. 

In the realm of bio-robotics, evidence-grounded multi-agent systems have been developed to automate high-level design processes, combining requirement analysis, module-specific retrieval, and conflict checking to assemble biological parts and genetic circuits [^10.48550_arxiv.2608.19699]. Similarly, state-machine-based architectures are being applied to complex diagnostic reasoning, where multiple agents analyze questions from different professional perspectives, discuss evidence, and vote on answers to improve transparency and accuracy in medical AI [^10.3390_math14142562].

Interoperability across different decision-making paradigms remains a significant challenge. The MOSAIC platform addresses this by introducing an IPC-based worker protocol and an operator abstraction that allows heterogeneous agents (RL policies, LLMs, VLMs, and humans) to act within shared reinforcement learning environments [^https:__openalex.org_W7133365089]. Hierarchical frameworks also continue to evolve, as demonstrated by Project Synapse, which employs a central Resolution Supervisor agent to delegate tactical execution to specialized worker agents for resolving last-mile delivery disruptions [^https:__openalex.org_W7124227974].

Furthermore, multi-agent LLM architectures are proving effective for automated front-end generation, coordinating generation, validation, and repair through supervisor, hierarchical, and custom workflow strategies to synthesize complete React applications from design artifacts [^https:__openalex.org_W7166959618]. Conversational multi-agent frameworks are being utilized to evaluate prompts across different LLM families, surfacing strengths and weaknesses more effectively than single-model testing [^10.5120_ijca2025925510].

## Safety, Trust, and Governance in Multi-Agent Systems

As multi-agent systems become more autonomous and interconnected, ensuring their safety, trustworthiness, and proper governance has emerged as a critical research area. The concept of an Internet of Agents (IoA) introduces systemic safety risks that require co-designing safety with capability. Research in this domain provides a principled guide for engineering safe agentic systems by analyzing vulnerabilities at the single-agent, multi-agent, and interoperable ecosystem levels [^10.48550_arxiv.2512.00520].

Trust quantification is another vital component. Information-theoretic approaches have been applied to quantify trust in multi-agent cooperative navigation environments, providing a mathematical foundation for evaluating agent reliability under various deception types [^10.6084_m9.figshare.32101069]. 

On the governance front, formal specifications like the Agent Trust Fabric (ATF) are establishing cognitive governance layers. These frameworks introduce counterfactual governance engines to record alternative decision paths, universal governance invariants to cross-reference multiple regulatory standards, and temporal governance bridges to maintain interpretability across long regulatory review cycles [^10.5281_zenodo.20391722].

## Debugging, Evaluation, and Error Attribution

The complexity of multi-agent interactions makes debugging and error attribution particularly challenging. Traditional evaluation methods often struggle with complex reasoning errors and interdependencies. The ECHO algorithm addresses this by combining hierarchical context representation, objective analysis, and consensus voting to accurately pinpoint agent and step-level failures in interaction traces [^10.48550_arxiv.2510.04886].

In systems engineering, multi-agent frameworks are also being deployed for root-cause diagnosis of kernel crashes. These systems utilize evidence graphs and automated pipelines to process log data and identify failure origins, significantly reducing manual debugging efforts [^10.5281_zenodo.19247220].

## Application Domains

Multi-agent systems are increasingly being adapted to solve domain-specific challenges that require distributed processing and specialized agent roles. In academic administration, automated categorization and multi-agent processing pipelines have been implemented to streamline assignment grading in computer science and statistics departments. By clustering similar responses and generating precise feedback, these systems reduce educator workload while maintaining rigorous evaluation standards [^10.54254_2755-2721_2025.30694].
