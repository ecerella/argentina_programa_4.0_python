"""
Escribir un programa que permita leer dos números A y B (enteros positivos). 
Calcular el producto A * B por sumas sucesivas e imprimir el resultado.

Ejemplo:

4*3 = 4 + 4 + 4 (4 sumado 3 veces).
3*4 = 3 + 3 + 3 + 3 (3 sumado 4 veces).
"""

numeroUno = int(input("Ingresa el primer numero: "))
numeroDos = int(input("Ingresa el segundo numero: "))

producto = 0
suma_repetida = ""

for _ in range(numeroDos): 
    producto += numeroUno

    suma_repetida += f"{numeroUno} + "

# Quitar el último "+" y espacio de la suma_repetida
suma_repetida = suma_repetida[:-2]

print(f"{numeroUno} * {numeroDos} = {suma_repetida} ({numeroUno} sumado {numeroDos} veces) = {producto}")