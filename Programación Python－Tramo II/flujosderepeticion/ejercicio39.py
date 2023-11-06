"""
Escribir un programa para calcular e imprimir la suma de los números comprendidos 
entre 42 y 176

"""

numeroUno = 42
numeroDos = 176
suma = 0

for i in range(numeroUno, numeroDos+1):
    suma += i

print (suma)