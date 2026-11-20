import numpy as np
import matplotlib.pyplot as plt


time = np.array([0, 3, 6, 9, 12, 15, 18], dtype=float)
position = np.array([0, 3.5, 7.8, 12.1, 16.5, 21.0, 25.6], dtype=float)
speed = np.zeros_like(position)
speed[0] = (position[1] - position[0]) / (time[1] - time[0])

for i in range(1, len(time) - 1):
    speed[i] = (position[i + 1] - position[i - 1]) / (
        time[i + 1] - time[i - 1]
    )

speed[-1] = (position[-1] - position[-2]) / (
    time[-1] - time[-2]
)

for current_time, distance, velocity in zip(time, position, speed):
    print(
        f"t={current_time:.0f}s, position={distance:.1f}m, "
        f"estimated speed={velocity:.2f}m/s"
    )

plt.plot(time, speed, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Estimated speed (m/s)")
plt.title("Speed estimated from GPS position data")
plt.grid(True)
plt.show()
