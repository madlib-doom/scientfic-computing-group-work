import numpy as np
from scipy.optimize import root


def equations(values: np.ndarray) -> np.ndarray:
    x, y = values
    return np.array([
        x**2 + y**2 - 25,
        x - y - 1,
    ])


solution = root(equations, x0=[2.0, 5.0])

print("Solver success:", solution.success)
print("Solution [x, y]:", solution.x)
print("Residual:", equations(solution.x))
