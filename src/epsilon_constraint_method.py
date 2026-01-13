import numpy as np


def epsilon_constraint_method(F, steps=30):
    solutions = []
    eps_values = np.linspace(F[:, 1].min(), F[:, 1].max(), steps)

    for eps in eps_values:
        feasible = F[F[:, 1] <= eps]
        if len(feasible) > 0:
            best = feasible[np.argmin(feasible[:, 0])]
            solutions.append([best[0], best[1]])

    return np.array(solutions)
