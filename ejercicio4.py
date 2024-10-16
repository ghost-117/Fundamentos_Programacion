
"""Realiza las cuatro operaciones básicas entre dos números.

  Args:
    num1: El primer número.
    num2: El segundo número.

  Returns:
    Una cadena con los resultados de las operaciones.
  """
# Pedimos al usuario ingresar los números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2  
print("La suma es:", suma)
print("La resta es:", resta) 
print("La division es:", multiplicacion )
print("La multiplicacion es:", division )
