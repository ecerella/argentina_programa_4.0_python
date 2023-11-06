"""
Escribir un programa que permita realizar varias operaciones matemáticas ingresando un caracter por cada una 
la operación a realizar (‘+’, ‘-’, ‘*’, ‘/’, ‘F’) y dos números enteros en el caso que no haya elegido ‘F’. 
La computadora debe mostrar el resultado para la operación ingresada. Considerar que no se puede dividir por cero. 
Cuando la operación ingresada sea ‘F’ nos indicará que no se desean calcular más operaciones.
"""

resultado = 0
cartel = ""

#logica
while True:

    operacion = input("operación a realizar (‘+’, ‘-’, ‘*’, ‘/’, para salir del programa: ‘F’)")

    if operacion != 'F':
        primer_numero = int(input("Ingrese el primer numero de la operacion: "))
        segundo_numero = int(input("Ingrese el segundo numero de la operacion: "))

        if operacion == '+':
            resultado = primer_numero + segundo_numero
            cartel = f"El resultado de la suma de {primer_numero} + {segundo_numero} = {resultado}"
        elif operacion == '-':
            resultado = primer_numero - segundo_numero
            cartel = f"El resultado de la suma de {primer_numero} - {segundo_numero} = {resultado}"
        elif operacion == '*':
            resultado = primer_numero * segundo_numero
            cartel = f"El resultado del producto de {primer_numero} * {segundo_numero} = {resultado}"
        elif operacion == '/':
            if segundo_numero == 0:
                print("ERROR: no se puede hacer una division por cero")
            else:
                resultado = primer_numero / segundo_numero
                cartel = f"El resultado de la division de {primer_numero} / {segundo_numero} = {resultado}"
        else:
            print("Operacion no valida! ")

        print(cartel)

    else:
        print("GRACIAS POR USAR ESTE SOFTWARE")
        break