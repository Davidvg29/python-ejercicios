#   Pida al usuario ingresar un numero entero
#   Si el entero es mayor a cero (positivo)
#   Si el numero es menor a cero (negativo)
#   Si el valor es cero que diga (cero)

variable = int(input("Dame un entero positivo: "))

if variable == 0:
    print(f"El valor ingresado {variable} es igual a cero")
elif variable > 0:
    print(f"El valor ingresado {variable} es positivo")
else:
    print(f"El valor ingresado {variable} es negativo")
    
print("Gracias por usar mi programa")