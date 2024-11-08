#   Dado un numero entero positivo determinar si pertenece a Fibonacci

def sosFibonacci(N):
    bandera = 0 #   Supongo de inicio que no es fibonacci
    #   Si fuera debo cambiar la bandera a 1
    F = 1
    A = 1
    B = 0
    while F < N:
        F = A + B
        B = A
        A = F
    if F == N:
        bandera = 1
    return bandera 
 
N = int(input("Dame un numero entero positivo: ")) 
  
#if sosFibonacci(N):    
if sosFibonacci(N) == 1:    # hay dos posibilidades o es 1 o es cero
    print(f"El valor ingresado {N} es fibonacci")
else:
    print(f"El valor ingresado {N} no es fibonacci")