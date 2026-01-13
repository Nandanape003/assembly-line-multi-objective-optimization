import numpy as np


def weighted_sum_method(F, steps=20):
    solutions = []
    weights = np.linspace(0, 1, steps)

    for w in weights:
        score = w * F[:, 0] + (1 - w) * F[:, 1]
        idx = np.argmin(score)
        solutions.append([F[idx, 0], F[idx, 1]])

    return np.array(solutions)
