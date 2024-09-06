# .Dado el precio de un producto, presentar por pantalla, los impuestos que debe
# pagar IVA 21%, Ingresos Brutos 2.5% e Impuesto Municipal 1.5%

precioProducto = float(input("Ingrese el precio del producto: "))

iva = precioProducto * (21 / 100)
ingresosBrutos = precioProducto * (2.5 / 100)
impuestoMunicipal = precioProducto * (1.5 / 100)

print("Precio del producto es: ")
print("Con los impuestos es de: ", precioProducto+iva+ingresosBrutos+impuestoMunicipal)