"""
Programa que reciba una cantidad de minutos y muestre por pantalla cuantas horas y minutos equivale 
"""
minutos = int(input("Ingrese la cantidad de minutos: "))

# Calculamos las horas dividiendo los minutos entre 60
horas = minutos // 60

# Calculamos los minutos 
minutos_restantes = minutos % 60

#Resultado
print(minutos, "minutos equivalen a", horas, "horas y", minutos_restantes, "minutos.")