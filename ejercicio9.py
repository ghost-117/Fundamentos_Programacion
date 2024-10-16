"""
Un programa donde una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
desea saber cuánto deberá pagar finalmente por su compra.
"""
# Pedimos al usuario que ingrese el precio total de la compra
precio_total = float(input("Ingrese el precio total de la compra: "))

# Calculamos el descuento 15% del precio total y el precio con descuento
descuento = precio_total * 0.15
precio_final = precio_total - descuento

# Imprimimos el resultado
print("El descuento es de:", descuento)
print("El precio final a pagar es:", precio_final)