
"""
Escribir un programa para registrar y obtener información sobre los viajes diarios 
de un conductor de Uber.
Cada vez que comienza un viaje se debe ingresar la distancia recorrida, 
indicando si el viaje fue corto (‘C’), mediano (‘M’), largo (‘L’) o si es el fin 
de los datos (‘Z’).

El día finaliza cuando se llega a los 30 viajes o cuando se ingresa distancia ‘Z’ 
(fin de los datos).
Por cada viaje se debe ingresar la siguiente información:
Cantidad de pasajeros (mayor a 0 y menor a 4).
Importe a cobrar, incluyendo la el costo básico ($180).
Por cada pasajero de ese viaje se debe ingresar:

Nombre.
Edad (mayor a 18 y menor a 120 años).
Se desea saber, para cada viaje, cuál es la persona más grande y su nombre.

Al finalizar el día de trabajo, el programa debe informar:

Cantidad de viajes por cada categoría (‘C’, ‘M’, ‘L’).
Recaudación total.
Valor promedio del viaje.
Porcentaje de viajes cortos.

Todos los datos ingresados deben ser validados.
"""


import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def obtener_formatos():
    formatos = {
        "encabezado": """
        **********************************************
        **               Diario-UBER                **
        **********************************************
        """,
        "opciones_viaje": """
        **********************************************
        **     opciones      viaje corto    ‘C’     **
        **       del         viaje mediano  ‘M’     **
        **      viaje        viaje largo    ‘L’     **
        **********************************************
        """,
        "resultados": """
    | Cantidad de viajes |      Total     |
    | ------------------ |    ---------   | 
    | viaje corto    ‘C’ |   {total_cortos:>12} |
    | viaje mediano  ‘M’ |   {total_medios:>12} |
    | viaje largo    ‘L’ |   {total_largos:>12} |
    | ------------------ |    ---------   |
    | Recaudacion Total  | $ {recaudacion_total:>12} |
    | Promedio Viajes    | $ {valor_promedio:>12.2f} |
    | % Viajes Cortos    | $ {porcentaje_cortos:>12.2f} |
    """
    }
    return formatos

def entrar_datos():
    formatos = obtener_formatos()
    pasajeros_lista = []
    viajes = []

    clear_console()
    print(formatos["encabezado"])
    print(formatos["opciones_viaje"])


    while len(viajes) < 30:
        distancia = input("Elija la distancia del viaje (corto 'C', mediano 'M', largo 'L', finalizar 'Z')").upper()
        if distancia == 'Z':
            break

        if distancia not in ('C', 'M', 'L', 'Z'):
            print("Distancia no valida, ('C', 'M', 'L', 'Z')")
            continue #vuelve al inicio del bucle

        pasajeros = int(input("Ingrese la cantidad de pasajeros (0 a 4)"))

        if pasajeros >=0 and pasajeros <= 4:
            importe = float(input("Importe a cobrar $: ")) + 180

            for n in range(pasajeros):
                nombre = input("Nombre del pasajero: ")
                edad = int(input("Edad del pasajero: "))
                if edad > 18 and edad < 120:
                    pasajeros_lista.append((nombre, edad))
                else:
                    print("Edad de pasajero fuera de rango (18 a 120 años)")
                
            viajes.append((distancia, pasajeros, importe))
        else:
            print("Ingrese la cantidad de pasajeros correcta (0 a 4)")
    else:
        print("Distancia no valida, ('C', 'M', 'L' o 'Z')")

    return viajes, pasajeros_lista


def calcular_resultados(viajes):
    #variables definicion
    total_cortos = 0
    total_medios = 0
    total_largos = 0
    recaudacion_total = 0
    total_pasajeros = 0

    #iteraciones entre viajes
    for distancia, pasajeros, importe in viajes:
        if distancia == 'C':
            total_cortos += 1
        elif distancia == 'M':
            total_medios += 1
        elif distancia == 'L':
            total_largos += 1

        recaudacion_total += importe
        total_pasajeros += pasajeros

    valor_promedio = recaudacion_total / len(viajes) #valor promedio viajes
    porcentaje_cortos = (total_cortos / len(viajes)) * 100 #porcentaje viajes cortos

    return total_cortos, total_medios, total_largos, recaudacion_total, valor_promedio, porcentaje_cortos

def main():
    formatos = obtener_formatos()
    datos = entrar_datos()
    viajes, pasajeros = datos # desempaqueta datos en 'viajes' y 'pasajeros'

    total_cortos, total_medios, total_largos, recaudacion_total, valor_promedio, porcentaje_cortos = calcular_resultados(viajes)

    clear_console()
    print(formatos["encabezado"])
    print(formatos["resultados"].format(
        total_cortos=total_cortos,
        total_medios=total_medios,
        total_largos=total_largos,
        recaudacion_total=recaudacion_total,
        valor_promedio=valor_promedio,
        porcentaje_cortos=porcentaje_cortos
    ))


main()