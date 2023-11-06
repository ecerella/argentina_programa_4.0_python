
"""
Un entrenador le ha propuesto a un atleta recorrer una ruta de cinco kilómetros durante 10 días 
para determinar si es apto para la prueba de 5 kilómetros que se desarrollará en el Parque. 
No se sabe si está apto y para eso nos piden que hagamos el siguiente programa.

Nos ingresan por cada día de entrenamiento tiempo de la prueba en minutos 
(entero mayor que 0 y menor a 100)

Para considerarlo apto debe cumplir las siguientes condiciones:

Que en ninguna de las pruebas haga un tiempo mayor a 20 minutos.
Que al menos en una de las pruebas realice un tiempo menor de 15 minutos.
Que su promedio sea menor o igual a 18 minutos.
Se pide:

Diseñar un algoritmo para registrar los datos y decidir si es apto para la competencia. *Sólo en 
caso de estar apto, informar el promedio y el número de día en el que realizó el menor tiempo
"""

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def datos_atleta():
    datos_atletas = []
    nombre = input("Ingrese el nombre del atleta: ")
    dia = 1

    while dia <= 10:
            tiempo = float(input(f"Dia {dia}: Ingrese el tiempo en que {nombre} recorrio los 5km: "))

            if tiempo > 0 and tiempo < 100:
                datos_atletas.append((nombre, tiempo))
                dia += 1
            else:
                print("tiempo fuera de parametros (0 a 100)")
  
    return datos_atletas


def probar_apto():
    datos_atletas = datos_atleta()
    menor_tiempo = float('inf')
    promedio = 0

    for nombre, tiempo in datos_atletas:
        clear_console()
        promedio += tiempo

        if tiempo > 20:
            print(f"Nombre: {nombre}, Día {datos_atletas.index((nombre, tiempo)) + 1}: Debes mejorar el tiempo de las prácticas.")
        elif tiempo > 15:
            print(f"Nombre: {nombre}, Día {datos_atletas.index((nombre, tiempo)) + 1}: Excelente tiempo de práctica.")
        else:
            print(f"Nombre: {nombre}, Día {datos_atletas.index((nombre, tiempo)) + 1}: Tiempo dentro de los parámetros.")

        if tiempo < menor_tiempo:
            menor_tiempo = tiempo

    promedio /= 10
    clear_console()

    if menor_tiempo < 15 and promedio <= 18:
        print(f"\n{nombre} es apto para competir.")
        print(f"Promedio de tiempo: {promedio:.2f} minutos")
        print(f"Día del menor tiempo: Día {datos_atletas.index((nombre, menor_tiempo)) + 1}")
    else:
        print("\nEl atleta no es apto para competir. Debe mejorar sus tiempos y cumplir con los requisitos.")



probar_apto()



"""
import os: Esta línea importa el módulo os, que proporciona funciones relacionadas con el sistema operativo. En particular, 
el código utiliza os.system() para limpiar la consola.

def clear_console(): Esta función utiliza os.system() para limpiar la consola. Dependiendo del sistema operativo, 
utiliza 'cls' en Windows (si os.name es 'nt') o 'clear' en sistemas Unix (como Linux o macOS).

def datos_atleta(): Esta función permite al usuario ingresar el nombre del atleta y luego registra los tiempos que el 
atleta toma para recorrer 5 km durante 10 días. Los tiempos se almacenan en una lista de tuplas llamada datos_atletas, 
donde cada tupla contiene el nombre y el tiempo del atleta para un día específico. Se asegura de que los tiempos ingresados 
estén dentro de los límites (mayores que 0 y menores que 100).

def probar_apto(): Esta función utiliza la función datos_atleta() para recopilar los datos del atleta. Luego, evalúa si 
el atleta es apto para competir en función de tres condiciones: que ningún tiempo sea mayor a 20 minutos, que al menos 
un tiempo sea menor a 15 minutos y que el promedio de los tiempos sea menor o igual a 18 minutos. La función también 
realiza un seguimiento del día en el que se obtuvo el tiempo más bajo y muestra los resultados en la consola, utilizando 
clear_console() para limpiar la pantalla antes de mostrar los resultados.

En resumen, este código permite al usuario registrar y evaluar el rendimiento de un atleta durante 10 días de entrenamiento. 
Al final, se muestra si el atleta es apto para competir o no, junto con el promedio de tiempos y el día en que se obtuvo el 
tiempo más bajo. La función clear_console() se utiliza para mantener la pantalla de la consola limpia y ordenada 
al mostrar los resultados.

"""