"""
Implementar la clase CajaFuerte, que recibe en su constructor la cantidad de objetos que puede contener, y tiene el siguiente comportamiento:

c = CajaFuerte(12345,20)    
c.abrir(12345)
c.poner("Reloj")
c.poner("Cadena")
c.poner(1000)
c.cerrar()
c.poner("Reloj Oro") ==> ValueError ("La caja esta cerrada")
c.abrir(3456) ==> ValueError ("Error en la clave")
c.abrir(12345)
c.sacar("Cadena")
c.sacar("Tortuga")  ==> ValueError ("El objeto Tortuga no esta en la caja")
c.abrir(12345) ==> ValueError("La caja esta abierta")
c.cerrar()

"""