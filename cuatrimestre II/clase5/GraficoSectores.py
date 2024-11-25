#   Grafico de sectores

import matplotlib.pyplot as plt
fix, ax = plt.subplots()
ax.pie([6,12])
plt.savefig("GraficoEstadisticaGeneros.png")
plt.show()