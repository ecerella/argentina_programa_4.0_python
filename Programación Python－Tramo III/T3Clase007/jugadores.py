
from abc import ABC,abstractmethod
from mazos import Mazo,MazoBlackJack
from cartas import Carta,CartaPoker

class JugadorCartas(ABC):
    def __init__(self,nombre:str,mazo:Mazo) -> None:
        super().__init__()
        self.__nombre:str = nombre
        self.__mano: Mazo = mazo

    @property
    def nombre(self)->str:
        return self.__nombre

    @property
    def mano(self)->Mazo:
        return self.__mano

    def poner_carta(self,carta:Carta,index:int):
        self.mano.poner_carta(carta,index)    
    
    def sacar_carta(self,carta:Carta,index:int):
        self.mano.poner_carta(carta,index)