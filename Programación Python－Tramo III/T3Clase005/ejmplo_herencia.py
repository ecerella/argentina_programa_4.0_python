import math

class Figura(object):
    def __init__(self,nombre) -> None:
        super().__init__()
        self.__nombre = nombre

    def get_nombre(self)->str:
        return self.__nombre
    
    def superficie(self)->float:
        pass
    
    def __str__(self) -> str:
        return f"{self.__nombre} ==> {self.superficie()}"

class Circulo(Figura):
    def __init__(self,radio) -> None:
        super().__init__("Circulo")
        self.__radio = radio

    def get_radio(self)->float:
        return self.__radio

    def superficie(self) -> float:
        return  math.pi * self.__radio**2


class Cuadrado(Figura):
    pass

class Triangulo(Figura):
    pass

def main():
    o = object()
    
    f1 = Circulo(6)
    
    f2 = Cuadrado(2)
    f3 = Triangulo(2,3)





main()


