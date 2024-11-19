#   Diagrama de barras horizontales

import matplotlib.pyplot as plt

fix, ax = plt.subplots()
ax.barh(["A","B","C","D","E","F","G"],
       [1,12,30,24,65,67,37])
plt.savefig("DiagranaBarrasHorizontales.png")
plt.show()