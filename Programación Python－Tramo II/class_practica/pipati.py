import random

class Gesto:
    #atributos de clases (constantes)
    PIEDRA = 1
    PAPEL = 2
    TIJERA = 3
    LAGARTO = 4
    SPOCK = 5

    # lo que es no siempre es lo que ves..
    # piedra como clave y como dato "piedra" es la forma en que armo un diccionario

    GESTOS = {PIEDRA:"PIEDRA",PAPEL:"PAPEL",TIJERA:"TIJERA",LAGARTO:"LAGARTO",SPOCK:"SPOCK"}#variable de clase Gesto

    def __init__(self) -> None:
        self.__valor:int = self.__gesto_random()

    def __eq__(self, __value: object) -> bool:
        if __value is None or not isinstance(__value,Gesto):
            return False
        
        return self.__valor == __value.__valor

    def get_valor(self) -> int:
        return self.__valor

    def __gesto_random(self) -> int: #metodo de instancia "self"
        return random.randint(Gesto.PIEDRA,Gesto.SPOCK)
    
    def __str__(self) -> str:
        return f"{Gesto.GESTOS[self.__valor]}"#retorname de la clase Gesto. GESTOS en que posicion. si el valor es 1 retorno piedra, 2 papel, etc


class Jugador:
    def __init__(self,nombre) -> None:
        self.__nombre:str = nombre
        self.__mano:Gesto = Gesto() #necesito una clase que represente al gesto

    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_mano(self) -> Gesto:
        return self.__mano

    def hacer_gesto(self) -> None:
        self.__mano = Gesto() #cada vez que el jugador hace un gesto crea un objeto nuevo gesto

    def __str__(self) -> str:
        return f"{self.get_nombre()} ==< {str(self.__mano)}"


class PiPaTi:
    def __init__(self,nombre_jugador1,nombre_jugador2) -> None:
        self.__jugador1:Jugador = Jugador(nombre_jugador1) #composicion, creeo jugador dentro del juego
        self.__jugador2:Jugador = Jugador(nombre_jugador2)

    def __quien_gana(self) -> Jugador:
        gesto1 = self.__jugador1.get_mano()
        gesto2 = self.__jugador2.get_mano()
        if gesto1 == gesto2:
            return None
        else:
            valor1 = gesto1.get_valor()
            valor2 = gesto2.get_valor()
            if valor1 == Gesto.TIJERA and valor2 == Gesto.PAPEL or valor1 == Gesto.PAPEL and valor2 == Gesto.PIEDRA or valor1 == Gesto.PIEDRA and valor2 == Gesto.LAGARTO or valor1 == Gesto.LAGARTO and valor2 == Gesto.SPOCK or valor1 == Gesto.SPOCK and valor2 == Gesto.TIJERA or valor1 == Gesto.TIJERA and valor2 == Gesto.LAGARTO or valor1 == Gesto.LAGARTO and valor2 == Gesto.PAPEL or valor1 == Gesto.PAPEL and valor2 == Gesto.SPOCK or valor1 == Gesto.SPOCK and valor2 == Gesto.PIEDRA or valor1 == Gesto.PIEDRA and valor2 == Gesto.TIJERA:
                return self.__jugador1

        return self.__jugador2

    def jugar(self) -> None:
        victorias_jug1 = 0#cuando termina. en dos victorias
        victorias_jug2 = 0
        terminar = False
        while not terminar:
            self.__jugador1.hacer_gesto()
            print(self.__jugador1)
            self.__jugador2.hacer_gesto()
            print(self.__jugador2)

            ganador = self.__quien_gana()

            if ganador is None:
                print("empate")
            elif ganador is self.__jugador1:
                print(f"Ganador: {ganador.get_nombre()}")
                victorias_jug1 += 1
            else:
                print(f"Ganador: {ganador.get_nombre()}")
                victorias_jug2 += 1

            if victorias_jug1 == 2 or victorias_jug2 == 2:
                terminar = True
        print(f"GANADORRRRRRRR ==> {ganador.get_nombre()}")

def main():
    juego = PiPaTi("Juan","Pinchame")
    juego.jugar() #un solo metodo publico. jugar.

    #for _ in range(10):
    #    print(Gesto())


    #print(Jugador("rosa"))
    #print(Jugador("pedro"))
    #print(Jugador("juan"))

main()