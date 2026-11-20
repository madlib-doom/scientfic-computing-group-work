import numpy as np
from scipy.integrate import simpson
# Smart-meter readings taken every two hours
time_hours = np.array([1, 3, 5, 7, 9, 11, 13], dtype=float)
power_kw = np.array([1.0, 1.5, 2.0, 1.8, 1.2, 0.8, 0.5], dtype=float)
energy_trapezoid = np.trapezoid(power_kw, time_hours)
energy_simpson = simpson(power_kw, x=time_hours)
print(f"Energy using trapezoidal rule: {energy_trapezoid:.3f} kWh")
print(f"Energy using Simpson's rule: {energy_simpson:.3f} kWh")
print(f"Difference between estimates: {abs(energy_simpson-energy_trapezoid):.3f}kWh")
