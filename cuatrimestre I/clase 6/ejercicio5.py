# Presentar por pantalla los N primeros números pares

numero = int(input("Ingrese un numero: "))
contador = 1

while contador<=numero:
    if contador%2==0:
        print(contador)
    contador=contador+1