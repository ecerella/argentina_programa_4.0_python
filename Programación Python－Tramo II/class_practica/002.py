"""
implementar la clase caramelera, que recibe en su constructor la cantidad de
caramelos que puede contener, y tiene el siguiente comportamiento:

>>> c = caramelera(20)          >>>c.sacar_caramelos(50)
>>> c.poner_caramelos(10)       Traceback (most recent call last):
>>> c.sacar_caramelos(4)        ...
>>> c.caramelelos()             valueError: no quedan tantos caramelos!
>>> 6                           >>>c.poner_caramelos(50)
>>> print(c)                    Traceback (most recent call last):
>>> caramelera con 6/20 caramelos  ...
                                ValueError: no queda lugar para caramelos
"""

class Caramelera:
    def __init__(self,capacidad:int) -> None:
        if not capacidad:
            raise ValueError("No se puede crear una caramelera sin cantidad inicial")
        self.__capacidad = capacidad #atributos son privados __
        self.__cantidad = 0

    def poner_caramelos(self,cantidad:int) -> None:
        if not cantidad or cantidad < 0:
            raise ValueError("No se puede agregar")
        if self.__capacidad < self.__cantidad+cantidad:
            raise ValueError("No entran!")
        
        self.__cantidad += cantidad

    def sacar_caramelos(self,cantidad:int) -> None:
        if not cantidad or cantidad < 0:
            raise ValueError("No se puede sacar!")
        
        if cantidad > self.__cantidad:
            raise ValueError("No hay!")
        
        self.__cantidad -= cantidad

    def __len__(self)-> int:
        return self.__cantidad

    def __str__(self)-> str:
        return f"caramelera con {self.__cantidad}/{self.__capacidad} caramelos"

def main():
    c = Caramelera(25)
    print(c)
    c.poner_caramelos(5)
    print(c)
    try:
        c.sacar_caramelos(30)
    except ValueError as e: #creo una variable e a la que se le asigna el motivo de la excepcion
        print(f"No se pudo realizar la operacion ==> {e}")
    else:
        print("se pudo sacar!")

    if len(c) > 30:
        c.sacar_caramelos(30)
        print("se pudo sacar!")
    else:
        print("No hay")

    print(c)


main()