import sympy as sym

x = sym.Symbol('x')
func = input("Enter the function: ")
sym.Derivative(func, x)

sym.Derivative(func, x, evaluate=True)