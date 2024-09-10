# Diseñar un algoritmo que permita ingresar una cantidad de Megabytes y
# presentar por pantalla su equivalente en Gigabytes, Kilobytes, Bytes y bits.

megabytes = int(input("Ingresa la cantidad de Megabytes: "))

gigabytes = megabytes/1024
kilobytes = megabytes*1024
bytes = megabytes*1024*1024
bits = megabytes*1024*1024*8

print(megabytes, "MB")
print(gigabytes, "GB")
print(kilobytes, "KB")
print(bytes, "Bytes")
print(bits, "Bit")