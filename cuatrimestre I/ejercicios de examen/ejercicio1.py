# dado N enteros positivos diferentes encuentre el mayor numero par, en caso de no 
# haber ingresado ningun numero par el sistema debe decir "No se ingreso ningun numero par", 
# si se ingreso uno solo el sistema debe decir "se ingreso un solo numero
#  par no es posible determinar el mayor"

pregunta = "si"
mayorPar = 0
cantPar = 0
numbers = []

while pregunta == "si":
    number = int(input("ingrese un numero entero positivo: "))
    while number < 0:
      number = int(input("Debes ingresar un numero entero positivo: "))  
    search = number in numbers
    if search == False:
        numbers.append(number)
        if number % 2 == 0 and number > mayorPar:
            mayorPar = number
            cantPar = cantPar + 1
    pregunta = input("Desea ingresar mas numeros? si o no: ")

if cantPar == 0:
    print("No se ingreso ningun numero par")
elif cantPar == 1:
    print("se ingreso un solo numero par no es posible determinar el mayor y es el: ", mayorPar)
else:
    print("El numero par mayor ingresado fue: ", mayorPar)