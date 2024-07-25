import numpy as np

def newton_divided_difference(x_points, y_points):
    n = len(x_points)
    divided_diff = np.zeros((n, n))
    divided_diff[:, 0] = y_points

    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i, j] = (divided_diff[i + 1, j - 1] - divided_diff[i, j - 1]) / (x_points[i + j] - x_points[i])
    
    def P(x):
        result = divided_diff[0, 0]
        product_term = 1.0
        for i in range(1, n):
            product_term *= (x - x_points[i - 1])
            result += divided_diff[0, i] * product_term
        return result

    return P

# Given data points
x_points = np.array([1, 2, 3, 4])
y_points = np.array([1, 4, 9, 16])

# Interpolating polynomial
P = newton_divided_difference(x_points, y_points)

# Print polynomial values at given points
print("Interpolated values:", [P(x) for x in x_points])
