
"""
Escribir un programa que permita Leer números que representan edades de un grupo 
de personas, finalizando la lectura cuando se ingrese el número 999. 
Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el 
promedio de edad de ambos grupos. Descartar valores que no representan una edad válida. 
(Se considera válido una edad entre 0 y 100)
"""

def Edades_grupo():

    lista_edades = []
    while True:
        edad = int(input("Ingrese edad de persona (999 para salir): "))
        if edad == 999:
            break
        elif edad >= 0 and edad <=100:
            lista_edades.append(edad)
        else:
            print("Edad no valida.")

    return lista_edades

def calculos_lista():

    lista_mayores = []
    lista_menores = []
    lista_edades = Edades_grupo()
    for edad in lista_edades: #iteramos sobre lista_edades y comparamos con 18
        if edad < 18:
            lista_menores.append(edad)
        else:
            lista_mayores.append(edad)

    print(f"Personas menores de 18 años: {len(lista_menores)}")
    print(f"Personas de 18 años o más: {len(lista_mayores)}")

    if lista_edades: #sum cada lista y dividimos por su longitud
        promedio_mayores = sum(lista_mayores) / len(lista_mayores)
        promedio_menores = sum(lista_menores) / len(lista_menores)

        print(f"Promedio de edad menores: {promedio_mayores:.2f}")
        print(f"Promedio de edad mayores: {promedio_menores:.2f}")

    else:
        print("No se ingresaron edades válidas.")

calculos_lista()