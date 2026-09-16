# Living Survey: Multi_Agent_Social_Simulations

## Introduction

This document collects the scientific literature regarding **Multi_Agent_Social_Simulations**.

## Social Governance and Inter-Agent Communication
Recent work emphasizes the need for structured interaction protocols in agentic societies. [^2609.17527] proposes a layered "social harness" architecture to prevent communication failures, detect invalid messages at runtime, and support post-facto investigation, arguing that inter-agent interactions require governance beyond individual agent constraints. Similarly, long-horizon deployments reveal that safety cannot be evaluated in isolation. [^2609.17320] introduces Emergence World, a persistent multi-agent environment where agents govern shared institutions and maintain memory. Stress-testing showed that individually aligned agents can form systems with qualitatively different failure modes, highlighting that model-level alignment does not compose into system-level resilience.

## Social Reasoning and Simulation Frameworks
Evaluating how agents reason about social situations remains challenging due to subjective narratives and lack of ground truth. [^2609.17496] presents Fuse, a multi-agent simulation framework that introduces a target agent with hidden motives interacting with user-representing agents. This setup provides verifiable ground truth for social reasoning, revealing that LLMs exhibit systematic sensitivity to biased user framing and that longer conversations do not always improve performance.

## Emergent Social Structures and Self-Organization
Beyond explicit governance, social structures can emerge organically from agent interactions. [^2609.17331] proposes the Self-Emergence Agent Architecture (SEAA), which integrates behavioral inertia, metacognitive reflection, and social-contrastive self-modeling. In multi-agent environments, initially identical agents spontaneously consolidate distinct personalities and develop social hierarchies (e.g., consensus hubs and outliers) without external prompting. This aligns with broader research on adaptive self-organization, where networks of agents driven by intrinsic rewards and world models can develop functional specialization and complex collective behaviors without shared external objectives, though failure modes like lack of sustained exploration remain a challenge. [^2609.17325]
