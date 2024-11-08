#   Dado un entero N positivo presentar N numeros fibonacci

#   F = 1,1,2,3,5,8,...,M,M+(M+1)
#   F = 1, A = 0, B = 1 no importa cual de las A o B es cero
#   lo que si debe pasar es que una debe ser cero y la otra 1
#   presento F
#   F = A + B
#   La que vale uno le pasa el valor a la que vale cero
#   A = B
#   A la que valia 1 le paso el valor de F
#   B = F

F = 1
A = 0
B = 1

N = int(input("Ingrese un entero y positivo: "))
while N <= 0:
    N = int(input("Ingrese un entero y positivo: "))
    
contador = 1
while contador <= N:
    print(f"{F}")
    F = A + B
    A = B
    B = F
    contador = contador + 1
print("Gracias")