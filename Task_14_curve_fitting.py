import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


users = np.array([50, 100, 200,300,400,500,600,700], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305, 380], dtype=float)


def model(x: np.ndarray, a: float, b: float, c: float) -> np.ndarray:
    return a * x**2 + b * x + c


parameters, _ = curve_fit(model, users, response_ms)
a, b, c = parameters
predicted = model(users, a, b, c)
rmse = np.sqrt(np.mean((response_ms - predicted) ** 2))

print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Predicted response at 400 users: {model(400, a, b, c):.2f} ms")
x_plot = np.linspace(users.min(), 400, 300)
plt.scatter(users, response_ms, label="Measurements")
plt.plot(x_plot, model(x_plot, a, b, c), label="Fitted curve")
plt.xlabel("Concurrent users")
plt.ylabel("Response time (ms)")
plt.title("Server response-time curve fitting")
plt.legend()
plt.grid(True)
plt.show()
