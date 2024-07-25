import numpy as np

def lagrange_interpolation(x_points, y_points):
    def L(k, x):
        terms = [(x - x_points[j]) / (x_points[k] - x_points[j]) for j in range(len(x_points)) if j != k]
        return np.prod(terms)
    
    def P(x):
        return sum(y_points[k] * L(k, x) for k in range(len(x_points)))
    
    return P

# Given data points
x_points = np.array([1, 2, 3, 4])
y_points = np.array([1, 4, 9, 16])

# Interpolating polynomial
P = lagrange_interpolation(x_points, y_points)

# Print polynomial values at given points
print("Interpolated values:", [P(x) for x in x_points])
