"""
Programa que pide al usuario dos números y muestra la "distancia" entre ellos (el valor
absoluto de su diferencia, de modo que el resultado sea siempre positivo).
"""
# Pedimos al usuario que ingrese los dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Calculamos la diferencia y tomamos el valor absoluto
distancia = abs(numero1 - numero2)

# Imprimimos el resultado
print("La distancia entre los dos números es:", distancia)