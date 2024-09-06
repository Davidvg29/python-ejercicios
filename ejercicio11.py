# Dados dos puntos en el plano P1(X1,Y1) y P2(X2,Y2), estos corresponden
# respectivamente a los vértices superior derecho e inferior izquierdo de un
# rectángulo. Indicar el perímetro y la superficie del rectángulo.

p1x1 = int(input("Ingresa el valor de x1 de P1"))
p1y1 = int(input("Ingresa el valor de y1 de P1"))
p2x2 = int(input("Ingresa el valor de x2 de P2"))
p2y2 = int(input("Ingresa el valor de y2 de P2"))

altura = p1y1 - p2y2
base = p1x1 - p2x2

perimetro = 2 * (base+altura)
superficie = base * altura

print("El perimetro es de: ", perimetro)
print("La superficie es de: ", superficie)