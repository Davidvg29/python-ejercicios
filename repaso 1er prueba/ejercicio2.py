# 2- Dado N entero par positivo presente en pantalla, si existen los N números de N cifras tal que la segunda mitad del número sea un valor aleatorio que presente N div 2 cifras.

import random

num = int(input("ingrese un numero: "))
while num % 2 != 0 or num < 0:
    num = int(input("numero tiene que ser entero y positivo: "))
mitadNum = num//2
UltMitad = random.randint(10**(mitadNum-1), 10**mitadNum-1)
print(f"{'X'*mitadNum}{UltMitad}")