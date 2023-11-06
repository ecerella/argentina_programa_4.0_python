"""
Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número comprendido 
entre 0 y 10.

La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.
"""

while True:
    nota = int(input("Ingrese nota entre 0 y 10: "))
    if nota <0 or nota >10:
        print("ERROR: Nota entre 0 y 10")
    else:
        print("Nota valida")