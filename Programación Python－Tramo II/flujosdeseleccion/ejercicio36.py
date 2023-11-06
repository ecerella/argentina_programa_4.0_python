
"""
Escribir un programa que permita ingresar dos números enteros y la operación 
a realizar('+', '-', '*', '/'). Debe mostrarse el resultado para la operación 
ingresada. Considerar que no se puede dividir por cero 
(en ese caso mostrar el texto 'ERROR').
"""

primer_numero = int(input("Ingrese un primer numero: "))
segundo_numero = int(input("Ingrese un segundo numero: "))
operacion = input("Ingrese la operacion a realizar ('+', '-', '*', '/') ")

if operacion == '+':
    resultado = primer_numero + segundo_numero
    resultado_txt = f"El resultado de la suma de los numeros es: {resultado}"
elif operacion == '-':
    resultado = primer_numero - segundo_numero
    resultado_txt = f"El resultado de la resta de los numeros es: {resultado}"
elif operacion == '*':
    resultado = primer_numero * segundo_numero
    resultado_txt = f"El resultado de la multiplicacion de los numeros es: {resultado}"
elif operacion == '/':
    if segundo_numero == 0:
        print("ERROR: No puedo dividir por cero")
    else:
        resultado = primer_numero / segundo_numero
        resultado_txt = f"El resultado de la uma de los numeroas es: {resultado}"
else:
    print("Ingrese un operador correcto!")
exit()

print(resultado_txt)