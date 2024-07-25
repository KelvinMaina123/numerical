import numpy as np

def gradient_descent(f, grad_f, initial_guess, learning_rate, num_iterations):
    x, y = initial_guess
    
    for _ in range(num_iterations):
        grad_x, grad_y = grad_f(x, y)
        x = x - learning_rate * grad_x
        y = y - learning_rate * grad_y
    
    return x, y

# Define the function f and its gradient
def f(x, y):
    return x**2 + y**2 - xy + x - y + 1

def grad_f(x, y):
    grad_x = 2*x - y + 1
    grad_y = 2*y - x - 1
    return grad_x, grad_y

# Initial guess and parameters
initial_guess = (0, 0)
learning_rate = 0.1
num_iterations = 100

# Perform Gradient Descent
min_x, min_y = gradient_descent(f, grad_f, initial_guess, learning_rate, num_iterations)
print("Minimum found at:", (min_x, min_y))
