import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.log(2*x+1) / np.log(5) + np.log(x-2) / np.log(5)

x = np.linspace(2.1, 5.9, 1000)
plt.plot(x, f(x))
plt.title(r'$\log_5(2x+1) + \log_5(x-2) = 2$')
plt.xlim(2.1, 5.9)
plt.ylim(-10, 10)
plt.text(3.5, 7, 'Função decrescente', fontsize=14, ha='center', va='center')
plt.show()