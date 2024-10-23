num = 12345
lista = []
suma = 0
digito = 0
while num > 0:
    digito = num % 10
    num = num // 10
    suma = suma +digito
    lista.append(num)

print(lista)
print(digito)
print(suma)