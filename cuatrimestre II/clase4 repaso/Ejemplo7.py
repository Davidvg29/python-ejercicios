#   Dado N entero positivo presente los numeros del 0 a N incluido

N = int(input("Ingrese un entero positivo: "))

#   Valor = 0
#   while Valor <= N:
#       presento Valor
#       Valor le sumo 1
valor = 0
while valor <= N:
    print(f"{valor}")
    valor = valor + 1
print("Gracias")

#   Si me lo dan al reves desde N a cero
N = int(input("Ingrese un entero positivo: "))
while 0 <= N:
    print(f"{N}")
    N = N - 1
print("Gracias")