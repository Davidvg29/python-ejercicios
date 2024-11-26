#   Grafico de barras

import matplotlib.pyplot as plt

fix, ax = plt.subplots()
ax.bar(["Entretenimiento","Capacitacion","Microcine"],
       [2,1,15])
max_valor = max([2,1,15])  # Máximo valor de las barras
ax.set_yticks(range(0, max_valor + 2))
plt.savefig("GraficoBarras.png")
plt.show()