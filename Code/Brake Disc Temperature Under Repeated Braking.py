# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 18:53:20 2025

@author: golde
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Material & Disc Properties
T_ambient = 100      # Ambient temperature [°C]
d = 7750             # Density [kg/m³]
Cp = 460.0           # Specific heat [J/kg·K]
Kt = 24.9 * 1000     # Thermal conductivity [W/m·K]
R = 0.08             # Radius [m]
th = 0.002           # Thickness [m]
A = 0.04             # Convective area [m²]
V = np.pi * R**2 * th
m = d * V            # Mass [kg]
h = 80               # Convective heat transfer coefficient [W/m²·K]

# Lumped system coefficient
k = (h * A) / (d * V * Cp)

# -----------------------------
# Vehicle & Braking Parameters
vehicle_mass = 1860  # kg
v0 = 25              # m/s (~90 km/h)
brake_eff = 0.7
num_discs = 2

E_kinetic = 0.5 * vehicle_mass * v0**2
Q_brake = E_kinetic * brake_eff / num_discs
delta_T_brake = Q_brake / (m * Cp)

# -----------------------------
# Repeated Braking Simulation
t_total = 180        # total simulation time [s]
dt = 0.5             # time step [s]
n_steps = int(t_total / dt)
brake_interval = 30  # braking every 30 seconds
T = T_ambient        # initial disc temperature

time_list = []
T_list = []

for i in range(n_steps):
    t = i * dt

    # Apply braking heat every 30 seconds
    if i % int(brake_interval / dt) == 0 and i != 0:
        T += delta_T_brake

    # Cooling model (Newton's Law)
    T = T_ambient + (T - T_ambient) * np.exp(-k * dt)

    # Log data
    time_list.append(t)
    T_list.append(T)

# -----------------------------
# Plotting
plt.figure(figsize=(9, 5))
plt.plot(time_list, T_list, color='red', label="Disc Temperature")
plt.title("Brake Disc Temperature Under Repeated Braking")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.axhline(y=T_ambient, color='gray', linestyle='--', label='Ambient Temp')
plt.axhline(y=350, color='orange', linestyle='--', label='Warning Temp (350°C)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
