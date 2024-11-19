#   Grafico de barras

import matplotlib.pyplot as plt

fix, ax = plt.subplots()
ax.bar(["A","B","C","D","E","F","G"],
       [1,12,30,24,65,67,37])
plt.savefig("GraficoBarras.png")
plt.show()