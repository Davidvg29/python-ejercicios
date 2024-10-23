# Dado el radio y la altura de un cilindro, presentar por pantalla el volumen de este.
# Sabiendo que su volumen se calcula como superficie de la base por la altura.

radio = float(input("Ingrese el radio de un cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

volumen = 3.14 * altura * radio ** 2

print("El volumen del cilindro es: ", volumen, "cm cubicos")