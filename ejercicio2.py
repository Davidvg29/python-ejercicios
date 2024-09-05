# Dado el radio de un círculo, presentar por pantalla el diámetro, el perímetro y el
# área del circulo

radio = float(input("ingresa el radio del circulo :"))
diametro = radio*2
perimetro = 2 * 3.14 * radio
area = 3.14 * radio ** 2

print("El diametro del circulo es: ", diametro)
print("El perimetro del circulo es: ", perimetro)
print("El area del circulo es: ", area)