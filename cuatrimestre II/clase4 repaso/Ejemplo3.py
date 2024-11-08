#   Pida al usuario ingresar un numero entero
#   Si el entero es mayor a cero (positivo)
#   presente un mensaje que diga que es positivo
#   caso contrario diga que el valor ingresado no es positivo

variable = int(input("Ingrese un entero: "))

if 0 < variable:
    print(f"El valor ingresado {variable} es positivo")
else:
    print(f"El valor ingresado {variable} no es positivo")
    
print("Fin, gracias por usar el programa")
    
