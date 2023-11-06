"""
Se pide implementar la clase Boleteria, que recibe en su constructor un evento y la cantidad de localidades para el mismo; de modo tal que cumpla el siguiente comportamiento:

>>> b = Boleteria("Rush",500)                       >>> b.localidades_agotadas()
>>> print(b)                                        False
Evento: Rush - Localidades vendidas: 0 de 500       >>> b.vender_localidades(100)
>>> b.vender_localidades(400)                       >>> b.localidades_agotadas()
>>> b.vender_localidades(200)                       True
Traceback (most recent call last):                  >>> print(b)
...                                                 Evento: Rush - Localidades vendidas: 500 de 500
ValueError: No hay localidades suficientes
"""




class Boleteria:
    def __init__(self,nombre_evento:str,cantidad_entradas:int) -> None:
        self.__nombre_evento:str=nombre_evento
        self.__cantidad_entradas:int = cantidad_entradas
        self.__vendidas:int = 0

    def getnombre_evento(self)->str:
        return self.__nombre_evento

    def localidades_agotadas(self)->bool:
        return self.__cantidad_entradas == self.__vendidas
    
    def hay_lugar(self,cantidad_entradas)->bool:
        disponible = self.__cantidad_entradas - self.__vendidas
        return cantidad_entradas <= disponible
    
    def vender_entradas(self,cantidad_comprada:int)->None:
        if not self.hay_lugar(cantidad_comprada):
            raise ValueError('No hay localidades suficientes')
        self.__vendidas += cantidad_comprada

    def __str__(self) -> str:
        return f"Evento {self.__nombre_evento} - Localidades vendidas: {self.__vendidas} de {self.__cantidad_entradas}"

class EmpresaEntradas:
    def __init__(self,nombre:str) -> None:
        self.nombre:str = nombre
        self.__boleterias:list[Boleteria] = []

    def agregar_boleteria(self,boleteria:Boleteria) -> None:
        if boleteria is None or not isinstance(boleteria,Boleteria):
            raise ValueError("No se puede agregar algo que no sea una boleteria")
        
        self.__boleterias.append(boleteria)

    def vender_entradas(self,nombre_evento:str,cantidad_entradas:int) -> None:
        evento_encontrado = self.__buscar_evento(nombre_evento)
        if evento_encontrado is None:
            print("No existe el evento")
        elif evento_encontrado.localidades_agotadas():
            print("localidades agotadas!")
        elif not evento_encontrado.hay_lugar(cantidad_entradas):
            print("No hay lugar!")
        else:
            evento_encontrado.vender_entradas(cantidad_entradas)
            print("Localidades vendidas ok!")


    def __buscar_evento(self,nombre_evento:str)->Boleteria:

        for boleteria in self.__boleterias:
            if boleteria.getnombre_evento() == nombre_evento:
                return boleteria
        return None


def main():
    ee= EmpresaEntradas("Ticketon")
    b1 = Boleteria("palito ortega", 1000)
    b2 = Boleteria("juan ramon", 1000)
    b3 = Boleteria("juan y juan", 200)

    ee.agregar_boleteria(b1)
    ee.agregar_boleteria(b2)
    ee.agregar_boleteria(b3)

    ee.vender_entradas("palito ortega", 20)
    ee.vender_entradas("palito ortega", 2000)
    ee.vender_entradas("juan ramona", 20)


    """
        b1 = Boleteria("palito ortega", 1000)
        print(b1)

        entradas = 2050
        try:
            b1.vender_entradas(entradas)
        except ValueError as e:
            print(f"Error: {e} para comprar {entradas} entradas")
        else:
            print(b1)

        b1.vender_entradas(15)
    """

main()