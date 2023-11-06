
"""
Escribir un programa que permita ingresar dos números enteros e indicar si el primero es mayor, 
menor o igual al segundo.
"""

numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

if numero1 == numero2:
    print("Los numeros son iguales")
elif numero1 < numero2:
    print("el primer numero es menor que el segundo")
else:
    print("El primer numero es mayor que el segundo")