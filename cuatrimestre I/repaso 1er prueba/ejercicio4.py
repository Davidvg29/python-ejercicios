# 4- Dado M entero positivo determinar L tal que 1+2+……. + L <= M


M = int(input("ingresa un numero: "))
l = 0
suma = 0
while True:
    l+=1
    suma += l
    if suma>M:
        l=l-1
        break

print(l)