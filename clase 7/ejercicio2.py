# 2. Ingresar N números enteros, presentar por pantalla el valor del mayor numero
# ingresado y la posición en que se ingresó (tener en cuenta la posibilidad de que
# todos los números ingresados pueden ser igual)



pregunta = "si"
numeroMayor = 0
contador = 0
posicion= 0

while pregunta == "si":
    number = int(input("ingresa un numero entero: "))
    contador = contador+1
    if number > numeroMayor:
        numeroMayor = number
        posicion=contador
    pregunta = input("Desea ingresar otro numero? si o no: ")

print("El numero mayor ingresado es", numeroMayor)
print("El numero se ingreso en la posicion", posicion)
