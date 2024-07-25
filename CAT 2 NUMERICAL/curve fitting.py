import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Example data
x_data = np.array([0, 1, 2, 3, 4])
y_data = np.array([2.9, 3.7, 3.2, 4.0, 4.5])

# Define the model function
def model(x, a, b):
    return a * x + b

# Fit the model to the data
popt, _ = curve_fit(model, x_data, y_data)

# Plot the data and the fitted curve
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, model(x_data, *popt), color='red', label='Fitted curve')
plt.legend()
plt.show()
