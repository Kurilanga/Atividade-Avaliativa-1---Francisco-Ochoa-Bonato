import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

# Define a função
def f(x):
    return 3**(x-1) - 2**x - 7

# Define os limites do intervalo onde a solução está
a = 2
b = 4

# Define a precisão desejada
tolerance = 1e-6

# Aplica o método da bissecção para encontrar a solução
while (b - a) / 2 > tolerance:
    c = (a + b) / 2
    if f(c) == 0:
        break
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c

# A solução aproximada é o valor médio do intervalo final
x = (a + b) / 2

# Define os valores de x
x_values = np.linspace(2, 4, 1000)

# Plota o gráfico da função
plt.plot(x_values, f(x_values))

# Adiciona a label com a função em latex
plt.title(r'$3^{x-1} - 2^x = 7$')

# Define os limites dos eixos
plt.xlim(2, 4)
plt.ylim(-10, 10)

# Adiciona a label com a informação sobre a monotonicidade
if f(x_values[0]) > f(x_values[-1]):
    plt.text(3, 7, 'Função decrescente', fontsize=14, ha='center', va='center')
else:
    plt.text(3, 7, 'Função crescente', fontsize=14, ha='center', va='center')

# Adiciona a marcação da solução
plt.plot(x_values, np.zeros_like(x_values), 'k--')
plt.plot(x_values, f(x_values), 'r')
plt.plot(x_values[np.abs(f(x_values)) < tolerance], np.zeros_like(x_values[np.abs(f(x_values)) < tolerance]), 'bo')
plt.plot([x], [f(x)], 'go')

# Exibe o gráfico
plt.show()
