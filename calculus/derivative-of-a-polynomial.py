
def poly_term_derivative(c, x, n):
    derivative = c * n * (x ** (n - 1))
    return derivative

print(poly_term_derivative(2.0, 3.0, 2.0))
