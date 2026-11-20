import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, interp1d


hours = np.array([8, 9, 13,16,17,20], dtype=float)
temperature = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5], dtype=float)
linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)
ten_minute_times = np.arange(8, 14 + 1 / 6, 1 / 6)
linear_estimates = linear(ten_minute_times)
cubic_estimates = cubic(ten_minute_times)
target_time = 10.5

print(f"Linear estimate at 10:30: {float(linear(target_time)):.2f} C")
print(f"Cubic estimate at 10:30: {float(cubic(target_time)):.2f} C")
plt.scatter(hours, temperature, label="Hourly measurements")
plt.plot(ten_minute_times, linear_estimates, label="Linear")
plt.plot(ten_minute_times, cubic_estimates, label="Cubic spline")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (C)")
plt.title("Temperature interpolation")
plt.legend()
plt.grid(True)
plt.show()
