"""
 Programa que pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos
puntos en el plano. Calcula y muestra la distancia entre ellos.
"""
import math

# Pedimos al usuario las coordenadas de los dos puntos
x1 = float(input("Ingrese la coordenada x del primer punto: "))
y1 = float(input("Ingrese la coordenada y del primer punto: "))
x2 = float(input("Ingrese la coordenada x del segundo punto: "))
y2 = float(input("Ingrese la coordenada y del segundo punto: "))

# Calculamos la distancia
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Imprimimos el resultado
print("La distancia entre los dos puntos es:", distancia)