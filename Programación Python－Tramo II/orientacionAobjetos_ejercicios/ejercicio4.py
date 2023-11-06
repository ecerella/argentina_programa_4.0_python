"""
Cree una clase Biblioteca y una clase Estante. Una biblioteca tiene muchos
estantes, pero un estante puede existir sin pertenecer a ninguna biblioteca.
"""
from ejercicio2 import Escritor, Libro


class Estante:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)


class Biblioteca:
    def __init__(self, nombre)->None:
        self.nombre = nombre
        self.estantes = []

    def agregar_estante(self, estante):
        self.estantes.append(estante)


def main():
    escritor1 = Escritor("J.K. Rowling")
    libro1 = escritor1.escribir_libro("Harry Potter y la Piedra Filosofal", "Fantasía")
    libro2 = escritor1.escribir_libro("Harry Potter y la Cámara Secreta", "Fantasía")

    estante1 = Estante()
    estante1.agregar_libro(libro1)
    estante2 = Estante()
    estante2.agregar_libro(libro2)

    biblioteca = Biblioteca("Biblioteca Principal")
    biblioteca.agregar_estante(estante1)
    biblioteca.agregar_estante(estante2)

    for estante in biblioteca.estantes:
        print(f"Estante en {biblioteca.nombre}:")
        for libro in estante.libros:
            print(f"Libro: {libro.nombre}, Autor: {libro.autor.nombre}, Género: {libro.genero}")

if __name__ == "__main__":
    main()