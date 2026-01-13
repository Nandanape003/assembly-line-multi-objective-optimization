import numpy as np


def find_knee_point(pareto_F):
    utopia = np.min(pareto_F, axis=0)
    distances = np.linalg.norm(pareto_F - utopia, axis=1)
    return pareto_F[np.argmin(distances)]

