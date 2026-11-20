import numpy as np


# 2x + 3y = 8 and 4x + y = 6
A = np.random.randint(0, 10, size=(2, 2)).astype(float)
b = np.random.randint(0, 10, size=(2,)).astype(float)
solution = np.linalg.solve(A, b)

print("Solution [x, y]:", solution)
print("Residual:", A @ solution - b)
