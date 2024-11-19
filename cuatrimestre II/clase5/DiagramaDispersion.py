#   Diagrama de dispersion

#   Importar el modulo pyplot con el alias plt

import matplotlib.pyplot as plt

#   Crear la figura y los ejes

fig, ax = plt.subplots()

#   Dibujar los puntos

ax.scatter(x=[1,2,3,4,5,6,7],
           y=[1,12,30,24,65,67,37])

#   Salvar la grafica en un archivo png
plt.savefig("Diagra_de_dispersion.png")

#   Mostrar el grafico

plt.show()
