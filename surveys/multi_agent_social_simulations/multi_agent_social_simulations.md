# Living Survey: Multi_Agent_Social_Simulations

## Introduction

This document collects the scientific literature regarding **Multi_Agent_Social_Simulations**.

## Multi-Agent Coordination and Social Dynamics

Research into multi-agent coordination has increasingly focused on formalizing social constraints within stochastic environments. Recent work extends the concept of social laws beyond deterministic settings to reward-based stochastic systems, introducing $\alpha$-robustness to measure guaranteed utility retention while agents pursue optimal policies under social laws [^2609.18929]. This formalism enables robustness verification through a reduction to Markov decision processes, providing a mathematical foundation for predicting collective outcomes in complex social simulations.

## Swarm Intelligence and Collective Belief Formation

Understanding emergent behaviors in large-scale agent populations remains a critical challenge for social simulations. The Flag Game introduces a toy model for mechanistic swarm interpretability, demonstrating how bounded agents with private observations can form collective beliefs through peer communication [^2609.19124]. The study reveals non-monotonic scaling of performance with population size, identifying a transition from collective belief collapse at small scales to polarization at larger scales, while also noting accuracy gains from social-awareness prompting and strong effects of organizational structure. Complementing this, simulations of aerial swarms highlight the importance of interface design in human-agent teaming, showing that body-motion control interfaces can significantly reduce navigation completion times and increase path directness in simulated 3D obstacle courses, albeit at the cost of higher physical demand [^2609.18881].

## Multi-Agent Communication and Pathfinding

Efficient communication and spatial coordination are foundational to functional multi-agent systems. Evaluations of paired frontier models in information-asymmetric games reveal that communication efficiency scales predictably with document set size, following a reliability parameter that dictates win rates across $\log_2 N$ questioning rounds [^2609.19113]. Furthermore, theoretical advances in Transient Multiagent Pathfinding establish fixed-parameter tractability for routing agents without collisions, parameterized by the gap between the sum of shortest-path distances and the target makespan, alongside the number of agents [^2609.18820]. These findings provide essential algorithmic guarantees for simulating large-scale agent interactions in constrained environments.
