# Создание графика квадратной функции

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = x**2

plt.plot(x, y, label='y = x^2')

plt.title('График квадратной функции')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()

plt.show()
