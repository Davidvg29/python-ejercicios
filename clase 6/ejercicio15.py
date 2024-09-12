# 15.Realizar un algoritmo que permita realizar una división usando el método de
# restas sucesivas, presentar el cociente y el resto de pantalla.

dividiendo = int(input("Ingrese el dividiendo: "))
divisor = int(input("Ingrese el divisor: "))
cociente = 0
resto = dividiendo

while resto >= divisor:
        resto -= divisor
        cociente += 1

print("El cociente es: ", cociente)
print("El resto es: ", resto)