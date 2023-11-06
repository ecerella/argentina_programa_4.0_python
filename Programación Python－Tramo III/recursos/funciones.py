"""
Este Módulo implementa funciones de uso general.

- es_entero(str_numero) 
- es_flotante(str_numero) 
- es_entero_entre(str_numero) 
- es_flotante_entre(str_numero) 

"""
# codigo martin agregado

# En funciones.py

from os import system
import os

def titulo(cadena: str) -> str:
    return f"""
{'-' * 80}
{cadena.title().center(80)}
{'-' * 80}

ARME SU PROPIO PEDIDO
"""
# En funciones.py



# En funciones.py

import os
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


# codigo martin agregado




from os import system


def titulo(cadena: str) -> str:
    return f"{'-'*80}\n{cadena.title().center(80)}\n{'-'*80}"


def menu(str_opciones: str) -> int:
    """

    """
    system("cls")
    lista_opciones = str_opciones.replace('\n', '').split(',')
    for index, cadena in enumerate(lista_opciones):
        if index == 0:
            print(titulo(cadena))
        else:
            print(f"{index} {cadena}")
    print(f"{index+1} Para terminar")
    return leer_entero("Ingrese una opcion: ", 1, index+1)


def es_entero(str_numero: str) -> bool:
    try:  # INTENTO
        int(str_numero)
    except:  # SI HAY ERROR
        return False
    else:   # SI NO HAY ERROR
        return True


def es_flotante(str_numero: str) -> bool:
    try:  # INTENTO
        float(str_numero)
    except:  # SI HAY ERROR
        return False
    else:   # SI NO HAY ERROR
        return True


def es_numero(str_numero: str) -> bool:
    return es_entero(str_numero) or es_flotante(str_numero)



def leer_entero(cartel: str = "Ing. un entero: ",
                desde: int = -9999999999999,
                hasta: int = 9999999999999) -> int:
    todo_ok = False
    while not todo_ok:  # mientras error
        cadena = input(cartel)
        if es_entero(cadena):
            numero = int(cadena)
            if desde <= numero <= hasta:  # if numero >= desde and numero <= hasta
                todo_ok = True
            else:
                print(
                    f"Error: El numero no esta en el rango: [{desde}..{hasta}].")
        else:
            print("Error: Tiene que ingresar un numero entero.")
    return numero


def leer_flotante(cartel:str="Ing. un Float: " ,
                    desde:float=-float('inf'),
                        hasta:float=float('inf')) -> float:
    todo_ok = False
    while not todo_ok:  # mientras error
        cadena = input(cartel)
        if es_flotante(cadena):
            numero = float(cadena)
            if desde <= numero <= hasta:  # if numero >= desde and numero <= hasta
                todo_ok = True
            else:
                print(
                    f"Error: El numero no esta en el rango: [{desde}..{hasta}].")
        else:
            print("Error: Tiene que ingresar un numero float.")
    return numero

def leer_numero(cartel:str="Ing. un numero: ")-> float|int:
    while True:
        cadena = input(cartel)
        if es_entero(cadena):
            return int(cadena)
        elif es_flotante(cadena):
            return float(cadena)
        else:
            print("Tiene que ing. un numero!")

def test_funciones():
    print(leer_numero("Importe: "))
    print(leer_numero("Edad: "))

    print(leer_entero())
    print(leer_entero("Ingrese un numero: "))
    print(leer_entero(desde=0))
    print(leer_entero("Dia: ",1,31))
    print(leer_entero(hasta=10,cartel="Hola: ",desde=1))
    



if __name__ == '__main__':
    test_funciones()
