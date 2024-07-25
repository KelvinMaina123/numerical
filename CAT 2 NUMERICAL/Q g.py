def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

# Example usage
result = trapezoidal_rule(lambda x: x**2, 0, 1, 1000)
print(result)
