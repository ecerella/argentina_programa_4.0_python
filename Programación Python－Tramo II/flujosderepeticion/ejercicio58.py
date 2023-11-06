
"""
Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:

Aplica el precio base a la primera docena de unidades.
Aplica un 10% de descuento a todas las unidades entre 13 y 100.
Aplica un 25% de descuento a todas las unidades por encima de las 100.

Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. 
El cálculo resultante sería:

100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04

Escribir un programa que lea la cantidad solicitada de un producto y su precio base, y
muestre el valor total de la venta y el precio promedio por unidad.
El fin de carga se determina ingresando -1 como cantidad solicitada.

Al finalizar informar:
a- Cantidad de ventas realizadas total.
b- Cantidad de ventas que se aplicaron un 10% de descuento.
c- Cantidad de ventas que SOLO se aplicó el precio base, no se le realizaron descuentos
"""

def calcular_precio(cantidad):
    precio_base = 100

    if cantidad <= 12:
        return cantidad * precio_base
    elif cantidad <= 100:
        return 12 * precio_base + (cantidad - 12) * precio_base * 0.9
    else:
        return 12 * precio_base + 88 * precio_base * 0.9 + (cantidad - 100) * precio_base * 0.75


def main():
    ventas_descuento_10 = 0
    ventas_sin_descuento = 0
    precio_total_ventas = 0
    ventas_totales = 0
    unidades_vendidas = 0

    while True:
        cantidad = int(input('Ingrese la cantidad de unidades que desea comprar (para salir ingrese -1): '))
        if cantidad == -1:
            print("Gracias por visitarnos!")
            break

        precio_venta = calcular_precio(cantidad)
        precio_total_ventas += precio_venta
        ventas_totales +=1
        unidades_vendidas += cantidad

        if cantidad <= 12:
            ventas_sin_descuento += 1
        elif cantidad <= 100:
            ventas_descuento_10 += 1

    if ventas_totales > 0:
        precio_promedio = precio_total_ventas / unidades_vendidas
        print(f"Valor total de la venta: {precio_total_ventas:.2f}")
        print(f"Precio promedio por unidad: {precio_promedio:.2f}")
        print(f"Cantidad de ventas realizadas total: {ventas_totales}")
        print(f"Cantidad de ventas con un 10% de descuento: {ventas_descuento_10}")
        print(f"Cantidad de ventas sin descuento: {ventas_sin_descuento}")
    else:
        print("No se realizaron ventas.")


main()
