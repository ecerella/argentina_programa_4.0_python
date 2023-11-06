"""
Crea un diccionario en el cual las llaves sean números enteros y los valores sean sus cuadrados. Haz esto para números del 1 al n.
"""


def crear_dic(cantidad:int)->dict[int,int]:
    return {x:x**2 for x in range(1,cantidad+1)}

def crear_lista(cantidad:int)->list[int]:
    return [x**2 for x in range(1,cantidad+1)]

def crear_tupla(cantidad:int)->tuple[int]:
    return tuple(x**2 for x in range(1,cantidad+1))

def crear_cadena(cantidad:int)->str:
    return ','.join([str(x**2) for x in range(1,cantidad+1)])


def main():
    print(crear_dic(10))
    print(crear_lista(10))
    print(crear_tupla(10))
    print(crear_cadena(10))


main()