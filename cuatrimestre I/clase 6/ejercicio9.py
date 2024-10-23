# 9. Introducir un numero N, menor que 40, y un carácter. Diseñar un algoritmo que
# dibuje una línea en pantalla, que incluya N veces el carácter.

numero = int(input("ingrese un numero menor que 40: "))
contador=0

while numero>40:
    numero = int(input("ingrese un numero menor que 40: "))

caracter = input("Ingrese un caracter: ")
while contador<=numero:
    print(caracter, "_____________________________________ ", caracter)
    contador=contador+1

