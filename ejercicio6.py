# Escribir un programa para convertir una medida dada en metros a sus
# equivalentes en decímetros, centímetros y milímetros. Presentar, por pantalla las
# cuatro magnitudes con sus respectivas unidades.

metros = float(input("Ingresa la cantidad de metros: "))

decimetro = metros*10
centimetros = decimetro*10
milimetros = centimetros*10

print("Decimetros: ", decimetro)
print("Centrimetros: ", centimetros)
print("Milimetros: ", milimetros)