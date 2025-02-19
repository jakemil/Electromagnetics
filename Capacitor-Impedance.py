import numpy as np

frequencies = [50 * 10 ** 3, 100 * 10 ** 3, 500 * 10 ** 3, 700 * 10 ** 3, 900 * 10 ** 3, 1 * 10 ** 6, 2 * 10 ** 6,
               3 * 10 ** 6, 4 * 10 ** 6, 5 * 10 ** 6]

capacitance = 470 * 10 ** -12
z0 = 50

for freq in frequencies:
    omega = 2*np.pi*freq
    print((1 / (omega * 1j * capacitance)) / z0)

