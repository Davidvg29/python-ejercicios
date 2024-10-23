# 13.Genere una lista de 100 números enteros aleatorios comprendidos entre 0 y 100,
# a continuación, presentar por pantalla
import random


import random

lista = []
cont = 0
while cont<=100:
    lista.append(random.randint(0, 100))
    cont = cont+1
print(lista)