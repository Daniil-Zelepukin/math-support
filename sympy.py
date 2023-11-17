# Нахождение производной и интеграла функции

from sympy import symbols, diff, integrate

x = symbols('x')
f = x**2
derivative = diff(f, x)

integral = integrate(f, x)

print("Функция:", f)
print("Производная функции:", derivative)
print("Интеграл функции:", integral)
