
"""
Una cadena de comida rápida solicita el desarrollo de una aplicación para sus 
terminales de autoservicio que permita a los clientes armar su propio menú. 
Los clientes pueden elegir entre diferentes opciones de combos o pedir por 
separado la comida, bebida y postre.

Al iniciar la aplicación, se debe mostrar el siguiente menú de opciones:

Combo 1: Hamburguesa, papas fritas y gaseosa - $1550
Combo 2: Hamburguesa con queso, papas fritas y gaseosa - $1650
Hamburguesa sola - $1300
Hamburguesa con queso - $1400
Gaseosa - $700
Postre - $600
Agregar aderezo - $100
Terminar

Luego de seleccionar cada ítem, se debe mostrar el subtotal para que el cliente
pueda decidir si desea agregar más productos a su pedido antes de terminar.

El valor mínimo del pedido debe ser de $1550. Si el cliente elige un combo, 
se debe sumar el importe total al subtotal. Si el cliente selecciona opciones 
3 a 7, se le debe preguntar la cantidad deseada y calcular el valor total 
antes de sumarlo al subtotal.

Al finalizar el pedido, se debe mostrar el monto total a pagar, el ítem más 
caro y, si no se han seleccionado productos, mostrar un mensaje que diga 
"Pedido cancelado".
"""

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def obtener_formatos():
    formatos = {
        "encabezado": """
        ****************************************************************
        **                  Cadena de comida rapida                   **
        ****************************************************************
        """,
        "menu": """
        1 Combo 1: Hamburguesa, papas fritas y gaseosa.............$1550
        2 Combo 2: Hamburguesa con queso, papas fritas y gaseosa...$1650
        3 Hamburguesa sola.........................................$1300
        4 Hamburguesa con queso....................................$1400
        5 Gaseosa..................................................$700
        6 Postre...................................................$600
        7 Agregar aderezo..........................................$100

        8 Terminar
        """,
        "pedido_subtotal": """
        | pedido:            |   subtotales   |
        | ------------------ |    ---------   |       
        |                    | $ {sub_total:>12} |
        9 Agregar productos a su pedido
        """,
        "resultados": """
        | pedido:            |   subtotales   |
        | ------------------ |    ---------   | 
        |             Total  | $ {monto_total:>12} |
        |                    |                |
          item mas caro: {item_mas_caro:>12} 
        """}
    
    return formatos


def calcular_total(pedido, menu_dict):

    precio_total = sum(menu_dict[item[0]]["precio"]*item[1] for item in pedido)
    return precio_total


def mostrar_subtotal(pedido, menu_dict):
    subtotal = calcular_total(pedido, menu_dict)
    print(f"Subtotal: ${subtotal}")

    return subtotal


def main():
    formato = obtener_formatos()

    menu_dict = {
    "1": {"nombre": "Combo 1: Hamburguesa, papas fritas y gaseosa", "precio": 1550},
    "2": {"nombre": "Combo 2: Hamburguesa con queso, papas fritas y gaseosa", "precio": 1650},
    "3": {"nombre": "Hamburguesa sola", "precio": 1300},
    "4": {"nombre": "Hamburguesa con queso", "precio": 1400},
    "5": {"nombre": "Gaseosa", "precio": 700},
    "6": {"nombre": "Postre", "precio": 600},
    "7": {"nombre": "Agregar aderezo", "precio": 100},
    "8": {"nombre": "Terminar", "precio": 0},}

    pedido = []
    subtotal = 0

    clear_console()
    print(formato["encabezado"])

    while True:
        print(formato["menu"])
        mostrar_subtotal(pedido, menu_dict)

        eleccion = input("Elija una opcion del menu: ")
        if eleccion in menu_dict:
            if eleccion in ["3", "4", "5", "6", "7"]:
                cantidad = int(input(f"Ingrese la cantidad de '{menu_dict[eleccion]['nombre']}': "))
                precio_item = menu_dict[eleccion]["precio"] * cantidad
                pedido.append((eleccion, cantidad))
                subtotal += menu_dict[eleccion]["precio"]*cantidad
            else:
                pedido.append((eleccion, 1))  # Por defecto, cantidad es 1 para otras opciones
                subtotal += menu_dict[eleccion]["precio"]
            mostrar_subtotal(pedido, menu_dict)
        else:
            print("Entrada invalida, vuelva a seleccionar un item.")

        if eleccion == "8":
            if subtotal < 1550:
                    print("El valor mínimo del pedido es de $1550. Agregue más productos.")
            else:
                break
        
    clear_console()
    print("Resumen de pedido:")
    for item, cantidad in pedido:
        nombre_item = menu_dict[item]["nombre"]
        if cantidad > 1:
            print(f"{nombre_item} (x{cantidad})")
        else:
            print(nombre_item)

    precio_total = calcular_total(pedido, menu_dict)
    if precio_total > 0:
        print(f"Total a pagar: ${precio_total}")
    else:
        print("Pedido cancelado.")

    # Mostrar resultados finales utilizando el formato "resultados"
    resultado_formato = obtener_formatos()["resultados"]
    detalle_subtotal = mostrar_subtotal(pedido, menu_dict)
    item_mas_caro = max(pedido, key=lambda item: menu_dict[item[0]]["precio"])
    print(resultado_formato.format(detalle_subtotal=detalle_subtotal, monto_total=precio_total, item_mas_caro=menu_dict[item_mas_caro[0]]["nombre"]))


main()
