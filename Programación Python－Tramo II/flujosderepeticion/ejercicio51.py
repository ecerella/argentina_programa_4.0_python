
"""
Escribir un programa que permita al usuario ingresar números hasta que se introduzca un 0.
La computadora debe mostrar el número máximo y el número mínimo.
"""

def ingresar_numeros():
    numeros = []
    while True:
        numero = int(input("Ingrese un numero, finaliza las entradas con 0: "))
        if numero == 0:
            break
        else:
            numeros.append(numero)
    
    print(f"numeros: {numeros}")
    maximo, minimo = maximo_minimo(numeros)
    print(f"el mayor es: {maximo} y el menor: {minimo}")


def maximo_minimo(numeros):
    maximo = max(numeros)
    minimo = min(numeros)
    return maximo, minimo


ingresar_numeros()
