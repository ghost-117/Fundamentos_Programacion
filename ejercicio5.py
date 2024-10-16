"""
Porgrama que convirte un valor dado  en grados Fahrenheit a grados Celsius
"""
# Pedimos al usuario que ingrese la temperatura en Fahrenheit
fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))

# Fórmula de conversión: Celsius = (Fahrenheit - 32) * 5/9
celsius = (fahrenheit - 32) * 5/9

# Imprimimos el resultado
print(fahrenheit, "grados Fahrenheit equivalen a", celsius, "grados Celsius.")