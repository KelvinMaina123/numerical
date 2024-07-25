import time

def bisection_method(a, b, c, lower_limit, upper_limit, error_tolerance, iterations):
    start_time = time.time()
    for i in range(iterations):
        midpoint = (lower_limit + upper_limit) / 2
        if (a * midpoint**2 + b * midpoint + c) == 0 or abs(upper_limit - lower_limit) < error_tolerance:
            break
        elif (a * midpoint**2 + b * midpoint + c) < 0:
            lower_limit = midpoint
        else:
            upper_limit = midpoint
    end_time = time.time()
    return midpoint, end_time - start_time

def regular_falsi(a, b, c, lower_limit, upper_limit, error_tolerance, iterations):
    start_time = time.time()
    for i in range(iterations):
        x = (lower_limit + upper_limit) / 2
        if (a * x**2 + b * x + c) == 0 or abs(upper_limit - lower_limit) < error_tolerance:
            break
        elif (a * x**2 + b * x + c) * (a * lower_limit**2 + b * lower_limit + c) < 0:
            upper_limit = x
        else:
            lower_limit = x
    end_time = time.time()
    return x, end_time - start_time

def newton_raphson_method(a, b, c, x0, error_tolerance, iterations):
    start_time = time.time()
    for i in range(iterations):
        x1 = x0 - (a * x0**2 + b * x0 + c) / (2 * a * x0 + b)
        if abs(x1 - x0) < error_tolerance:
            break
        x0 = x1
    end_time = time.time()
    return x1, end_time - start_time

def secant_method(a, b, c, x0, x1, error_tolerance, iterations):
    start_time = time.time()
    for i in range(iterations):
        x2 = x1 - (a * x1**2 + b * x1 + c) * (x1 - x0) / ((a * x1 + b) - (a * x0 + b))
        if abs(x2 - x1) < error_tolerance:
            break
        x0 = x1
        x1 = x2
    end_time = time.time()
    return x2, end_time - start_time

# User input
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
lower_limit = float(input("Enter the lower limit: "))
upper_limit = float(input("Enter the upper limit: "))
error_tolerance = float(input("Enter the error tolerance: "))
iterations = int(input("Enter the number of iterations: "))

# Calculate roots
root_bisection, time_bisection = bisection_method(a, b, c, lower_limit, upper_limit, error_tolerance, iterations)
root_regular_falsi, time_regular_falsi = regular_falsi(a, b, c, lower_limit, upper_limit, error_tolerance, iterations)
root_newton_raphson, time_newton_raphson = newton_raphson_method(a, b, c, (lower_limit + upper_limit) / 2, error_tolerance, iterations)
root_secant, time_secant = secant_method(a, b, c, lower_limit, upper_limit, error_tolerance, iterations)

# Print results
print("\nBisection method:")
print("Root: ", root_bisection)
print("Time complexity: O(log n)")
print("Time taken: ", time_bisection, "seconds")

print("\nRegular falsi:")
print("Root: ", root_regular_falsi)
print("Time complexity: O(n)")
print("Time taken: ", time_regular_falsi, "seconds")

print("\nNewton-Raphson method:")
print("Root: ", root_newton_raphson)
print("Time complexity: O(n)")
print("Time taken: ", time_newton_raphson, "seconds")

print("\nSecant method:")
print("Root: ", root_secant)
print("Time complexity: O(n)")
print("Time taken: ", time_secant, "seconds")