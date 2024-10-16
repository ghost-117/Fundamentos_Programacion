""""
Programa que calcule donde un  vendedor recibe un sueldo base más un 10% extra por comisión de sus
ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de
comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes
tomando en cuenta su sueldo base y comisiones.
"""
# Sueldo base del vendedor
sbase = float(input("Ingrese el sueldo base del vendedor: "))

# Ventas del vendedor en el mes
v1 = float(input("Ingrese el valor de la primera venta: "))
v2 = float(input("Ingrese el valor de la segunda venta: "))
v3 = float(input("Ingrese el valor de la tercera venta: "))

# Calculamos el total de ventas ,la comisión (10%) y el sueldo total (Sbase + comision)
Tventas = v1 + v2 + v3
comision = Tventas * 0.10

# Calculamos el sueldo total (sueldo base + comisión)
sueldototal = sbase + comision

# Imprimimos los resultados
print("El total de ventas es:", Tventas)
print("La comisión obtenida es:", comision)
print("El sueldo total del vendedor es:", sueldototal)