"""
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre 
el máximo.
"""

numeros_enteros = [1, 456, 34, 76, 54, 23, 3, 7, 9, 0]

maximo = -float('inf')

for x in numeros_enteros:
    if x > maximo:
        maximo = x

print(f"maximo: {maximo}")

