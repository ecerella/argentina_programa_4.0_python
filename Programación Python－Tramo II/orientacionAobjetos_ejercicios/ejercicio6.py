"""
Cree clases Aeropuerto y Avión. Un aeropuerto puede tener varios aviones estacionados, 
pero un avión puede existir sin pertenecer a ningún aeropuerto.
"""

class Aeropuerto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aviones = []

    def agregar_avion(self, avion):
        self.aviones.append(avion)


class Avion:
    def __init__(self, nombre, tipo, motor):
        self.nombre = nombre
        self.tipo = tipo
        self.motor = motor

    def volar(self):
        print(f"el aeroplano: {self.nombre} tipo: {self.tipo} esta en vuelo")


if __name__ == "__main__":

    aeropuerto = Aeropuerto("Newbery")
    avion1 = Avion("Cessna", "Entrenamiento", "Piston")
    avion2 = Avion("Learjet", "Privado", "Turbina")
    avion3 = Avion("Pitts", "Acrobacia", "Piston")

    aeropuerto.agregar_avion(avion1)
    aeropuerto.agregar_avion(avion2)
    aeropuerto.agregar_avion(avion3)

    print(f"{aeropuerto.nombre} tiene los siguientes aviones:")
    for avion in aeropuerto.aviones:
        print(f"avion: {avion.nombre}, tipo: {avion.tipo}")

    print("aviones volando:")
    for avion in aeropuerto.aviones:
        avion.volar()


"""
Las instancias de Avion se crean con los argumentos correctos, como 
Avion("Cessna", "Entrenamiento", "Piston").

Las llamadas a agregar_avion se hacen con instancias de Avion, 
como aeropuerto.agregar_avion(avion1).
"""