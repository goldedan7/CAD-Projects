# 🚗 Disc Brake Thermal Simulation Project

This project models the thermal behavior of a vehicle's disc brake system under repeated braking conditions. The simulation uses Python to estimate temperature rise from braking events and cooling behavior using Newton's Law of Cooling. It also evaluates thermal stress on the disc based on estimated temperature gradients.

---

## 📌 Project Goals

- Estimate temperature rise due to braking heat
- Model disc cooling with Newtonian cooling
- Visualize repeated braking cycles
- Calculate thermal stresses using mechanical properties

---

## 📂 Repository Contents

```
.
├── disc_brake_simulation.py       # Full simulation: braking + cooling over time
├── disc_brake_single_event.py     # Braking heat + single cooling curve + stress calc
├── images/
│   ├── cooling_curve.png
│   └── repeated_braking.png
├── README.md                      # This file
```

---

## 📊 Key Parameters

| Property | Value |
|----------|-------|
| Material | AISI 420 Stainless Steel |
| Disc Radius | 0.08 m |
| Thickness | 2 mm |
| Vehicle Mass | 1860 kg |
| Initial Speed | 25 m/s (90 km/h) |
| Specific Heat | 460 J/kg·K |
| Heat Transfer Coeff. | 80 W/m²·K |

---

## 🔥 Braking Heat Load

```python
E_kinetic = 0.5 * vehicle_mass * v0**2
Q_brake = E_kinetic * brake_eff / num_discs
delta_T = Q_brake / (m * Cp)
```

- Resulting disc temperature rise per brake: **~167°C**

---

## ❄️ Cooling Curve

```python
T = T_ambient + (T - T_ambient) * np.exp(-k * time)
```

- Exponential decay due to convective cooling

![Cooling Curve]([Images/Brake_Disc_Cooling_graph.png](https://github.com/goldedan7/CAD-Projects/blob/main/Images/Brake%20Disc%20cooling%20graph.png))


---

## 🔁 Repeated Braking Simulation

Braking occurs every 30 seconds. Each event increases the disc's temperature before cooling resumes.

![Repeated Braking]([Images/Brake_Disc_Temperature_Under_Repeated_Braking_Graph.png](https://github.com/goldedan7/CAD-Projects/blob/main/Images/Brake%20Disc%20Temperature%20Under%20Repeated%20Braking%20Graph.png))

---

## 🧠 Thermal Stress Estimation

Thermal stress is estimated using:

```python
sigma_th = E * alpha * delta_T / (1 - nu)
```

- Approximate peak stress: **~218 MPa**
- Assumes clamped flat disc condition (worst-case)

---

## ✅ Conclusion

This project demonstrates how a simplified lumped-parameter thermal model can be used to:

- Predict temperature behavior of brake discs
- Understand cooling time needed between braking cycles
- Estimate thermal stress under transient heat load

---

## 📘 Future Extensions

- 🔄 Integrate FEA analysis using Fusion 360
- 📈 Compare with experimental data or datasheets
- 💨 Add airflow dynamics for enhanced convective cooling
- 🧱 Structural deformation modeling (Fusion, Abaqus)

---

## 🔗 Author

**Changhyeon Lee**  
Mechanical Engineering, University of Bristol  
📧 golde0715@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/changhyeon-lee-329685232)

---

## 🌐 GitHub Pages Portfolio
You can view the online version of this project [**here**](https://yourusername.github.io/disc-brake-simulation). *(Replace with actual link)*
