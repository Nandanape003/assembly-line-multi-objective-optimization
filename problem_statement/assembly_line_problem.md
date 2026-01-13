# Assembly Line Multi-Objective Optimization – Problem Statement

## Background
In modern manufacturing systems, assembly lines operate machines under varying conditions such as temperature, speed, torque, and tool usage. Continuous operation under these conditions can lead to machine failures, increased tool wear, and reduced production efficiency.

The AI4I 2020 Predictive Maintenance dataset contains real-world sensor data collected from industrial machines, representing operating conditions in an assembly line environment.

---

## Problem Description
Manufacturers aim to improve production efficiency while reducing machine failures and maintenance costs. However, these goals are conflicting in nature. Increasing machine speed may improve productivity but can increase tool wear and the probability of machine failure. Similarly, reducing failures may require conservative operating conditions that reduce output.

Therefore, optimizing the assembly line requires balancing multiple conflicting objectives.

---

## Objectives
The objectives of this study are:

1. Maximize production efficiency (represented using rotational speed)
2. Minimize machine failure occurrences
3. Minimize tool wear to reduce maintenance and downtime

---

## Optimization Approach
This problem is formulated as a multi-objective optimization problem. Techniques such as Pareto front analysis, weighted sum method, epsilon-constraint method, and knee point analysis are used to identify optimal trade-off solutions.

---

## Expected Outcome
The result of this study is a set of Pareto-optimal solutions that help decision-makers select optimal operating conditions for the assembly line based on their priorities.

