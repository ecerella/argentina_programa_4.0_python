"""
Escribir un programa que permita validar una opción ingresada. 
Se le preguntará al usuario si desea continuar con alguna operación de la forma 
"¿Deseás continuar? [S/N]". Se espera que el usuario ingrese una 'S' o una 'N' 
(incluir las minúsculas). La opción debe ser ingresada tanto como sea necesario hasta que 
quede comprendida dentro de las posibilidades esperadas.
"""

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Llama a la función para limpiar la consola
clear_console()


print(f"""
      ******************************************************
      ** Estas solo, perdido, en una noche de luna llena  **
      ** tu espiritu aventura desaparece mientras aumenta **
      ** la desesperacion... el camino se divide y te da  **
      ** dos opciones una casa y seguir sendero al bosque **
      ******************************************************
      """)
casa = input("Entrar a la casa? [S/N]")
if casa == 'S':
    clear_console()
    print(f"""
      ******************************************************
      **   TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT  **
      **   I                                           I  **
      **   I   T---------T    T-----T    T---------T   I  **
      **   I   I         I    I     I    I         I   I  **
      **   I   I         I    I     I    I         I   I  **
      **   I   I         I    I     I    I         I   I  **
      **   I   -----------    I     I    -----------   I  **
      **   I                  I     I                  I  **
      ******************************************************
          Bienvenido a la casa de El gaucho zonda!
          espero no este en casa,
          tiende a echarte con la honda!
      """)
else:
    bosque = input("Seguir sendero al bosque? [S/N]")
    print(f"""
      ******************************************************
            *            +                *            *
           **           **               **           **
          ***           **              ****         ***
         *****         ****            ******       *****
        *******      *******         *********     ********
          I I          I I             I I            II    
      **********    **********    ************    **********
          Bienvenido al camino del bosque oscuro
          tene cuidado con los caminos te hacen
          perder hasta el rumbo!
          """)