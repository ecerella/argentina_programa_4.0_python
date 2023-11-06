
"""
Escribir un programa que permita al usuario ingresar dos números enteros.
La computadora debe indicar si el mayor es divisible por el menor.

(Un número entero a es divisible por un número entero b
cuando el resto de la división entre a y b es 0)
"""

numero_uno = int(input("Ingrese el primer numero: "))
numero_dos = int(input("Ingrese el segundo numero: "))


if numero_uno > numero_dos:
    resto_division = numero_uno % numero_dos
else:
    resto_division = numero_dos % numero_uno


if resto_division == 0:
    print(f"[{numero_uno}, {numero_dos}] es divisible")
else:
    print(f"[{numero_uno}, {numero_dos}] no es divisible")