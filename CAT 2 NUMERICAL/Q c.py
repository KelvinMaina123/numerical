import numpy as np

x_data = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y_data = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

# Linear interpolation
y_4_0 = np.interp(4.0, x_data, y_data)
print(y_4_0)
