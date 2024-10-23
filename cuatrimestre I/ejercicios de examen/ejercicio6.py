# dado un numero entero positivo mayor a 1000 determinar su invertido, presentar el original y el invertido

num = 1234
lista = list(str(num)) 
lista.reverse()         
resultado = ''.join(lista)
print(resultado)        

# num = 1234
# original = num
# invertido = 0
# while num > 0:
#     digito = num % 10
#     invertido = invertido * 10 + digito
#     num = num // 10

# print("numero original: ", original)
# print("numero invertido: ", invertido)