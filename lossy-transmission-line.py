import numpy as np
import matplotlib.pyplot as plt

# Constants for lossy transmission line
V0 = 1  # Voltage amplitude (V)
alpha = 0.2  # Attenuation constant (Np/m)
beta = 2 * np.pi  # Phase constant (rad/m)
frequency = 1e3  # Frequency (Hz)
omega = 2 * np.pi * frequency  # Angular frequency (rad/s)
x = np.linspace(0, 10, 500)  # Position along the line (m)

# Time steps (4 points across one period)
T = 1 / frequency  # Period of the wave (s)
time_steps = [0, T / 4, T / 2, 3 * T / 4]  # 0, π/2, π, 3π/2 in terms of phase

# Create plots for each time step
plt.figure(figsize=(12, 8))
for idx, t in enumerate(time_steps):
    # Reverse traveling voltage wave: V(x, t)
    V = V0 * np.exp(alpha * x) * np.cos(omega * t + beta * x)
    plt.plot(x, V, label=f"t = {t:.4f} s")

# Plot formatting
plt.title("Reverse Traveling Voltage Wave on a Lossy Transmission Line")
plt.xlabel("Position along the line (x)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid()
plt.show()
