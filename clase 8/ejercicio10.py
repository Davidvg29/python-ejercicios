# 10.Con la lista anterior presente en pantalla el elemento que se encuentra en la
# cuarta posición y el índice del elemento que vale 8 usando instrucciones.

lista = []
contador = 0

while contador<20:
    contador= contador+1
    lista.append(contador)

print(lista[4])
print(lista.index(8))