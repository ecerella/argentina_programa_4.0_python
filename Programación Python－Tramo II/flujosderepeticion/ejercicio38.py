"""
38 - Escribir un programa que permita ingresar un número entero n. Debe mostrar los 
primeros 10 múltiplos de n.
"""

numero = int(input("Ingrese un numero: "))

print(f"Los 10 múltiplos de {numero} son:")
for i in range(1, 11): 
    total = numero * i
    print(f"""{numero} X {i} = {total}""")

