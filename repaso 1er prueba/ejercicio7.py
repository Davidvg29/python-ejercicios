# 7- Dado un texto determinar cuál es la vocal que más se presenta tenga en cuenta todos los casos

text = input("ingresa el texto para buscar la vocal: ")

a = 0
e = 0
i = 0
o = 0
u = 0

for caracter in text:
    if caracter == "a":
        a+=1
    elif caracter == "e":
        e+=1
    elif caracter == "i":
        i+=1
    elif caracter == "o":
        o+=1
    elif caracter == "u":
        u+=1

if a==0 and e==0 and i==0 and o==0 and u==0:
    print("no hay vocales")
else:
    maxVocal= max(a, e, i, o, u)
    if maxVocal == a:
        print("la vocal mayor veces fue A: ", a)
    elif maxVocal == e:
        print("la vocal mayor veces fue E: ", e)
    elif maxVocal == i:
        print("la vocal mayor veces fue I: ", i)
    elif maxVocal == o:
        print("la vocal mayor veces fue O: ", o)
    elif maxVocal == u: 
        print("la vocal mayor veces fue u: ", u)