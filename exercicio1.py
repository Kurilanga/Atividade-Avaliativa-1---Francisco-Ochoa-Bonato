from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import math
import numpy as np

t = np.arange(0, 21,)

def depreciacao(t):
    Vt = 4000 * (1-0.2)**t
    return Vt

resultado_a = depreciacao(5)
print("A depreciacao depois de 5 anos foi de: {}" .format(resultado_a))

plt.title("Exercicio 1")
plt.xticks(np.arange(min(t), max(t)+1, 1.0))
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.axhline(color="black")
plt.axvline(color="black")
plt.plot(t, depreciacao(t))
plt.show()
