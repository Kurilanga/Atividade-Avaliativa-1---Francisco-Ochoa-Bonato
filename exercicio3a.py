import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#calculando o limite

x = sp.Symbol('x')
f = sp.sin(2*x)/x
result = sp.limit(f, x, 0)
print("O limite é: ".format(result))

#plotando a funcao

def f(x):
    return np.sin(2*x)/x
x_vals = np.linspace(-10, 10, 1000)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals)
plt.xlabel('x')
plt.ylabel('sin(2x)/x')
plt.title('Graph of sin(2x)/x')
plt.show()