#   Dado un numero entero positivo determinar si pertenece a Fibonacci

N = int(input("Dame un numero entero positivo: "))

F = 1
A = 1
B = 0

while F < N:
    F = A + B
    B = A
    A = F
if F == N:
    print(f"El valor {N} es fibonacci")
else:
    print(f"El valor {N} no es fibonacci")    