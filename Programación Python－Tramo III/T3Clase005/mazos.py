"""
mazos.py
--------

Este módulo contiene definiciones para la representación y manejo de cartas y mazos de póker.

Clases:
    - CartaPoker: Representa una carta individual de un mazo de póker.
    - MazoPoker: Representa un mazo completo de 52 cartas de póker.

Funciones principales:
    - sacar_carta: Retorna y remueve la carta superior del mazo.
    - poner_carta: Agrega una carta al final del mazo.
    - barajar: Baraja las cartas del mazo de manera aleatoria.
    - isvacio: Retorna `True` si el mazo no tiene cartas y `False` en caso contrario.

Uso:
    mazo = MazoPoker(con_cartas=True)
    mazo.barajar()
    carta = mazo.sacar_carta()
    print(carta)

Nota:
    Aunque este módulo ha sido diseñado específicamente para cartas de póker, podría ser extendido o adaptado
    para otros tipos de juegos de cartas.

Autor: ######################
Fecha: ##/##/####
"""


from cartas import CartaPoker
import random

class MazoPoker:
    """Clase que representa un mazo de cartas de Poker."""

    def __init__(self, con_cartas: bool = False, tapado: bool = False) -> None:
        """
        Inicializa el mazo de Poker.

        Args:
            con_cartas (bool, optional): Si el mazo debe ser inicializado con cartas. Por defecto es False.
            tapado (bool, optional): Si las cartas deben ser inicializadas tapadas. Por defecto es False.
        """
        self.__cartas: list[CartaPoker] = []
        if con_cartas:
            self.llenar(tapado)

    def __len__(self) -> int:
        """Retorna el número de cartas en el mazo."""
        return len(self.__cartas)

    def isvacio(self) -> bool:
        """Verifica si el mazo está vacío."""
        return len(self) == 0

    def poner_carta(self, carta: CartaPoker, index: int = None) -> None:
        """
        Agrega una carta al mazo.

        Args:
            carta (CartaPoker): Carta a agregar al mazo.
            index (int, optional): Posición donde insertar la carta. Por defecto es al final.

        Raises:
            ValueError: Si el argumento no es una instancia de CartaPoker.
        """
        if not isinstance(carta, CartaPoker):
            raise ValueError(f"{carta} No es un una CartaPoker")

        if index is None:
            self.__cartas.append(carta)
        else:
            self.__cartas.insert(index, carta)

    def sacar_carta(self, index: int = None) -> CartaPoker:
        """
        Saca una carta del mazo.

        Args:
            index (int, optional): Posición de la carta a sacar. Por defecto es la primera.

        Returns:
            CartaPoker: Carta sacada del mazo.
        """
        if index is None:
            return self.__cartas.pop(0)
        return self.__cartas.pop(index)

    def llenar(self, tapado: bool = False) -> None:
        """Llena el mazo con las 52 cartas de Poker."""
        self.__cartas.clear()

        for n in range(1, 14):
            for p in range(1, 5):
                self.poner_carta(CartaPoker(n, p, tapado))

    def barajar(self) -> None:
        """Baraja las cartas del mazo."""
        random.shuffle(self.__cartas)

    def cortar(self) -> None:
        """
        Corta el mazo en una posición aleatoria y coloca la parte inferior arriba.
        """
        posicion = random.randint(0, len(self) - 1)
        self.__cartas = self.__cartas[posicion:] + self.__cartas[:posicion]

    def __str__(self) -> str:
        """Retorna la representación en cadena del mazo."""
        return ''.join([str(carta) for carta in self.__cartas])
    
    def __iter__(self):
            self.__index = 0
            return self

    def __next__(self):
        if self.__index < len(self):
            carta = self.__cartas[self.__index]
            self.__index += 1
            return carta
        else:
            raise StopIteration


def test_mazos():
    print("Se esta ejecutando el test de la clase MazoPoker")
    mp = MazoPoker()
    mp.llenar()
    mp.barajar()
    print(mp)
    
    
    for carta in mp:
        print(carta)


if __name__ == '__main__':
    test_mazos()
