
"""
Escribir un programa para calcular el sueldo final a pagar a cada empleado de 
una empresa. De cada uno se tiene, sueldo básico, antigüedad, cantidad de hijos 
y estudios superiores (‘S’ o ‘N’). Además, se conocen los porcentajes de aumento 
del sueldo que dependen de los siguientes factores:

Si el empleado tiene más de 10 años de antigüedad: aumento del 10%
Si el empleado tiene más de 2 hijos: aumento del 10%, si solo tiene uno 5%
Si el empleado posee estudios superiores: aumento del 5%
Luego de ingresar los datos de un empleado se debe preguntar si se desea ingresar 
otro empleado o no. Se termina la carga cuando no se deseen ingresar más empleados.

Determinar: a. Por cada empleado: número de empleado, el sueldo básico y el 
nuevo sueldo. b. Sueldo nuevo promedio de la empresa.
"""

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    
    empleados = []
    sueldo_promedio = 0
    numero_de_empleado = 1
 

    while True:
        clear_console()
        otro = input("Desea ingresar un empleado (s/n): ").lower()
        if otro != "s":
            break

        empleado = {} #diccionario almacena datos de empleados

        empleado['numero_de_empleado'] = numero_de_empleado

        clear_console()
        sueldo_basico = float(input("Ingrese el sueldo basico del trabajador: "))

        antiguedad = int(input("Ingrese la antiguedad del trabajador: "))
        if antiguedad > 10:
            sueldo_basico += sueldo_basico * 0.1

        cantidad_hijos = int(input("Ingrese cantidad de hijos del trabajador: "))
        if cantidad_hijos > 2:
            sueldo_basico += sueldo_basico * 0.1
        else:
            sueldo_basico += sueldo_basico * 0.05

        estudios_superiores = input("Tiene estudios superiores (s/n): ").lower()
        if estudios_superiores == "s":
            sueldo_basico += sueldo_basico * 0.05

        empleado['sueldo_basico'] = sueldo_basico
        empleado['nuevo_sueldo'] = sueldo_basico

        sueldo_promedio += empleado['nuevo_sueldo']

        empleados.append(empleado)

        numero_de_empleado += 1

    if len(empleados) > 0:
        sueldo_promedio /= len(empleados)

    # Mostrar la información de los empleados y el sueldo nuevo promedio de la empresa
    print("\nInformación de los empleados:")
    for empleado in empleados:
        clear_console()
        print(f"Número de Empleado: {empleado['numero_de_empleado']}")
        print(f"Sueldo Básico: ${empleado['sueldo_basico']:.2f}")
        print(f"Nuevo Sueldo: ${empleado['nuevo_sueldo']:.2f}")
        print("---------------------------")

    print(f"Sueldo Nuevo Promedio de la Empresa: ${sueldo_promedio:.2f}")


main()




"""
def main():

    empleados = []         #empleados (para almacenar los datos de los empleados),
    sueldo_promedio = 0    # sueldo_promedio (para calcular el sueldo promedio de la empresa) y numero_de_empleado
    numero_de_empleado = 1 # (para llevar un registro del número de empleado que se asignará automáticamente).

    
    while True:            # Este bucle while permite ingresar datos de empleados hasta que el usuario decida no ingresar más.
        # Preguntamos al usuario si desea ingresar un empleado y convertimos su respuesta a minúsculas.
        otro = input("Desea ingresar un empleado (s/n): ").lower()
        
        if otro != "s":        # Si el usuario no quiere ingresar más empleados, salimos del bucle.
            break

        empleado = {}    # Creamos un diccionario llamado 'empleado' para almacenar los datos del empleado actual.

        # Asignamos automáticamente el número de empleado al diccionario 'empleado'.
        empleado['numero_de_empleado'] = numero_de_empleado

        # Solicitamos al usuario que ingrese el sueldo básico del empleado y lo almacenamos en la clave 'sueldo_basico'.
        sueldo_basico = float(input("Ingrese el sueldo basico del trabajador: "))

        # Solicitamos al usuario que ingrese la antigüedad del empleado y calculamos el aumento si es mayor a 10 años.
        antiguedad = int(input("Ingrese la antigüedad del trabajador: "))
        if antiguedad > 10:
            sueldo_basico += sueldo_basico * 0.1

        # Solicitamos al usuario que ingrese la cantidad de hijos del empleado y calculamos el aumento según la cantidad de hijos.
        cantidad_hijos = int(input("Ingrese cantidad de hijos del trabajador: "))
        if cantidad_hijos > 2:
            sueldo_basico += sueldo_basico * 0.1
        else:
            sueldo_basico += sueldo_basico * 0.05

        # Solicitamos al usuario si el empleado posee estudios superiores y calculamos el aumento correspondiente.
        estudios_superiores = input("Tiene estudios superiores (s/n): ").lower()
        if estudios_superiores == "s":
            sueldo_basico += sueldo_basico * 0.05

        # Almacenamos el sueldo básico y el nuevo sueldo en el diccionario 'empleado'.
        empleado['sueldo_basico'] = sueldo_basico
        empleado['nuevo_sueldo'] = sueldo_basico

        # Sumamos el nuevo sueldo al sueldo_promedio.
        sueldo_promedio += empleado['nuevo_sueldo']

        # Agregamos el diccionario 'empleado' a la lista 'empleados'.
        empleados.append(empleado)

        # Incrementamos automáticamente el número de empleado para el próximo empleado.
        numero_de_empleado += 1

    # Calculamos el sueldo promedio si se han ingresado empleados.
    if len(empleados) > 0:
        sueldo_promedio /= len(empleados)

    # Mostramos la información de los empleados y el sueldo nuevo promedio de la empresa.
    print("\nInformación de los empleados:")
    for empleado in empleados:
        print(f"Número de Empleado: {empleado['numero_de_empleado']}")
        print(f"Sueldo Básico: ${empleado['sueldo_basico']:.2f}")
        print(f"Nuevo Sueldo: ${empleado['nuevo_sueldo']:.2f}")
        print("---------------------------")

    print(f"Sueldo Nuevo Promedio de la Empresa: ${sueldo_promedio:.2f}")

# Esta línea verifica si el programa se está ejecutando como un script principal.
if __name__ == "__main__":
    main()

"""