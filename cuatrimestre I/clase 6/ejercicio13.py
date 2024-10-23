# 13.Si se ingresa un numero natural presentar por pantalla el desarrollo del factorial
# de dicho número, como así también el valor del factorial.

numero = int(input("Ingrese un numero para sacar su factorial: "))
resultado = 1
contador=1

while contador<=numero:
    resultado = resultado*contador
    contador=contador+1

print("El factorial de ", numero, "es ", resultado)
