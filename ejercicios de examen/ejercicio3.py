# Desarrolle un sistema que permita ingresar numeros enteros mientras sean distintos de cero e ir sumandolos. al ingresar un numero cero el sistema debe presentar el valor de la suma en pantalla

suma = 0

number = int(input("ingresa un numero para sumar: "))
while number != 0:
    suma = suma + number
    number = int(input("ingresa un numero para sumar: "))

print("la suma de los numeros ingresado es: ", suma)