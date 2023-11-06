
"""
escribir un programa que permita ingresar las notas de los parciales de
un alumno e indicar si promociono, desaprobo o debe recuperar.
si el valor de la nota no esta entre 0 y 10, debe informar un error.
se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
se debe recuperar cuando al menos una de las notas es menor a 4.
"""

nota1 = int(input("Ingrese nota parcial 1: "))
nota2 = int(input("Ingrese nota parcial 2: "))

datos_ok = nota1 >=0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10

aprueba = nota1 >= 4 and nota2 >= 4
promociona = nota1 >= 7 and nota2 >= 7

if datos_ok:
    if aprueba:
        cartel = "Aprueba"
        if promociona:
            cartel = " con promocion"
    else:
        cartel = "Recupera"

print(f"[{nota1},{nota2}]" + cartel)

