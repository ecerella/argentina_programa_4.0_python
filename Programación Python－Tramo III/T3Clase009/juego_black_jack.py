import utilidades as util
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
        if not isinstance(cliente, Cliente):
            raise ValueError("Solo juegan los clientes!!!")
        self.jugadores.append(cliente)

    def __hay_jugadores(self) -> bool:
        return len(self.jugadores) > 0

    def __juego_inicia_mano(self) -> None:
        self.mazo.barajar()
        self.apuestas.clear()

    def __jugadores_apuestan(self) -> None:
        print(self.croupier)
        for jug in self.jugadores:
            self.apuestas.append(jug.apuesto())

    def __juego_reparte_dos_cartas(self) -> None:
        for jug in self.jugadores:
            jug.poner_carta(self.mazo.sacar_carta())
            jug.poner_carta(self.mazo.sacar_carta())
        c = self.mazo.sacar_carta()
        c.tapar()
        self.croupier.poner_carta(c)
        self.croupier.poner_carta(self.mazo.sacar_carta())

    def __jugadores_juegan(self) -> None:

        print(util.titulo("los jugadores juegan"))
        print(self.croupier)
        for jug in self.jugadores:
            while not jug.me_planto():
                jug.poner_carta(self.mazo.sacar_carta())
    
    def __croupier_juega(self)->None:
        print(util.titulo("juega el croupioer"))
        c = self.croupier.sacar_carta()
        c.destapar()
        self.croupier.poner_carta(c,0)
        while not self.croupier.me_planto():
            self.croupier.poner_carta(self.mazo.sacar_carta())


    def __juego_reparte_premios(self) -> None:
        suma_croupier = self.croupier.sumar_cartas()
        
        if suma_croupier > 21: # SE PASO EL CROUPIER
            print(f"{self.croupier} ({suma_croupier}) SE PASO!")
            for index,jug in enumerate(self.jugadores):
                apuesta = self.apuestas[index]
                suma_jugador = jug.sumar_cartas()
                if suma_jugador > 21: # PIERDE ==> SE PASO
                    cartel = "PIERDE ==> SE PASO"
                    jug.perder_fichas(apuesta) 
                else: # GANA ==> EL CROUPIER SE PASO
                    cartel = "GANA ==> EL CROUPIER SE PASO"
                    jug.ganar_fichas(apuesta)
                print(f"{jug} {cartel}")
        else:
            print(f"{self.croupier} ({suma_croupier})")
            for index,jug in enumerate(self.jugadores):
                apuesta = self.apuestas[index]
                suma_jugador = jug.sumar_cartas()
                if suma_jugador > 21: # PIERDE ==> SE PASO
                    cartel = "PIERDE ==> SE PASO"
                    jug.perder_fichas(apuesta) 
                elif suma_jugador < suma_croupier:
                    cartel = "PIERDE ==> EL CROUPIER LE GANA"
                    jug.perder_fichas(apuesta) 
                elif suma_jugador > suma_croupier: # GANA ==> LE GANA AL CROUPIER
                    cartel = "GANA ==> LE GANA AL CROUPIER"
                    jug.ganar_fichas(apuesta)
                else:
                    cartel = "EMPATE"
                print(f"{jug} {cartel}")





    def __jugadores_se_descartan(self) -> None:
        for jug in self.jugadores:
            while jug.tiene_cartas():
                self.mazo.poner_carta(jug.sacar_carta())
        
        while self.croupier.tiene_cartas():
            self.mazo.poner_carta(self.croupier.sacar_carta())

    def __jugadores_se_retiran(self) -> None:
        index = 0
        while index < len(self.jugadores):
            jug = self.jugadores[index]
            if jug.fichas <= 0:
                print(f'{jug.nombre} Se retira del juego')
                self.jugadores.pop(index)
            else:
                index += 1


    def jugar(self) -> None:
        self.mazo.llenar()
        while self.__hay_jugadores():
            self.__juego_inicia_mano()
            self.__juego_reparte_dos_cartas()
            self.__jugadores_apuestan()
            self.__jugadores_juegan()
            self.__croupier_juega()
            self.__juego_reparte_premios()
            self.__jugadores_se_descartan()
            self.__jugadores_se_retiran()


def main():
    jbj = BlackJack()
    jbj.agregar_jugador(Humano("Rosita", 100))
    #jbj.agregar_jugador(Compu("CompuClara", 100))
    jbj.agregar_jugador(Humano("Raul", 100))
    #jbj.agregar_jugador(Compu("CompuCoso", 100))

    jbj.jugar()


main()
