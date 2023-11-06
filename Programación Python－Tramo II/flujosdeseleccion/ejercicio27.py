
"""
Escribir un programa que permita ingresar una edad (entre 1 y 120 años), un género 
('F'para mujeres, 'M' para hombres) y un nombre. En caso de haber ingresado valores erróneos 
(edad fuera de rango o género inválido), informar tal situación indicando el nombre de la persona. 
Si los datos están bien ingresados el programa debe indicar, sabiendo que las mujeres se 
jubilan con 60 años o más y los hombres con 65 años o más, si la persona está en edad de jubilarse.

"""

nombre = input("Ingrese nombre de la persona: ")
genero = input("Ingrese género F para mujeres, M para hombres: ")
edad = int(input("Ingrese una edad, entre 1 y 120 años: "))

if genero != "F" and genero != "M":
    print(f"parametro Invalido en genero! para {nombre}")

elif edad <1 or edad >120:
    print(f"parametro erroneo en edad para {nombre}")

else:
    if genero == "F" and edad >= 60:
        print(f"{nombre} puede jubilarse.")
    elif genero == "M" and edad >= 65:
        print(f"{nombre} puede jubilarse.")
    else:
        print(f"{nombre} aun no puede jubilarse.")

