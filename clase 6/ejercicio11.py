# 11.Ingresar números mientras sean distintos de cero, presentar por pantalla el
# promedio de estos.

numero = 0
suma=0
promedio=0
contador=0

pregunta="si"

while pregunta=="si":
    numero = int(input("Ingresa un numero distinto de 0: "))
    while numero==0:
        numero = int(input("Tienes que ingresar un numero distinto de 0: "))
    suma = suma + numero
    contador = contador+1
    pregunta=input("Quieres agregar mas numeros? si o no: ")

promedio=suma/contador
print("El promedio de los numeros ingresados es: ", promedio)

    