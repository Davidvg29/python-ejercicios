#   Desarrolle un programa que pida a una persona su nombre y apellido y presente en pantalla el apellido y el nombre en ese orden

#   Entrada de dato
#   nombreVariable = tipo(input("Cartelito "))
#   tipo en general usabamos int, float, cuando queremos ingresar texto (string) no se pone el #    tipo por que python por defecto entiende que es de tipo string

var_nombre = input("Nombre: ")
var_apellido = input("Apellido: ")
#   para presentar en pantalla uso el comando print
#   print(f"contedio del mensaje {variable}"")
print(f"Su apellido es {var_apellido} y su nombre es {var_nombre}")
#   Si no ponen la f la va a dar error
