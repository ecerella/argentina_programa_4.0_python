"""
Implementar una clase Carta, que se crea a partir de un palo y un valor. 
Las cartas deben poder imprimirse de la forma <valor> de <palo>. 
Las cartas deben poder compararse entre ellas: 
    Una carta vale menos que otra si al ser del mismo palo su valor es menor, 
    o si al ser de distintos palos el propio es menor que el palo de la otra carta 
    Implementar una clase Palo, 
    que implementa los métodos __eq__, __lt__ y __str__).
"""
# import sys

# sys.path.append(f"{sys.path[0]}\\recursos\\")

# from txtcolores import strclr

import random

class CartaPoker:

    def __init__(self, numero: int, palo: int, tapada: bool = False) -> None:
        self.__numero: int = numero
        self.__palo: int = palo
        self.__tapada: bool = tapada

    def get_numero(self) -> int:
        return self.__numero

    def get_palo(self) -> int:
        return self.__palo

    def istapada(self) -> bool:
        return self.__tapada

    def tapar(self) -> None:
        self.__tapada = True

    def destapar(self) -> None:
        self.__tapada = False

    def isroja(self) -> bool:
        return self.get_palo() <= 2

    def isnegra(self) -> bool:
        return self.get_palo() >= 3

    def __str__(self) -> str:
        palos = ("#", "♥", "♦", "♣", "♠")
        numeros = ("#", "A", "2", "3", "4", "5", "6",
                   "7", "8", "9", "10", "J", "Q", "K")

        """    
            if self.istapada():
                    cadena = f"{strclr('[',10)}{numeros[0]}{palos[0]}{strclr(']',10)}"
                else:
                    cadena = f"{strclr('[',10)}{numeros[self.get_numero()]}{palos[self.get_palo()]}{strclr(']',10)}"

                return cadena
        """ 
        if self.istapada():
            cadena = f"[{numeros[0]}{palos[0]}]"
        else:
            cadena = f"[{numeros[self.get_numero()]}{palos[self.get_palo()]}]"

        return cadena

    def __eq__(self, __value: object) -> bool:
        if __value is None or not isinstance(__value, CartaPoker):
            return False
        return self.get_numero() == __value.get_numero() \
            and self.get_palo() == __value.get_palo()

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)


class MazoPoker:
    def __init__(self) -> None:
        self.__cartas:list[CartaPoker] = []

    def __len__(self)->int:
        return  len(self.__cartas)
    
    def poner(self,carta:CartaPoker,index:int=None)->None:
        if not isinstance(carta,CartaPoker):
            raise ValueError("Solo se pueden poner cartas de poker!!")  
        if index:
            self.__cartas.insert(index,carta)
        else:
            self.__cartas.append(carta)

        

    def sacar(self,index:int=0)->CartaPoker:
        return self.__cartas.pop(index)

    def isvacio(self)->bool:
        return len(self) == 0
    
    def mezclar(self)->None:
        random.shuffle(self.__cartas)

    def llenar(self,tapado:bool = False)-> None:
        for n in range(1,14):
            for p in range(1,5):
                self.poner(CartaPoker(n,p,tapado))

    def cortar(self)->None:
        if not self.isvacio(): # if len(self) > 0
            posicion = random.randint(0,len(self)-1)
            self.__cartas = self.__cartas[posicion:] + self.__cartas[:posicion]
    
    def __str__(self) -> str:
        return ''.join( [str(carta) for carta in self.__cartas]  )

def main():
    """
    c1 = CartaPoker(1, 1)
    print(c1)
    c1.tapar()
    print(c1)
    if c1.istapada():
        print("Roja", c1.isroja())
    """

    m = MazoPoker()
    m.cortar()
    print(m.sacar())
    m.llenar()
    print('\n',m)
    m.mezclar()
    print('\n',m)
    

    lista = [1,2,3,4,5,6,7,8,9]
    #        0 1 2 3 4 5 6 7 8  
    print(lista)
    lista  = lista[8:]+lista[:8]
    print(lista)
main()
