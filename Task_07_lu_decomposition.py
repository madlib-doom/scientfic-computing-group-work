import numpy as np
from scipy.linalg import lu, solve_triangular


A = np.random.randint(0, 10, size=(3, 3)).astype(float)
b = np.array([1.0, -2.0, 0.0])

P, L, U = lu(A)
intermediate = solve_triangular(L, P @ b, lower=True, unit_diagonal=True)
solution = solve_triangular(U, intermediate)

print("P matrix:\n", P)
print("L matrix:\n", L)
print("U matrix:\n", U)
print("Solution:", solution)
print("Residual:", A @ solution - b)
