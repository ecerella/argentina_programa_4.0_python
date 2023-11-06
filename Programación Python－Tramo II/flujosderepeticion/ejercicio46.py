"""
Escribir un programa que a partir de un número entero cant ingresado por el
usuario permita cargar por teclado cant números enteros. 
La computadora debe mostrar cuál fue el mayor número y en qué posición apareció.
"""

from random import randint

#limpiar consola
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Llama a la función para limpiar la consola
clear_console()



posicion = 0
maximo = -float('inf')
cant = randint (1,10)

for x in range(cant):
    numero = randint (-1000,1000)
    print(f"numero: {numero} posicion: {x+1}")
    if numero > maximo:
        posicion = x + 1
        maximo = numero

print(f"cantidad de numeros: {cant}")
print(f"maximo: {maximo} posicion: {posicion}")