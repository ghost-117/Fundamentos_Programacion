"""
Realizar un programa que lea un número y que muestre su raíz cuadrada y su
raíz cúbica.
"""
import math
# Pedimos al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Calculamos la raíz cuadrada y la raíz cúbica
Rcuadrada = math.sqrt(numero)
Rcubica = numero**(1/3)

# Imprimimos los resultados
print("La raíz cuadrada de", numero, "es:",  Rcuadrada)
print("La raíz cúbica de", numero, "es:", Rcubica)