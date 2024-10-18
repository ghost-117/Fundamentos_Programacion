"""
 Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide
realizar un programa que intercambie los valores de ambas variables y muestre
cuanto valen al final las dos variables.   
"""
# Solicitar al usuario que introduzca los valores de A y B
A = float(input("Introduce el valor de A: "))
B = float(input("Introduce el valor de B: "))

# Mostrar los valores originales
print("Valores originales  A:", A, "B:", B)
# Intercambiar los valores
temp = A
A = B
B = temp
# Mostrar los nuevos valores
print("Valores intercambiados  A:", A, "B:", B)
