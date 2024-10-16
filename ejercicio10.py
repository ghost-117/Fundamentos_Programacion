"""
 Programa donde un alumno desea saber cuál será su calificación final en la materia de
Algoritmos Dicha calificación se compone de los siguientes porcentajes:
• 55% del promedio de sus tres calificaciones parciales.
• 30% de la calificación del examen final.
• 15% de la calificación de un trabajo final.
"""
# Pedimos al usuario que ingrese las calificaciones
cparcial1 = float(input("Ingrese la primera calificación parcial: "))
cparcial2 = float(input("Ingrese la segunda calificación parcial: "))
cparcial3 = float(input("Ingrese la tercera calificación parcial: "))
cexamenfinal = float(input("Ingrese la calificación del examen final: "))
ctrabajofinal = float(input("Ingrese la calificación del trabajo final: "))

# Calculamos el promedio de las calificaciones parciales,los porcentajes y la calificación final
promedioparciales = (cparcial1 + cparcial2 + cparcial3) / 3
porcentaje_parciales = promedioparciales * 0.55
porcentajexamen = cexamenfinal * 0.30
porcentajetrabajo = ctrabajofinal * 0.15
calificacion_final = porcentaje_parciales + porcentajexamen + porcentajetrabajo

# Imprimimos el resultado
print("La calificación final del alumno es:", calificacion_final)