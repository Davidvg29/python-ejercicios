# 3. Presentar por pantalla los N primeros números de la serie de Fibonacci
# fibonacci es la suma de los dos anteriores
#suma de los anteriores

number = int(input("Ingrese el limite de fibonacci: "))
contador = 0
aux1 = 1
aux2 = 0
resultado = 0

while contador<number:
    print(resultado)
    contador = contador+1
    resultado = aux1 + aux2
    aux1 = aux2
    aux2= resultado
