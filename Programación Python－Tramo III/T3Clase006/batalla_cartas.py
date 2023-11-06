import math
from abc import ABC, abstractmethod


class Figura(ABC):
    def __init__(self, nombre) -> None:
        self.__nombre = nombre

    def get_nombre(self) -> str:
        return self.__nombre

    @abstractmethod
    def superficie(self) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.__nombre} ==> {self.superficie()}"


class Circulo(Figura):
    def __init__(self, radio) -> None:
        super().__init__("Circulo")
        self.__radio = radio

    def get_radio(self) -> float:
        return self.__radio

    def superficie(self) -> float:
        return math.pi * self.__radio**2


class Cuadrilatero(Figura):
    def __init__(self, nombre, lado1, lado2, lado3, lado4) -> None:
        super().__init__(nombre)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3
        self.__lado4 = lado4

    def get_lado1(self) -> float:
        return self.__lado1

    def get_lado2(self) -> float:
        return self.__lado2

    def get_lado3(self) -> float:
        return self.__lado3

    def get_lado4(self) -> float:
        return self.__lado4

    def __str__(self) -> str:
        return f"{super().__str__()} Lados: [{self.__lado1},{self.__lado2},{self.__lado3},{self.__lado4}]"

class Cuadrado(Cuadrilatero):
    def __init__(self,lado) -> None:
        super().__init__("Cuadrado", lado, lado, lado, lado)
    
    def superficie(self) -> float:
        return self.get_lado1() **2

class Rectangulo(Cuadrilatero):
    def __init__(self, lado_mayor, lado_menor) -> None:
        super().__init__('Rectangulo', lado_mayor, lado_menor, lado_mayor, lado_menor)
    
    def superficie(self) -> float:
        return self.get_lado1()*self.get_lado2()

class Triangulo(Figura):
    def __init__(self,base,altura=0) -> None:
        super().__init__("Triangulo")
        self.__base = base
        self.__altura = altura

    def superficie(self) -> float:
        return self.__base * self.__altura / 2
    
    def __str__(self) -> str:
        return f"{super().__str__()} Base: {self.__base} Altura: {self.__altura}"

def main():
    lista = []
    lista.append(object())
    lista.append(Circulo(6))    
    lista.append(Cuadrado(2))
    lista.append(Rectangulo(8, 3))
    lista.append(Triangulo(2, 3))
    c = Cuadrilatero("sajkdhRombo",1,2,3,4)
    for f in lista:
        print(f)

main()
