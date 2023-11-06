# EN ejercicio 065
"""Ejercicio 65 :

Una cadena de comida rápida solicita el desarrollo de una aplicación para sus terminales de autoservicio que permita a los clientes armar su propio menú.
Los clientes pueden elegir entre diferentes opciones de combos o pedir por separado la comida, bebida y postre.

Al iniciar la aplicación, se debe mostrar el siguiente menú de opciones:
1) Combo 1: Hamburguesa, papas fritas y gaseosa - $1550
2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - $1650
3) Hamburguesa sola - $1300
4) Hamburguesa con queso - $1400
5) Gaseosa - $700
6) Postre - $600
7) Agregar aderezo - $100
8) Terminar

Luego de seleccionar cada ítem, se debe mostrar el subtotal para que el cliente pueda decidir si desea agregar más productos a su pedido antes de terminar.

El valor mínimo del pedido debe ser de $1550. 

Si el cliente elige un combo, se debe sumar el importe total al subtotal. 

Si el cliente selecciona opciones 3 a 7, se le debe preguntar la cantidad deseada y calcular el valor total antes de sumarlo al subtotal.

Al finalizar el pedido, se debe mostrar el monto total a pagar, el ítem más caro y, si no se han seleccionado productos, mostrar un mensaje que diga "Pedido cancelado".
"""

from sys import path
path.insert(0, 'recursos/recursos')
import funciones as fun
import os

TERMINAR = 8

# Precios de los productos
PRECIOS = {
    "Combo 1: Hamburguesa papas fritas y gaseosa chica": 1550.0,
    "Combo 2: Hamburguesa con queso papas fritas y gaseosa mediana": 1650.0,
    "Hamburguesa sola": 1300.0,
    "Hamburguesa con queso": 1400.0,
    "Gaseosa": 700.0,
    "Postre": 600.0,
    "Agregar aderezo": 100.0
}


def menu(str_opciones: str) -> int:
    lista_opciones = str_opciones.split('\n')
    
    titulo_menu = fun.titulo(lista_opciones[0])  # Mover esta línea aquí
    opciones = lista_opciones[1:-1]  # Mover esta línea aquí

    # Resto del código del menú
    opcion_seleccionada = None
    subtotal = 0
    opciones_elegidas = []  # Lista para almacenar las opciones elegidas

    while True:      
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla

        print(titulo_menu)
        for index, cadena in enumerate(opciones):
            print(f"{index + 1} {cadena.strip()}")
        
        if opcion_seleccionada is not None:
            print(f"\nOpciones elegidas:\n")
            for opcion in opciones_elegidas:
                print(opcion)  # Muestra las opciones elegidas
        
        print(f"Subtotal: ${subtotal:.2f}\n")  # Muestra el subtotal actual
        print(f"{len(opciones) + 1} Terminar\n")
        
        opcion = fun.leer_entero("Ingrese una opción: ", 1, len(opciones) + 1)
        if opcion == len(opciones) + 1:  # Si elige terminar, sale del bucle
            break
        
        # Aquí debes actualizar el subtotal según la opción elegida
        opcion_seleccionada = opciones[opcion - 1].strip()
        precio_posicion = opcion_seleccionada.rfind('$')  # Encuentra la posición del precio
        if precio_posicion != -1:
            precio_opcion = float(opcion_seleccionada[precio_posicion:].strip().replace("$", "").replace(",", ""))
            subtotal += precio_opcion
            opciones_elegidas.append(opcion_seleccionada)  # Agrega la opción elegida a la lista
            
    return opcion



def main():
    subtotal = 0.0
    monto_total = 0.0
    item_mas_caro = list(PRECIOS.keys())[0]  # Inicializa item_mas_caro con la primera clave del diccionario
    pedido = []

    opciones = list(PRECIOS.keys())

    while True: 
        fun.limpiar_pantalla()  # Limpia la pantalla en cada iteración      
        print(fun.titulo("Rapi Food"))

        for i, opcion in enumerate(opciones, start=1):
            precio = PRECIOS[opcion]
            print(f"{i}) {opcion} - ${precio:.2f}")

        if subtotal > 0:
            print(f"\nSubtotal: ${subtotal:.2f}\n")

        print(f"\n{TERMINAR}) PARA CONFIRMAR SU COMPRA\n")

        opcion = fun.leer_entero("Ingrese una opción: ", 1, TERMINAR)

        if opcion == TERMINAR:
            break

        producto_elegido = opciones[opcion - 1]
        cantidad = 1

        if opcion >= 3 and opcion <= 7:
            cantidad = fun.leer_entero("Ingrese la cantidad deseada: ")

        precio_producto = PRECIOS[producto_elegido]
        subtotal += precio_producto * cantidad
        pedido.append(f"{producto_elegido} x{cantidad}")

        if precio_producto > PRECIOS[item_mas_caro]:
            item_mas_caro = producto_elegido

    if subtotal < 1550.0:
        print("El valor mínimo del pedido debe ser de $1550.")
        return

    print("\nPedido:")
    for item in pedido:
        print(item)

    print(f"\nSubtotal: ${subtotal:.2f}\n")

    monto_total = subtotal
    print(f"\nMonto total a pagar: ${monto_total:.2f}")
    print(f"Ítem más caro: {item_mas_caro}")

    if not pedido:
        print("Pedido cancelado")


main()