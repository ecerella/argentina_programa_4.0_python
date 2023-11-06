

class Gato:
    # METODO CONSTRUCTOR
    def __init__(self,nombre='',edad=0,color='') -> None:
        # ATRIBUTOS DE INSTANCIA
        self.nombre = nombre
        self.edad = edad
        self.color = color
    
    def hacer_ruido(self)->str:
        return f'{str(self)} ==> Miauuu' 

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} - [{self.color}] ({self.edad} Años.)'

def main():
    g1 = Gato()
    print(type(g1))

    g1.nombre = "Michi"
    g1.edad = 3
    g1.color = 'Negro'

    print(g1)
    print(g1.hacer_ruido())
    
    
    g2 = Gato(3,'Blanco')
    print(str(g2))    
    print(g2.__str__())
    print(g2.hacer_ruido())
    

main()
