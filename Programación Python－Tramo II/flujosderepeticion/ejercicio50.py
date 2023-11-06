"""
Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número 
comprendido entre 0 y 10.

La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.

Las notas 1 y 3 no se usan nunca.
La nota 0 se reserva para los ausentes.
Las notas válidas pueden ser un 2 o un valor entre 4 y 10.
"""

while True:
    nota = int(input("Ingrese nota entre 0 y 10: "))
    if nota <0 or nota >10:
        print("ERROR: Nota entre 0 y 10")
    elif nota == 0:
        print("ausente en examen")
    elif nota in (1,3):
        print("No se usan nunca!")
    elif nota ==2 or (nota >=4 and nota <= 10):
        print("Nota validada")
        break
    else:
        print("Nota invalida")
