"""
Cree clases Escritor y Libro. Un escritor ha escrito varios libros, pero un libro solo tiene un escritor.
"""

class Escritor:
    def __init__(self, nombre)->(None): #constructor de clase
        self.nombre = nombre #atributo
        self.libros = [] #lista vacia de libros

    def escribir_libro(self, nombre_libro, genero): #defino metodo escribir_libro
        libro = Libro(nombre_libro, self, genero) #Crea una instancia de la clase Libro, pasando el nombre del libro, el escritor (representado por self), y el género como argumentos
        self.libros.append(libro) #Agrega el libro recién creado a la lista de libros del escritor
        return libro #devueve objeto libro

class Libro:
    def __init__(self, nombre, autor, genero)->(None): #constructor de clase
        self.nombre = nombre #Asigna el nombre del libro al atributo nombre de la instancia
        self.autor = autor #Asigna el autor (que es una instancia de la clase Escritor) al atributo autor
        self.genero = genero # Asigna el género del libro al atributo genero

def main(): #Define la función main(), que es donde se ejecuta el programa principal
    escritor1 = Escritor("J.K. Rowling") #Crea una instancia de la clase Escritor llamada escritor1 con el nombre "J.K. Rowling"
    libro1 = escritor1.escribir_libro("Harry Potter y la Piedra Filosofal", "Fantasia")#Llama al método escribir_libro de escritor1 para crear un libro y lo asigna a la variable libro1
    libro2 = escritor1.escribir_libro("Harry Potter y la Cámara Secreta", "Fantasia")

    for libro in escritor1.libros: #itera a través de la lista de libros del escritor1 y muestra información sobre cada libro, incluyendo el nombre del libro, el autor y el género.
        print(f"Libro: {libro.nombre}, Autor: {libro.autor.nombre}, Genero: {libro.genero}")



if __name__ == "__main__": #Esta línea verifica si el programa se está ejecutando como un script independiente (no importado como módulo en otro programa). Si es así, ejecuta la función main().

    main()


"""
Por supuesto, estaré encantado de explicar en detalle la línea if __name__ == "__main__": en el código.
Cuando ejecutas un archivo de Python, ya sea directamente o mediante un intérprete de comandos, Python establece una variable especial llamada __name__. El valor de __name__ depende de cómo se esté utilizando el archivo:
Si el archivo se está ejecutando como el programa principal, el valor de __name__ será igual a "__main__". Esto significa que se está ejecutando de manera independiente, no importado como un módulo en otro programa.
Si el archivo se importa como un módulo en otro programa, el valor de __name__ será igual al nombre del módulo (el nombre del archivo sin la extensión .py).
La línea if __name__ == "__main__": se utiliza para distinguir entre estos dos casos. Cuando el valor de __name__ es "__main__", significa que el archivo se está ejecutando como un programa principal, y es el punto de entrada de la ejecución. En este caso, el código dentro del bloque indentado que sigue a esta línea se ejecutará. Si el valor de __name__ no es "__main__" (por ejemplo, cuando se importa el archivo como un módulo en otro programa), el código dentro de ese bloque no se ejecutará.
En el contexto de tu código:

if __name__ == "__main__":
    main()

Esto significa que la función main() solo se ejecutará cuando ejecutes el archivo directamente como un programa principal. Si importas este archivo en otro programa como un módulo, la función main() no se ejecutará automáticamente. Esto es útil cuando quieres reutilizar partes de tu código en otros programas sin que la parte principal se ejecute automáticamente al importar el módulo.
Es una práctica común en Python utilizar esta estructura para organizar tu código de manera que sea reutilizable y modular.
"""