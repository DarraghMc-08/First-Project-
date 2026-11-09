import numpy as np
import matplotlib.pyplot as plt

V0 = 10  # volts
R = 1000  # ohms
C = 100e-6  # farads

tau = R * C
time = np.linspace(0, 5 * tau, 500)

voltage = V0 * np.exp(-time / tau)
current = voltage / R

fig, (ax_voltage, ax_current) = plt.subplots(1, 2)

ax_voltage.plot(time, voltage)
ax_voltage.set_title("Voltage vs Time")
ax_voltage.set_xlabel("Time (s)")
ax_voltage.set_ylabel("Voltage (V)")
ax_voltage.grid(True)

ax_current.plot(time, current)
ax_current.set_title("Current vs Time")
ax_current.set_xlabel("Time (s)")
ax_current.set_ylabel("Current (A)")
ax_current.grid(True)

plt.tight_layout()
plt.show()

