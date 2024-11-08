#   Dado dos numeros enteros sumarlos y presenta la suma en pantalla
#   Sin funciones

def SumarNumero(numero1,numero2):
    resultado = numero1 + numero2
    return resultado

numero1 = int(input("Ingrese el primer numero entero: "))
numero2 = int(input("Ingrese el segundo numero entero: "))

suma = SumarNumero(numero1,numero2) #   suma = resultado

print(f"El valor de la suma de {numero1} y {numero2} es igual a {suma}")    #   No funciona si pongo resultado
