
class Gato:
    #metodo constructor
    def __init__(self)->None:
        self.nombre = ""
        self.edad = 0
        self.color = ""

    def hacer_ruido(self) -> str: #metodo es una funcion dentro de un objeto
        return f'{str(self)} ==> Miauuu'

    def __str__(self) -> str: #metodo string para imprimir en consola
        return f'Nombre: {self.nombre} - [{self.color}] -({self.edad} Años)'


def main(): #defino main 2do paso
    g1 = Gato() #creo un objeto Gato
    print(type(g1))
    print(g1)

    g1.nombre = "Michi"
    g1.color = "Negro"
    g1.edad = 4

    print(g1)
    print(g1.hacer_ruido())


main() #llamada a funcion 1er paso