import numpy as np

def bisec(f, a, b, error):
    """
    Bisection method to find the root of a function f in the interval [a, b].
    
    Parameters:
        f (function): The function for which the root is to be found.
        a (float): The start of the interval.
        b (float): The end of the interval.
        error (float): Tolerance for convergence.
        
    Returns:
        tuple: The approximate root and its function value.
    """
    if f(a) * f(b) > 0:
        print("Root not bracketed!")
        return None

    c = 0.5 * (a + b)
    while np.abs(a - b) > error:
        c = 0.5 * (a + b)
        if f(c) == 0:
            return c, f(c)
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, f(c)

def func1(x):
    return x**x - 100

def func2(x):
    return 7 * x**2 + 4 * x + 3

def func3(x):
    return -2 * x**5 - 12 * x**4 - 3 * x**3 - 2 * x**2 - 5 * x + 14

def func4(x):
    return -(x**7 + 7 * x - 3)

def func5(x):
    return -3 * x**3 - 2 * x**2 - x + 15

def func6(x):
    return 3 * x**3 + 4 * x**2 + 55

print(bisec(func1, -10, 10, 1e-12))
print(bisec(func2, -10, 10, 1e-12))
print(bisec(func3, -10, 10, 1e-12)) 
print(bisec(func4, -10, 10, 1e-12))
print(bisec(func5, -10, 10, 1e-12))
print(bisec(func6, -10, 10, 1e-12))
