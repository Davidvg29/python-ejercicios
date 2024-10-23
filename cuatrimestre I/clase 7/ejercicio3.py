# 3. Dado N número enteros, presentar por pantalla el menor número impar
# ingresado, en caso de que no se hubiera ingresado por lo menos dos números
# impares distintos, presentar el mensaje correspondiente

pregunta = "si"
numberMenor = 0


while pregunta == "si":
    number = int(input("Ingrese un numero: "))
    if numberMenor == 0:
        numberMenor = number
    if number%2 != 0 and number < numberMenor:
        numberMenor = number
    pregunta = input("desea agregar mas numeros? si o no: ")

print("El numero menor ingresado es impar es el: ", numberMenor )
