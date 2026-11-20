import numpy as np
import matplotlib.pyplot as plt


A = np.random.randint(0,2,size=(5,5)).astype(float)
b = np.array([100.0, 0.0, 0.0, 0.0, 20.0])


def jacobi(
    matrix: np.ndarray, values: np.ndarray, tol: float = 1e-8,
    max_iter: int = 500,
) -> tuple[np.ndarray, list[float]]:
    diagonal = np.diag(matrix)
    remainder = matrix - np.diagflat(diagonal)
    estimate = np.zeros_like(values)
    errors = []
    for _ in range(max_iter):
        new_estimate = (values - remainder @ estimate) / diagonal
        error = np.linalg.norm(new_estimate - estimate, ord=np.inf)
        errors.append(error)
        if error < tol:
            return new_estimate, errors
        estimate = new_estimate
    return estimate, errors


def gauss_seidel(
    matrix: np.ndarray, values: np.ndarray, tol: float = 1e-8,
    max_iter: int = 500,
) -> tuple[np.ndarray, list[float]]:
    estimate = np.zeros_like(values)
    errors = []
    for _ in range(max_iter):
        old_estimate = estimate.copy()
        for i in range(len(values)):
            estimate[i] = (
                values[i]
                - matrix[i, :i] @ estimate[:i]
                - matrix[i, i + 1:] @ old_estimate[i + 1:]
            ) / matrix[i, i]
        error = np.linalg.norm(estimate - old_estimate, ord=np.inf)
        errors.append(error)
        if error < tol:
            return estimate, errors
    return estimate, errors


x_jacobi, errors_jacobi = jacobi(A, b)
x_gauss_seidel, errors_gauss_seidel = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)

print("Jacobi temperatures:", x_jacobi)
print("Gauss-Seidel temperatures:", x_gauss_seidel)
print("Direct solution:", x_exact)
plt.semilogy(errors_jacobi, label="Jacobi")
plt.semilogy(errors_gauss_seidel, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Convergence of iterative temperature solution")
plt.legend()
plt.grid(True)
plt.show()
