from sys import path  
path.append('recursos/')
import funciones as fun


def es_binario(num:str) -> bool:                    #Esta funcion verifica si el numero es binario
    for elem in num:
        if elem != '1' and elem != '0':
            return False
    return True

def es_hexa(num:str) -> bool:                       #Esta funcion verifica si el numero es hexadecimal
    for elem in num:
        if not elem.isnumeric() and not elem in ('A','B','C','D','E','F','a','b','c','d','e','f') :
            return False
    return True

def leer_binario(msg:str)->str:                     #Sirve para leer numeros binarios
    ok = True
    while ok:
        binario = input(msg)
        if es_binario(binario):
            ok = False
        else:
            print('Ingrese un numero binario valido!')
    return binario

def leer_hexa(msg:str)->str:                        #Sirve para leer numeros hexadecimales
    ok = True
    while ok:
        hexa = input(msg)
        if es_hexa(hexa):
            ok = False
        else:
            print('Ingrese un numero hexadecimal valido!')
    return hexa

def decimal_binario_entero(numero:int) -> str:      #Recibe un numero decimal y lo convierte a binario
    resto = ''
    if numero == 0:
            return '0'
    while True:
        resto += str(numero%2)
        numero //= 2
        if numero == 1:
            resto += str(numero)
            break
    resultado = resto[::-1]
    return resultado

def binario_decimal(numero:str) ->int:              #Recibe un numero binario y lo convierte a decimal
    vuelta = numero[::-1]
    c = 0
    resultado = 0
    for elemento in vuelta:
        resultado += int(elemento)*2**c
        c += 1
    return int(resultado)

def decimal_hexadecimal_entero(num:int) -> str:     #Recibe un numero decimal y lo convierte a hexadecimal
    resto = ''
    if num < 16:
        if num == 10:
            return 'A'
        elif num == 11:
            return 'B'
        elif num == 12:
            return 'C'
        elif num == 13:
            return 'D'
        elif num == 14:
            return 'E'
        elif num == 15:
            return 'F'
        elif num < 10:
            return num
    while True:
        if num%16 == 10:
            resto += 'A'
        elif num%16 == 11:
            resto += 'B'
        elif num%16 == 12:
            resto += 'C'
        elif num%16 == 13:
            resto += 'D'
        elif num%16 == 14:
            resto += 'E'
        elif num%16 == 15:
            resto += 'F'
        elif num%16 < 10:
            resto += str(num%16)
        num //= 16
        if num < 16:
            if num == 10:
                resto += 'A'
            elif num == 11:
                resto += 'B'
            elif num == 12:
                resto += 'C'
            elif num == 13:
                resto += 'D'
            elif num == 14:
                resto += 'E'
            elif num == 15:
                resto += 'F'
            elif num < 10:
                resto += str(num%16)
            break
    resultado = resto[::-1]
    return resultado

def hexadecimal_decimal(num:str) ->int:         #Recibe un hexadecimal y lo convierte a decimal
    vuelta = num[::-1]
    c = 0
    resultado = 0
    for elemento in vuelta:
        if elemento in ('a','A'):
            resultado += 10*16**c
        elif elemento in ('b','B'):
            resultado += 11*16**c
        elif elemento in ('c','C'):
            resultado += 12*16**c
        elif elemento in ('d','D'):
            resultado += 13*16**c
        elif elemento in ('e','E'):
            resultado += 14*16**c
        elif elemento in ('f','F'):
            resultado += 15*16**c
        else:
            resultado += int(elemento)*16**c
        c += 1
    return int(resultado)


def main():
    numero = fun.leer_entero('Ing. un numero decimal: ')
    print(decimal_binario_entero(numero))
    numero = leer_binario('Ing. un numero binario: ')
    print(binario_decimal(numero))
    numero = fun.leer_entero('Ing. un numero decimal: ')
    print(decimal_hexadecimal_entero(numero))
    numero = leer_hexa('Ing. un hexadecimal: ')
    print(hexadecimal_decimal(numero))


main()











