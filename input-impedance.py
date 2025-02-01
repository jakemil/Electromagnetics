import matplotlib.pyplot as plt
import numpy as np

characteristic_impedance = 50
load_impedance = 25 + 25j


# Function to calculate the input impedance
def input_impedance(characteristic, load, length):
    return (characteristic * (load + 1j * characteristic * np.tan(2 * np.pi * length))) / (
            characteristic + load * 1j * np.tan(2 * np.pi * length)
    )

#overlook this is just for a hw problem
print(input_impedance(50, 20-35j, -0.3))


# Define parameters
start_value = 0
end_value = 0.45
num_points = 1000000  # Number of points to sample

length_values = np.linspace(start_value, end_value, num_points)
y_values = input_impedance(characteristic_impedance, load_impedance, length_values)

# Extract real and imaginary parts for complex plane visualization
real_parts = np.real(y_values)
imag_parts = np.imag(y_values)

# Find points where the imaginary part equals zero
zero_imag_indices = np.isclose(imag_parts, 0, atol=1e-2)  # Tolerance for floating-point precision
zero_imag_lengths = length_values[zero_imag_indices]
zero_imag_points_real = real_parts[zero_imag_indices]
#print(zero_imag_points_real)
zero_imag_points_imag = imag_parts[zero_imag_indices]
#print(zero_imag_points_imag)

# Plot the results on the complex plane
plt.figure(figsize=(8, 6))
plt.plot(real_parts, imag_parts, label="Input Impedance (Z_in)", color="blue")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")

# Annotate the starting point
plt.annotate(f"Length = {length_values[0]:.2f}",
             (real_parts[0], imag_parts[0]),
             textcoords="offset points", xytext=(-30, 10),
             arrowprops=dict(arrowstyle="->", color="green", lw=1.5),
             fontsize=10, color="green")

# Annotate the ending point
plt.annotate(f"Length = {length_values[-1]:.2f}",
             (real_parts[-1], imag_parts[-1]),
             textcoords="offset points", xytext=(-30, -20),
             arrowprops=dict(arrowstyle="->", color="red", lw=1.5),
             fontsize=10, color="red")

# Annotate and mark points where Im(Z) = 0
for i, (real, imag, length) in enumerate(zip(zero_imag_points_real, zero_imag_points_imag, zero_imag_lengths)):
    plt.scatter(real, imag, color="orange", marker="o", s=80)  # Mark the point on the graph
    plt.annotate(f"Length = {length:.2f}",
                 (real, imag),
                 textcoords="offset points", xytext=(5, -15),
                 arrowprops=dict(arrowstyle="->", color="orange", lw=1.5),
                 fontsize=10, color="orange")

# Add labels, title, and legend
plt.xlabel("Real Part of $Z_{in}$ (Re)")
plt.ylabel("Imaginary Part of $Z_{in}$ (Im)")
plt.title("Input Impedance on the Complex Plane")
plt.legend(["Input Impedance (Z_in)", "Im(Z_in) = 0"], loc="best")
plt.grid(True)
plt.show()



