import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#calculando o limite

x = sp.Symbol('x')
f = sp.exp(x) / x**3
limit = sp.limit(f, x, sp.oo)
print("O limite é: {}".format(limit))

#plotando a funcao

x = sp.Symbol('x')
f = sp.exp(x) / x**3
sp.plot(f, (x, 0, sp.oo))
plt.show()