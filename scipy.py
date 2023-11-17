# Нахождение минимума функции

from scipy.optimize import minimize

def quadratic_function(x):
    return x**2 + 4*x + 4


initial_guess = 0
result = minimize(quadratic_function, initial_guess)

print("Минимум функции:", result.x)
