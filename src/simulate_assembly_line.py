import pandas as pd
import numpy as np
from pathlib import Path

from pareto_front import is_pareto_efficient
from knee_point_analysis import find_knee_point
from weighted_sum_method import weighted_sum_method
from epsilon_constraint_method import epsilon_constraint_method
from visualization import (
    plot_pareto,
    plot_knee_point,
    plot_weighted_sum,
    plot_epsilon_constraint
)



def load_data():
    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / "ai4i2020.csv"

    df = pd.read_csv(file_path)

    df = df.drop(columns=["UDI", "Product ID", "Type"])

    # objectives
    f1 = -df["Rotational speed [rpm]"].values   # maximize throughput
    f2 = df["Tool wear [min]"].values           # minimize defect
    f3 = df["Torque [Nm]"].values               # minimize energy

    F = np.column_stack([f1, f2, f3])
    return F



def main():
    F = load_data()

    F_2d = F[:, :2]

    # Pareto front
    pareto_mask = is_pareto_efficient(F_2d)
    pareto_F = F_2d[pareto_mask]

    # Knee point
    knee_point = find_knee_point(pareto_F)

    # Multi-objective methods
    ws_solutions = weighted_sum_method(F_2d)
    eps_solutions = epsilon_constraint_method(F_2d)

    # Plots
    plot_pareto(F_2d, pareto_F)
    plot_knee_point(pareto_F, knee_point)
    plot_weighted_sum(pareto_F, ws_solutions)
    plot_epsilon_constraint(pareto_F, eps_solutions)


if __name__ == "__main__":
    main()
