# 14.Realizar un algoritmo que permita realizar una multiplicación usando el método
# de sumas sucesivas, presentar el resultado por pantalla.

multiplicando = int(input("Ingrese el numero multiplicando: "))
multiplicador = int(input("Ingresa el numero multiplicadpr: "))
contador=multiplicador
resultado=0

while contador>0:
    resultado = resultado+multiplicando
    contador=contador-1

print("el resultado de multiplicación usando el método de sumas sucesivases: ", resultado)