"""
Programa que calcula la media de 3 numeros ingresados por el usuario 
"""
# Pedimos al usuario que ingrese los tres números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Calculamos la media (promedio)
media = (numero1 + numero2 + numero3) / 3
#Resultado
print("La media de los números ingresados es:", media)