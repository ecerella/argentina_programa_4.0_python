"""
Defina clases Orquesta y Instrumento. Una orquesta utiliza varios instrumentos,
pero un instrumento puede existir sin estar en ninguna orquesta.
"""

class Orquesta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def agregar_instrumento(self, instrumento):
        self.instrumentos.append(instrumento)

class Instrumento:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def tocar(self):
        print(f"Tocando el instrumento {self.nombre}")


if __name__ == "__main__":
    guitarra = Instrumento("Guitarra", "Cuerda")
    piano = Instrumento("Piano", "Teclado")

    orquesta = Orquesta("Orquesta Sinfónica")
    orquesta.agregar_instrumento(guitarra)
    orquesta.agregar_instrumento(piano)

    print(f"{orquesta.nombre} tiene los siguientes instrumentos:")
    for instrumento in orquesta.instrumentos:
        print(f"Instrumento: {instrumento.nombre}, Tipo: {instrumento.tipo}")

    print("Tocando los instrumentos:")
    for instrumento in orquesta.instrumentos:
        instrumento.tocar()

"""
Comprende el enunciado: Lee detenidamente el enunciado del ejercicio para comprender lo que se te está pidiendo. 
Identifica los objetos, las relaciones y las propiedades que deben ser modelados.
Identifica las clases: Determina las clases que necesitas para resolver el ejercicio. En este caso, 
las clases son Orquesta e Instrumento.
Atributos de las clases: Piensa en los atributos que deben tener cada clase. Por ejemplo, en el ejercicio 
"Una orquesta utiliza varios instrumentos", puedes pensar en un atributo de lista en la clase Orquesta para mantener 
los instrumentos que utiliza.
Métodos de las clases: Considera los métodos que deben estar disponibles en las clases. Por ejemplo, en el ejercicio, 
puedes pensar en un método en la clase Orquesta para agregar instrumentos a la orquesta.
Relaciones entre las clases: Define cómo se relacionan las clases entre sí. En este caso, una orquesta utiliza 
varios instrumentos, lo que sugiere una relación de composición donde la orquesta tiene una lista de instrumentos.
Implementa las clases y métodos: Una vez que tengas claro qué atributos y métodos debe tener cada clase, 
puedes comenzar a implementar las clases en Python.
Ejemplo de uso: Crea un ejemplo de uso para probar y demostrar cómo funcionan las clases y los métodos. 
Esto también te ayudará a verificar que tu implementación es correcta.
Prueba y depuración: Ejecuta el ejemplo de uso y asegúrate de que las clases y los métodos funcionen correctamente. 
Realiza pruebas adicionales para asegurarte de que tu implementación sea sólida.
Recuerda que la programación orientada a objetos implica la creación de objetos que representen entidades del 
mundo real y cómo interactúan entre sí. Al seguir estos pasos y pensar cuidadosamente en la modelización de tus clases, 
podrás resolver los ejercicios de manera efectiva. La práctica te ayudará a mejorar tus habilidades en 
la creación de clases y objetos.
"""