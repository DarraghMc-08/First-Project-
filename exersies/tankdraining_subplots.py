import numpy as np
import matplotlib.pyplot as plt

rho = 1000  # kg/m^3
g = 9.81  # m/s^2

h = np.linspace(0, 10, 100)  # depth in metres
v = np.sqrt(2 * g * h)  # outlet velocity in m/s
pressure_kpa = rho * g * h / 1000  # bottom pressure in kPa

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(h, v, color="green")
axes[0].set_xlabel("Depth (m)")
axes[0].set_ylabel("Outlet velocity (m/s)")
axes[0].set_title("Outlet Velocity vs Depth")
axes[0].grid(True)

axes[1].plot(h, pressure_kpa, color="blue")
axes[1].set_xlabel("Depth (m)")
axes[1].set_ylabel("Bottom pressure (kPa)")
axes[1].set_title("Bottom Pressure vs Depth")
axes[1].grid(True)

plt.tight_layout()
plt.show()
