# Data Folder

This project uses the AI4I 2020 Predictive Maintenance Dataset, which contains sensor-level and operational measurements collected from an industrial manufacturing process. The dataset represents realistic machine operating conditions and is suitable for analyzing production efficiency, quality degradation, and operational cost trade-offs.

Each row in the dataset corresponds to one production instance observed from an assembly line machine.

Complete List of Dataset Variables
Identification and Product Information

UDI: Unique identifier of each observation

Product ID: Identifier assigned to the manufactured product

Type: Product quality category (L – Low, M – Medium, H – High)

Environmental and Process Measurements

Air temperature [K]: Ambient air temperature surrounding the machine

Process temperature [K]: Temperature during the production process

Rotational speed [rpm]: Rotational speed of the machine spindle

Torque [Nm]: Mechanical torque applied during operation

Tool wear [min]: Accumulated tool usage time in minutes

Failure and Quality Indicators

Machine failure: Overall failure indicator (1 = failure, 0 = normal operation)

TWF: Tool wear failure indicator

HDF: Heat dissipation failure indicator

PWF: Power failure indicator

OSF: Overstrain failure indicator

RNF: Random failure indicator

Variables Used in This Project

During preprocessing, only the variables directly contributing to optimization objectives are retained.

Used Variables

Rotational speed [rpm]

Tool wear [min]

Torque [Nm]


Objective Function Formulation

The multi-objective optimization problem is defined as:

f₁(x) = − Rotational speed [rpm]
(Throughput maximization converted into a minimization problem)

f₂(x) = Tool wear [min]
(Defect rate proxy to be minimized)

f₃(x) = Torque [Nm]
(Energy consumption / operating cost to be minimized)

This formulation enables the study of trade-offs between productivity, quality degradation, and operating cost.

Role of the Dataset in This Project

The dataset is used to:

Represent realistic assembly line operating conditions

Generate feasible solutions for multi-objective optimization

Compute Pareto-optimal solutions

Support analysis using weighted sum, ε-constraint, and knee point methods

All optimization results and visualizations in the outputs directory are derived using this dataset.