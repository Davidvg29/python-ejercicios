# 9. Dado N números determinar la cantidad de números impares ingresados en
# posición impar.

contadorCant = 0
contador = 0
pregunta = "si"

while pregunta=="si":
    number = int(input("ingrese un numero: "))
    contador = contador +1
    if contador % 2 != 0 and number % 2 != 0:
        contadorCant = contadorCant +1
    pregunta = input("Desea ingresar mas numeros? si o no: ")

print("números impares ingresados en posición impar son: ", contadorCant)