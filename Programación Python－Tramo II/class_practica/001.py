
class Gato:
    #METODO CONSTRUCTOR, se ejecuta al instanciar/crear objeto
    def __init__(self,nombre="",edad=0,color="") -> None: #self referencia al objeto actual
        #ATRIBUTOS DE INSTANCIA
        self.nombre = nombre #tercero los objetos tienen: atributos, hacen: comportamiento
        self.edad = edad
        self.color = color

    def hacer_ruido(self): #comportamiento (hace)
        return f'{str(self)} ==> Miauuu'

    def __str__(self) -> str: #metodo para mostrar gato (metodo especial __)
        return f'Nombre: {self.nombre} - [{self.color}] - ({self.edad}) Años'

def main(): #segundo defino
    g1 = Gato() #g1 instancia de objeto
    print(type(g1))

    g1.nombre = "Michi"
    g1.edad = 3
    g1.color = "Negro"

    print(g1)
    print(g1.hacer_ruido())

    g2 = Gato("Pepe",3,"Blanco")
    print(str(g2))
    print(g2. __str__()) #

    print(g2.hacer_ruido())


main()#primero pongo esto