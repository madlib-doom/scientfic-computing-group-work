import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar


def heat_balance(temperature: float | np.ndarray) -> float | np.ndarray:
    return temperature - 25 - 10 * np.exp(-temperature / 20)


solution = root_scalar(
    heat_balance,
    bracket=[20, 40],
    method="bisect",
    xtol=1e-10,
)


def fixed_point(temperature: float | np.ndarray) -> float | np.ndarray:
    return 25 + 10 * np.exp(-temperature / 20)


temperature = 31.9
history = [temperature]
for _ in range(500):
    new_temperature = fixed_point(temperature)
    history.append(new_temperature)
    if abs(new_temperature - temperature) < 1e-10:
        break
    temperature = new_temperature

print(f"Bisection equilibrium temperature: {solution.root:.6f} C")
print(f"Fixed-point equilibrium temperature: {history[-1]:.6f} C")
print("Fixed-point iterations:", len(history) - 1)

temperatures = np.linspace(20, 40, 300)
plt.plot(temperatures, heat_balance(temperatures))
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--")
plt.xlabel("Temperature (C)")
plt.ylabel("Heat-balance function")
plt.title("Equilibrium temperature")
plt.grid(True)
plt.show()
