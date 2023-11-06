"""
Reglas del Juego "Batalla de Cartas":
El juego se juega entre dos jugadores.
Cada jugador recibe la mitad del mazo (26 cartas) al azar.
Los jugadores revelan la carta superior de su mazo.
El jugador con la carta de mayor valor toma ambas cartas y las coloca en el fondo de su mazo.
Si ambas cartas son del mismo valor, se coloca en un "pozo" y se revela la siguiente carta. 
El jugador con la carta de mayor valor en la siguiente ronda toma todas las cartas del "pozo" y las coloca en el fondo de su mazo.
El juego termina cuando uno de los jugadores no tiene más cartas o después de un número determinado de rondas (por ejemplo, 50 rondas). 
El jugador con más cartas al final gana.
"""

from mazos import MazoPoker


class Jugador:
    def __init__(self,nombre) -> None:
        self.__nombre = nombre
        self.__mano = MazoPoker()

    def poner_carta(self,carta):
        self.__mano.poner_carta(carta)

class BatallaDeCartas:
    def __init__(self,nombre_jugador1,nombre_jugador2,cantidad_manos) -> None:
        self.__cantidad_manos = cantidad_manos
        self.__jug1 = Jugador(nombre_jugador1)
        self.__jug2 = Jugador(nombre_jugador2)
        self.__mazo = MazoPoker()
        self.__mazo.llenar()
        self.__mazo.barajar()

    def __repartir(self):
        while not self.__mazo.isvacio():
            self.__jug1.poner_carta(self.__mazo.sacar_carta())
            self.__jug2.poner_carta(self.__mazo.sacar_carta())

    def jugar(self):
        self.__repartir()


def main():
    bc = BatallaDeCartas("Juan","Pinchame",50)
    bc.jugar()

main()








