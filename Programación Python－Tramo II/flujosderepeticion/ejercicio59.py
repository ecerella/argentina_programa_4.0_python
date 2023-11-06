
"""
Escribir un programa para un negocio de venta de granos que desea controlar las ventas realizadas. 
De cada venta ingresa el importe total y un código que indica la forma de pago. Los códigos puede ser:

C: cheque, 20% de recargo.
E: efectivo, 10% de descuento.
T: con tarjeta, 12% de recargo.
Se debe ingresar una F para finalizar el día de venta y arrojar los siguientes totales.

| Forma de Pago    | Total     |
| ---------------- | --------- | 
| Efectivo en Caja | $ xxxx.xx |
| Tarjeta Crédito  | $ xxxx.xx |
| Cheques          | $ xxxx.xx |
| Total de Venta   | $ xxxx.xx |
| Importe del IVA  | $ xxxx.xx |

"""

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def obtener_formatos():
    formatos = {
        "encabezado": """
        ****************************************************************
        **                    FORRAJERIA BELgranos                    **
        ****************************************************************
        """,
        "opciones_pago": """
        ****************************************************************
        **     opciones de pago:     C: cheque, 20% de recargo.       **
        **                           E: efectivo, 10% de descuento.   **
        **                           T: con tarjeta, 12% de recargo.  **
        **                           F: finaliza las entradas.        **
        ****************************************************************
        """,
        "resultados": """
    | Forma de Pago    |      Total     |
    | ---------------- |    ---------   | 
    | Efectivo en Caja | $ {efectivo:>12,.2f} |
    | Tarjeta Crédito  | $ {tarjeta:>12,.2f} |
    | Cheques          | $ {cheque:>12,.2f} |
    | Total de Venta   | $ {ventas_total:>12,.2f} |
    | Importe del IVA  | $ {iva:>12,.2f} |
    """
    }
    return formatos


def main():

    ventas_total = 0
    efectivo = 0
    tarjeta = 0
    cheque = 0

    while True:
        formatos = obtener_formatos()
        clear_console()
        print(formatos["encabezado"])
        print("\n")

        importe = float(input("Ingrese el importe total de la venta: "))

        print(formatos["opciones_pago"])
        print("\n")

        forma_pago = input("Elija opcion de pago (C, E, T o F)").upper()

        if forma_pago == "F":
            break
        elif forma_pago == "C":
            cheque = importe + (importe * 0.2)
        elif forma_pago == "E":
            efectivo = importe - (importe * 0.1)
        elif forma_pago == "T":
            tarjeta = importe + (importe * 0.12)
        else:
            print("solo las opciones disponibles por favor")
 
        ventas_total += importe
        iva = ventas_total * 0.21

    clear_console()
    print(formatos["encabezado"])
    print("\n")
    print(formatos["resultados"].format(
        efectivo=efectivo,
        tarjeta=tarjeta,
        cheque=cheque,
        ventas_total=ventas_total,
        iva=iva
    ))

main()


