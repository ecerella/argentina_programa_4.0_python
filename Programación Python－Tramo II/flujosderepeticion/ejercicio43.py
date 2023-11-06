"""
Escribir un programa que lea números enteros hasta que se la suma de éstos 
sea mayor que 100, y muestre la cantidad de números ingresados.
"""

suma = 0
ingresos = 0

while suma < 100:
    numeros = int(input("Inresa un numero entero: "))
    ingresos += 1
    suma += numeros

print(f"la suma es: {suma} y los numeros ingresados {ingresos}")
              