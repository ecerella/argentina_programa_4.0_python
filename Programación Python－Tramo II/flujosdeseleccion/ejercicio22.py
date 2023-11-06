
"""
Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.
"""

numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))
numero3 = int(input("Ingresa el tercer numero: "))

mayor = max(numero1, numero2, numero3)

print(f"El numero mayor es: {mayor}")