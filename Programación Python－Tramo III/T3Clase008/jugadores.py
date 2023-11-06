
from abc import ABC,abstractmethod
from mazos import Mazo,MazoBlackJack
from cartas import Carta,CartaPoker


class Plantable(ABC):
    @abstractmethod
    def me_planto(self)->bool:
        pass

class JugadorBlackJack(Plantable):
    def __init__(self,nombre:str) -> None:
        super().__init__()
        self.__nombre:str = nombre
        self.__mano: MazoBlackJack = MazoBlackJack()

    @property
    def nombre(self)->str:
        return self.__nombre

    @property
    def mano(self)->MazoBlackJack:
        return self.__mano

    def __str__(self) -> str:
        return f"{self.nombre} {self.mano}"
    
    def poner_carta(self,carta:CartaPoker,index:int=None)->None:
        self.mano.poner_carta(carta,index)    
    
    def sacar_carta(self,carta:Carta,index:int=None)->CartaPoker:
        self.mano.poner_carta(carta,index)
    
    def sumar_cartas(self)->int:
        cantidad_unos = 0
        suma_numeros = 0

        for carta in self.mano.cartas:
            if carta.numero == 1:
                cantidad_unos += 1
            elif carta.numero <= 10:
                suma_numeros += carta.numero
            else:
                suma_numeros += 10


        suma = 0
        if cantidad_unos == 0:
            suma = suma_numeros
        elif cantidad_unos == 1:
            if suma_numeros + 11 > 21:
                suma = suma_numeros + 1
            else:
                suma = suma_numeros + 11
        else:
            if suma_numeros + 11 + cantidad_unos - 1 > 21:
                suma = suma_numeros + cantidad_unos
            else:
                suma = suma_numeros + 11 + cantidad_unos - 1
        
        return suma


class Apostable(ABC):
    def apuesto(self)->int:
        pass

class Cliente(JugadorBlackJack,Apostable):
    def __init__(self, nombre: str,cantidad_fichas:int) -> None:
        super().__init__(nombre)
        self.__fichas:int = cantidad_fichas 
    
    @property
    def fichas(self)->int:
        return self.__fichas

    def __str__(self) -> str:
        return f"{super().__str__()} ${self.fichas} ({self.sumar_cartas()})"

    def ganar_fichas(self,cantidad:int)->None:
        self.__fichas += cantidad

    def perder_fichas(self,cantidad:int)->None:
        self.__fichas -= cantidad


class Croupier(JugadorBlackJack):
    def __init__(self) -> None:
        super().__init__("Sr Croupier")
    
    def me_planto(self) -> bool:
        pass
    

class Humano(Cliente):
    def __init__(self, nombre: str, cantidad_fichas: int) -> None:
        super().__init__(nombre, cantidad_fichas)
    
    def apuesto(self) -> int:
        return super().apuesto()
    
    def me_planto(self) -> bool:
        return super().me_planto()

class Compu(Cliente):
    def __init__(self, nombre: str, cantidad_fichas: int) -> None:
        super().__init__(nombre, cantidad_fichas)
    
    def apuesto(self) -> int:
        return super().apuesto()
    
    def me_planto(self) -> bool:
        return super().me_planto()


if __name__ == '__main__':
    m = MazoBlackJack()
    m.llenar()
    m.barajar()

    cr = Croupier()
    x = m.sacar_carta()
    x.tapar()
    cr.poner_carta(x) 
    cr.poner_carta(m.sacar_carta()) 
    print(cr)

    ch = Humano("Juan",10)
    ch.poner_carta(m.sacar_carta()) 
    ch.poner_carta(m.sacar_carta()) 
    print(ch)

