
"""
Ejercicio 026
Escribir un programa que permita ingresar la cantidad de invitados 
a una fiesta y la cantidad de asientos disponibles en el salon. 
Debes indicar si alcanzan los asientos, 
Si los asientos no alcanzaran indicar cuántos faltan para que 
todos los invitados puedan sentarse.
"""

cantidad_invitados = 20
cantidad_asientos = 12

if cantidad_invitados <= cantidad_asientos:
    print("¡Los asientos alcanzan para todos")
else:
    faltan_asientos = cantidad_invitados - cantidad_asientos
    print(f"Faltan {faltan_asientos} asientos para que los invitados puedan sentarse.")
