# 2. Diseñar un algoritmo que presente en pantalla las 10 primeras tablas de
# multiplicar

numTabla = int(input("¿Ingresa el numero de la tabla que quieras ver:? "))
contador = 1

while numTabla<1 or numTabla>10:
    print("Debes ingresar un numero entre 1 y 10")
    numTabla = int(input("¿Ingresa el numero de la tabla que quieras ver:? "))

print("Tabla de multiplicar del ", numTabla)
while contador <= 10:
    print(contador, " X ", numTabla, " = ", contador*numTabla)
    contador = contador + 1
