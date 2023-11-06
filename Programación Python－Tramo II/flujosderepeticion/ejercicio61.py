
"""
Escribir un programa que permita ingresar un número entero positivo y mostrar su 
factorial. El factorial de un número es el producto de todos los números enteros 
desde 1 hasta el número ingresado. Por ejemplo, 
el factorial de 5 es 1 * 2 * 3 * 4 * 5 = 120.
"""

def ingresar_numero_entero():
    while True:
        numero= int(input("Ingresar un numero entero: "))
        if numero >0:
            return numero
        else:
            print("Debe ingresar un numero positivo!")


def factorial():
    factorial = 1

    numero = ingresar_numero_entero()
    for s in range(1, numero + 1):
        factorial *= s
        print(factorial)


factorial()