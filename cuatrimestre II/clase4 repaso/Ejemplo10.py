

def validar(N):
    while N <= 0:
        N = int(input("Ingrese un entero y positivo: "))
        
def fibonacci(N):
    F = 1
    A = 0
    B = 1
    contador = 1
    while contador <= N:
        print(f"{F}")
        F = A + B
        A = B
        B = F
        contador = contador + 1
    
N = int(input("Ingrese un entero y positivo: "))
validar(N)
fibonacci(N)
