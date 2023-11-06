"""
Escribir un programa que permita leer dos números naturales A y B. 
Calcular A elevado a la B mediante productos sucesivos y mostrar el resultado.

Ejemplo:

4^3 = 4 * 4 * 4 (4 multiplicado 3 veces).
3^4 = 3 * 3 * 3 * 3 (3 multiplicado 4 veces).
"""

numeroUno = int(input("Ingresa el primer numero: "))
numeroDos = int(input("Ingresa el segundo numero: "))

elevado = 1
multiplicacion_repetida = ""

for _ in range(numeroDos): 
    elevado *= numeroUno

    multiplicacion_repetida += f"{numeroUno} * "

# Quitar el último "*" y espacio
suma_repetida = multiplicacion_repetida[:-2]

print(f"{numeroUno} ^ {numeroDos} = {multiplicacion_repetida} ({numeroUno} multiplicado {numeroDos} veces) = {elevado}")