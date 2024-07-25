import sympy as sp
x=sp.Symbol('x')
f=x**3+2*x**2+3*x+4
f_prime+sp.diff(f,x)
print(f_prime)
