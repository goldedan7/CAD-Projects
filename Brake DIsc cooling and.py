# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 18:49:27 2025

@author: golde
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Basic Parameters
T_ambient = 100      # Ambient temperature [°C]
T0 = 400             # Initial disc temperature [°C] (e.g., after braking)
d = 7750             # Density of AISI 420 stainless steel [kg/m³]
Cp = 460.0           # Specific heat capacity [J/kg·K]
Kt = 24.9 * 1000     # Thermal conductivity [W/m·K] (converted from kW)
R = 0.08             # Disc radius [m]
th = 0.002           # Disc thickness [m]
A = 0.04             # Convective surface area [m²]
V = np.pi * R**2 * th  # Volume of disc [m³]
m = d * V            # Mass of disc [kg]
h = 80               # Convective heat transfer coefficient [W/m²·K]

# Lumped system cooling constant (Newtons Cooling)
k = (h * A) / (d * V * Cp)

# -----------------------------
# 1. Cooling Curve Calculation
time = np.linspace(0, 60, 100)  # Time range: 0 to 60 seconds
T_cooling = T_ambient + (T0 - T_ambient) * np.exp(-k * time)  # Exponential cooling

# -----------------------------
# 2. Braking Heat Load Estimation

vehicle_mass = 1860   # Vehicle mass [kg]
v0 = 25               # Initial velocity [m/s] (~90 km/h)
brake_eff = 0.7       # Brake energy conversion efficiency
num_discs = 2         # Number of brake discs on the vehicle

E_kinetic = 0.5 * vehicle_mass * v0**2  # Total kinetic energy [J]
Q_total = E_kinetic * brake_eff / num_discs  # Heat absorbed by one disc [J]

# Temperature rise due to braking
delta_T = Q_total / (m * Cp)  # Temperature increase [K]
T_peak = T_ambient + delta_T

print(f"[Braking Heat] Heat per disc: {Q_total:.2f} J")
print(f"[Temperature Rise] ΔT = {delta_T:.2f}°C → Peak T = {T_peak:.2f}°C")

# -----------------------------
# 3. Thermal Stress Estimation

alpha = 1.1e-5    # Coefficient of thermal expansion [1/K]
E = 200e9         # Young's modulus [Pa]
nu = 0.3          # Poisson's ratio

# Approximate thermal stress for fixed disc (flat plate assumption)
sigma_th = E * alpha * delta_T / (1 - nu)  # Thermal stress [Pa]
print(f"[Thermal Stress] σ_th = {sigma_th/1e6:.2f} MPa")

# -----------------------------
# 4. Plotting Cooling Curve with Peak Temp

plt.figure(figsize=(8, 5))
plt.plot(time, T_cooling, label="Cooling Curve", color='red')
plt.axhline(y=T_peak, linestyle='--', color='orange', label='Peak Temp (Braking)')
plt.title("Brake Disc Cooling & Thermal Load")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
