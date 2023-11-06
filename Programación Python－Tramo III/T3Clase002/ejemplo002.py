
"""
Implementar la clase Caramelera, que recibe en su constructor la cantidad de 
caramelos que puede contener, y tiene el siguiente comportamiento:

>>> c = Caramelera(20)            >>> c.sacar_caramelos(50)
>>> c.poner_caramelos(10)        Traceback (most recent call last):
>>> c.sacar_caramelos(4)         ...
>>> c.caramelos()                ValueError: No quedan tantos caramelos!
6                                >>> c.poner_caramelos(50)
>>> print(c)                     Traceback (most recent call last):
Caramelera con 6/20 caramelos    ...
                                    ValueError: No queda lugar para tantos caramelos
"""

class Caramelera:
    def __init__(self,capacidad:int) -> None:
        if not capacidad:
            raise ValueError("No se puede crear una Caramelera sin cantidad inicial.")
        self.__capacidad = capacidad
        self.__cantidad = 0

    def poner_caramelos(self,cantidad:int)->None:
        if not cantidad or cantidad < 0 :
            raise ValueError("No se puede agrgar!.")      
        if self.__capacidad < self.__cantidad+cantidad:
            raise  ValueError("No entran!.")      
        
        self.__cantidad += cantidad

    def sacar_caramelos(self,cantidad:int)->None:
        if not cantidad or cantidad < 0 :
            raise ValueError("No se puede sacar!.")      
        
        if cantidad >  self.__cantidad:
            raise  ValueError("No hay!.")      
        
        self.__cantidad -= cantidad

    def __len__(self)->int:
        return self.__cantidad

    def __str__(self) -> str:
        return f"Caramelera con {self.__cantidad}/{self.__capacidad} caramelos."


def main():
    c = Caramelera(25)
    print(c)
    c.poner_caramelos(5)
    print(c)
    try:
        c.sacar_caramelos(30)
    except ValueError as e: # creo una variable e con el texto de la exception
        print(f"No se pudo realizar la operacion ==> {e}") 
    else:
        print("se pudo sacar!!")

    if len(c) > 30:
       c.sacar_caramelos(30)    
       print("se pudo sacar!!") 
    else:
        print("No hay")   
    print(c)





main()





