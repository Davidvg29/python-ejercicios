# 7. Ingresar N números, presentar por pantalla la suma y el promedio de ellos.

contador = 0
suma = 0
promedio = 0

# numero = int(input("Ingrese un numero: "))

pregunta = "si"

while pregunta=="si":
    numero = int(input("Ingrese un numero: "))
    suma = suma+numero
    contador = contador+1
    pregunta=input("¿Desea agregar mas numeros? Si o no: ")

promedio = suma/contador

print("La suma total es: ", suma)
print("El promedio es: ", promedio)
