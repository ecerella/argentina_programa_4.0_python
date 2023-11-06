"""
Realizá un programa que permita ingresar el monto total de las ventas realizadas por un
vendedor durante el mes, de quien se sabe que gana un sueldo fijo de 44000 pesos más el 16
por ciento del monto total vendido. Con tales datos debes calcular y mostrar el importe a
cobrar por el vendedor.
"""

SUELDO_FIJO = 44000
total_ventas = float(input("ingresa venta mensual total del vendedor: "))
porcentaje_ventas = total_ventas * 0.16
sueldo_total = SUELDO_FIJO + porcentaje_ventas
print ("el valor de sueldo total es de:", sueldo_total, "pesos.")
