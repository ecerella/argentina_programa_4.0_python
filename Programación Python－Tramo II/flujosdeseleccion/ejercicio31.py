
"""
Una editorial determina el precio de un libro según la cantidad de páginas 
que contiene. El costo básico del libro es de $1000, más $35,10 por página 
con encuadernación rústica. Si el número de páginas supera las 300 
la encuadernación debe ser especial, lo que incrementa el costo en $1200. 
Además, si el número de páginas sobrepasa las 600 se hace necesario 
otro procedimiento de encuadernación que incrementa el costo en $880. 
Desarrollar un programa que calcule el costo de un libro dado el número 
de páginas.
En Python no existen constantes como tal, pero se utiliza una convención 
de nomenclatura en mayúsculas para indicar que una variable no debe ser 
modificada. Esto se conoce como "constante simbólica" o "constante 
convencional". Para definir una constante convencional, simplemente se 
define una variable con un nombre en mayúsculas.
Por ejemplo, para el problema anterior, se pueden definir las constantes:

COSTO_BASICO con valor 1000
COSTO_POR_PAGINA con valor 35.10
COSTO_ENC_RUSTICA con valor 1200
COSTO_ENC_ESPECIAL con valor 880.

Es una buena práctica utilizar constantes para almacenar valores fijos en 
un programa, ya que facilita la lectura del código y su mantenimiento, 
evita errores por la modificación accidental de valores y permite un 
fácil ajuste de los valores fijos en caso de ser necesario.
"""


# constantes simbólicas
COSTO_BASICO = 1000
COSTO_POR_PAGINA = 35.10
COSTO_ENC_RUSTICA = 1200
COSTO_ENC_ESPECIAL = 880

num_paginas = int(input("Ingrese el número de páginas del libro: "))

if num_paginas < 300:
    costo = COSTO_BASICO + (COSTO_POR_PAGINA * num_paginas) + COSTO_ENC_RUSTICA
elif num_paginas >300 and num_paginas < 600:
    costo = COSTO_BASICO + (COSTO_POR_PAGINA * num_paginas) + COSTO_ENC_ESPECIAL
else:
    costo = COSTO_BASICO + (COSTO_POR_PAGINA * num_paginas)

print("El costo del libro es: $", costo)
