"""
Escribir un programa que lea números enteros hasta que se ingrese un 0, y 
muestre el promedio de los números ingresados.

"""
from random import randint

contador = 0
resultado = 0
numeros = randint(0, 10)

for x in range(numeros):
    numeros = randint(0, 100)
    contador +=1
    resultado += numeros
    print(f"contador: {contador} numeros: {numeros} resultado: {resultado}")

promedio = resultado/contador


print(f"el resultado del promedio es: {promedio}")


#usando while
"""
from random import randint

contador = 0
resultado = 0

while True:
    numero = randint(0, 100)  # Generar número aleatorio entre 0 y 100
    
    if numero == 0:
        break
    
    contador += 1
    resultado += numero

if contador == 0:
    print("No se generaron números.")
else:
    promedio = resultado / contador
    print(f"El promedio de los números generados es: {promedio}")
"""
