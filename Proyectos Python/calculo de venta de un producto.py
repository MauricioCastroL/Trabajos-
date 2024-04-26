precio_articulo = float(input("Cual es el precio del articulo?: "))
porcentaje_ganancia = float(input("Cual es la ganania esperaada?: "))
precio_venta = precio_articulo*(1+(porcentaje_ganancia/100))
print(" El precio de venta del articulo es de: ", precio_venta)
