# .Diseñar un algoritmo que convierta temperatura en grados Fahrenheit a grados
# centígrados, presentar por pantalla ambos valores. Sabiendo °C = 5/9 * (°F - 32)

gradosFahrenheit = float(input("Ingrese grados Fahrenheit: "))

gradosCentigrados = 5/9 * (gradosFahrenheit-32)

print("Grados Fahrenheit: ", gradosFahrenheit, "°F")
print("Grados Centigrados: ", gradosCentigrados, "°C")