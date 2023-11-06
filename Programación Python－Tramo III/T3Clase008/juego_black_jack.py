
from mazos import MazoBlackJack
from jugadores import Croupier, Cliente, Humano, Compu


class BlackJack:
    def __init__(self) -> None:
        self.__croupier: Croupier = Croupier()
        self.__mazo: MazoBlackJack = MazoBlackJack()
        self.__jugadores: list[Cliente] = []
        self.__apuestas: list[int] = []

    @property
    def croupier(self) -> Croupier:
        return self.__croupier

    @property
    def mazo(self) -> MazoBlackJack:
        return self.__mazo

    @property
    def jugadores(self) -> list[Cliente]:
        return self.__jugadores

    @property
    def apuestas(self) -> list[Cliente]:
        return self.__apuestas

    def agregar_jugador(self, cliente: Cliente) -> None:
        if not isinstance(cliente,Cliente):
            raise ValueError("Solo juegan los clientes!!!")
        self.jugadores.append(cliente)
    
    def __hay_jugadores(self)->bool:
        return len(self.jugadores) > 0

    def __juego_inicia_mano(self)->None:
        self.mazo.barajar()
        self.apuestas.clear()

    def __jugadores_apuestan()->None:
            pass
            
            self.__juego_reparte_dos_cartas()
            self.__jugadores_juegan()
            self.__juego_reparte_premios()
            self.__jugadores_se_descartan()
            self.__jugadores_se_retiran()

    def jugar(self) -> None:
        self.mazo.llenar()
        
        while self.__hay_jugadores():
            self.__juego_inicia_mano()
            self.__jugadores_apuestan()
            self.__juego_reparte_dos_cartas()
            self.__jugadores_juegan()
            self.__juego_reparte_premios()
            self.__jugadores_se_descartan()
            self.__jugadores_se_retiran()




def main():

    jbj = BlackJack()

    jbj.agregar_jugador(Humano("Rosita", 100))
    jbj.agregar_jugador(Compu("CompuClara", 100))
    jbj.agregar_jugador(Humano("Raul", 100))
    jbj.agregar_jugador(Compu("CompuCoso", 100))

    jbj.jugar()


main()
