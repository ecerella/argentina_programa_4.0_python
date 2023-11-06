"""
Escribir un programa que permita ingresar dos numeros enteros a y b. 
El programa debe mostrar:

La suma de los numeros pares entre a y b.
El producto de los numeros impares entre a y b.
"""

a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))

while a > b: #mientras ERROR!!!
    print(f"ERROR: {a} <= {b}")
    b = int(input("Ingrese b: "))

producto_impar = 1 #no puede ser 0 por que es absorvente
suma_pares = 0

for numero in range (a,b+1):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        producto_impar *= numero

print(f"el producto de los impares es: {producto_impar}")
print(f"la suma de los pares es: {suma_pares}")