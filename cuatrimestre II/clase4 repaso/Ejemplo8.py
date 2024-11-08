
def presentaNumero(N):
    while 0 <= N:
        print(f"{N}")
        N = N - 1
        #   Fijense que no hay retorno

N = int(input("Ingrese un entero positivo: "))
presentaNumero(N)
print("Fin")
