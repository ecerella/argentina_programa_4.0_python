
import random

class Gesto:
    # Atributos de clase (constantes)
    PIEDRA = 1
    PAPEL = 2
    TIJERA = 3
    LAGARTO = 4
    SPOCK = 5
    GESTOS = {PIEDRA:"PIEDRA", PAPEL:"PAPEL", TIJERA:"TIJERA", LAGARTO:"LAGARTO", SPOCK:"SPOCK"}

    def __init__(self) -> None:
        self.__valor:int = self.__gesto_random()

    def __eq__(self, __value: object) -> bool:
        if __value is None or not isinstance(__value,Gesto):
            return False
        
        return self.__valor == __value.__valor

    def get_valor(self)->int:
        return self.__valor

    def __gesto_random(self)->int:
        return random.randint(Gesto.PIEDRA,Gesto.SPOCK)

    def __str__(self) -> str:
        return f"{Gesto.GESTOS[self.__valor]}"

class Jugador:
    def __init__(self,nombre) -> None:
        self.__nombre:str = nombre
        self.__mano:Gesto = Gesto()

    def get_nombre(self)->str:
        return self.__nombre

    def get_mano(self)->Gesto:
        return self.__mano

    def hacer_gesto(self)->None:
        self.__mano = Gesto()

    def __str__(self) -> str:
        return f"{self.get_nombre():12} ==< {str(self.__mano)}"

class PiPaTi:
    dicc_motivo={'PIEDRATIJERA': "Piedra aplasta Tijera",
                 'PIEDRALAGARTO':"Piedra aplasta Lagarto",
                 'PAPELPIEDRA':  "Papel tapa a Piedra",
                 'PAPELSPOCK':   "Papel desautoriza Spock",
                 'TIJERAPAPEL':  "Tijera corta Papel",
                 'TIJERALAGARTO':"Tijera decapita Lagarto",
                 'LAGARTOSPOCK': "Lagarto envenena a Spock",
                 'LAGARTOPAPEL': "Lagarto devora Papel",
                 'SPOCKTIJERA':  "Spock rompe Tijera",
                 'SPOCKPIEDRA':  "Spock vaporiza Piedra"
                }

    def __init__(self,nombre_jugador1,nombre_jugador2) -> None:
        self.__jugador1:Jugador = Jugador(nombre_jugador1)
        self.__jugador2:Jugador = Jugador(nombre_jugador2)
        
    def __quien_gana(self)->Jugador:
        gesto1 = self.__jugador1.get_mano() 
        gesto2 = self.__jugador2.get_mano() 
        if gesto1 == gesto2:
            return None, "Empate"
        else:
            valor1 = gesto1.get_valor()
            valor2 = gesto2.get_valor()
            clave1=Gesto.GESTOS[valor1]+Gesto.GESTOS[valor2]
            clave2=Gesto.GESTOS[valor2]+Gesto.GESTOS[valor1]
            if PiPaTi.dicc_motivo.get(clave1):
                return self.__jugador1, PiPaTi.dicc_motivo[clave1]
            else:
                return self.__jugador2, PiPaTi.dicc_motivo[clave2]

            ''' 
            if valor1 == Gesto.PIEDRA and valor2 == Gesto.TIJERA:
                return (self.__jugador1, "Piedra aplasta Tijera")
            if valor1 == Gesto.PIEDRA and valor2 == Gesto.LAGARTO:
                return (self.__jugador1, "Piedra aplasta Lagarto")
            elif valor1 == Gesto.PAPEL and valor2 == Gesto.PIEDRA:
                return (self.__jugador1, "Papel tapa a Piedra")
            elif valor1 == Gesto.PAPEL and valor2 == Gesto.SPOCK:
                return (self.__jugador1, "Papel desautoriza Spock")
            elif valor1 == Gesto.TIJERA and valor2 == Gesto.PAPEL:
                return (self.__jugador1, "Tijera corta Papel")
            elif valor1 == Gesto.TIJERA and valor2 == Gesto.LAGARTO:
                return (self.__jugador1, "Tijera decapita Lagarto")
            elif valor1 == Gesto.LAGARTO and valor2 == Gesto.SPOCK:
                return (self.__jugador1, "Lagarto envenena a Spock")
            if valor1 == Gesto.LAGARTO and valor2 == Gesto.PAPEL:
                return (self.__jugador1, "Lagarto devora Papel")
            elif valor1 == Gesto.SPOCK and valor2 == Gesto.TIJERA:
                return (self.__jugador1, "Spock rompe Tijera")
            elif valor1 == Gesto.SPOCK and valor2 == Gesto.PIEDRA:
                return (self.__jugador1, "Spock vaporiza Piedra")           
            '''
        return None, ''


    def jugar(self)->None:
        victorias_jug1 =0
        victorias_jug2 =0
        terminar = False
        while not terminar:
            self.__jugador1.hacer_gesto()
            print(self.__jugador1)
            self.__jugador2.hacer_gesto()
            print(self.__jugador2)

            ganador, motivo = self.__quien_gana()
            
            if ganador is None:
                print("------   Empate \n")
            else:
                print(f"Ganador: {ganador.get_nombre()}, {motivo} \n")
                if ganador is self.__jugador1:
                    victorias_jug1 += 1
                else:
                    victorias_jug2 += 1

            if victorias_jug1 == 2 or victorias_jug2 == 2:
                terminar = True
        print(f"GANADORRRRRR ==> {ganador.get_nombre()}")

def main():
    juego = PiPaTi("Juan","Pinchame")
    juego.jugar()
    
    """
    for _ in range(10):
        print(Gesto())

    j1 = Jugador("Rosa")
    print(j1)
    j1.hacer_gesto()
    print(j1)

    print(Jugador("Pedro"))
    print(Jugador("Maria"))
    """
main()



