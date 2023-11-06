
"""
Escribir un programa que permita ingresar los números de legajo de los alumnos 
de un curso y su nota de examen final. El fin de la carga se determina 
ingresando un -1 en el legajo.

Informar para cada alumno si aprobó o no el examen considerando que se aprueba 
con nota mayor o igual a 4. Se debe validar que la nota ingresada sea 
entre 1 y 10. Terminada la carga de datos, informar:

Cantidad de alumnos que aprobaron (nota >= 4). 
Cantidad de alumnos que desaprobaron el examen (nota < 4). 
Porcentaje de alumnos que están aplazados (nota == 1).
"""

def ingresar_datos():
    datos_alumnos = [] #lista vacia

    while True:
        nombre = input("Ingrese nombre del alumno: ")
        legajo = int(input("Ingrese numero de legajo de alumno. (-1 para salir)"))

        if legajo == -1:
            print("gracias por usar nuestro software!")
            break

        nota = int(input("Ingrese la nota del alumno: (entre 1 y 10)"))
        if nota < 1 or nota > 10:
            print("nota fuera de rango (debe ser entre 1 y 10)")
        else:
            datos_alumnos.append({"nombre": nombre, "legajo": legajo, "nota": nota})

    return datos_alumnos

def main():
    datos_alumnos = ingresar_datos()
    aprobados = 0
    desaprobados = 0
    aplazados = 0

    for datos in datos_alumnos:
        nota = datos["nota"]

        if nota >= 4:
            print(f"El alumno: {datos['nombre']} APROBO.")
            aprobados +=1
        elif nota == 1:
            print(f"El alumno: {datos['nombre']} APLAZO.")
            aplazados +=1
        else:
            print(f"El alumno: {datos['nombre']} DESAPROBO.")
            desaprobados +=1

    print(f"Cantidad de alumnos que aprobaron: {aprobados}")
    print(f"Cantidad de alumnos desaprobados: {desaprobados}")
    print(f"Porcentaje de alumnos aplazados: {100 * (aplazados / len(datos_alumnos)):-2f}%")


main()