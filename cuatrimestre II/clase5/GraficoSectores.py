#   Grafico de sectores

import matplotlib.pyplot as plt
fix, ax = plt.subplots()
ax.pie([1,12,30,24,37])
plt.savefig("GraficoSectores.png")
plt.show()