
"""
Una remisería requiere un sistema que calcule el precio de un viaje a partir 
de la cantidad de km que desea recorrer el usuario.

Tiene la siguiente tarifa:

Viaje mínimo $50
Si recorre entre 0 y 10km: $20/km
Si recorre 10km o más: $15/km
Escribir un programa que permita ingresar la cantidad de km que desea 
recorrer el usuario y muestre el precio del viaje.
"""

cant_kilometros = int(input("Ingrese la cantidad de kilometros recorridos: "))
viaje_minimo = 50

if cant_kilometros >= 0 and cant_kilometros <= 10:
    precio_viaje = (cant_kilometros * 20) + viaje_minimo
elif cant_kilometros >= 10:
    precio_viaje = (cant_kilometros * 15) + viaje_minimo

print(f"El precio del viaje para el usuario sera de: {precio_viaje}")
