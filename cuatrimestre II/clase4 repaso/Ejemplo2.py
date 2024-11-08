#   Dado un numero si el numero es positivo presentar un mensaje que diga que es mayor a cero


#   Entrada de dato
#   nombreVariable = tipo(input("Cartelito "))
#   tipo en general usabamos int, float, cuando queremos ingresar texto (string) no se pone el #    tipo por que python por defecto entiende que es de tipo string

var_numero = int(input("Dame un numero entero: "))
#   var_numero = float(input("Dame un numero entero: ")) Si van activar esta opcion borre la sangria izquierda

#   if condicion logica :   condicion logica es la que devuelve un booleano (True or False)
#       Si se cumple ejecuta esto
#   si no ejecuta esto otro

if var_numero > 0:
    print(f"El numero {var_numero} es positivo")
print("Fin, gracias por usar el programa")
    