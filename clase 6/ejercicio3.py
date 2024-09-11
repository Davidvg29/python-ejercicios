# 3. Presentar por pantalla los N primeros números de la serie de Fibonacci
# fibonacci es la suma de los dos anteriores
#suma de los anteriores

number = int(input("Ingrese el limite de fibonacci: "))
contador = 0
init = 0
aux1 = init
aux2 = aux1 + init
resultado = 0

while contador<=number:
    init= init+1
    contador = contador+1
