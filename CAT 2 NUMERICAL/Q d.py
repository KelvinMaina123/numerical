import sympy as sp

x = sp.Symbol('x')
f = 423 * 10**-9 + 0.9331*x - 650 - x**3
f_prime = sp.diff(f, x)

# Initial guess
x_n = 1

# Newton's Method
for i in range(3):
    x_n1 = x_n - f.evalf(subs={x: x_n}) / f_prime.evalf(subs={x: x_n})
    error = abs((x_n1 - x_n) / x_n1) * 100
    x_n = x_n1
    print(f"Iteration {i+1}: x = {x_n}, Error = {error}%")
