"""
Dado un número de dos cifras, diseñe un programa que permita obtener el
número invertido.
"""
# Pedimos al usuario que ingrese un número de dos cifras
numero = int(input("Ingrese un número de dos cifras: "))

# Separamos las cifras y Invertimos las cifras
cifraunidades = numero % 10
cifradecenas = numero // 10
Ninvertido = cifraunidades * 10 + cifradecenas
# Imprimimos el resultado
print("El número invertido es:", Ninvertido)