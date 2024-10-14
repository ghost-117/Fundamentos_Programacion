"""
Ejercicio 3:Programa que calcula la hipotenusa de un triangullo rectangulo a partir de sus catetos
entrada: cateto1: int
cateto2: int 
salidas hipotenusa
"""
cat1 = input("Escribe el cateto 1:")
cat1= int(cat1)

cat2 = int(input("Escribe el cateto 2:"))
hipo= cat1 * cat1 + cat2 * cat2
hipo =hipo ** (1/2)
print("La hipotenusa es: ", hipo)
