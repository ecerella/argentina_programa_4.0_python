
"""
Escribir un programa que permita resolver el siguiente problema:
Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado
y qué porcentaje aportó cada una (indicando nombre y porcentaje).
Solicitar la carga por teclado del nombre de cada socio y su capital aportado,
a partir de esto calcular e informar lo requerido previamente.
"""
nombre_persona1 = input("Ingrese nombre de la persona 1:")
inversion_persona1 = float(input("Ingrese la cantidad invertida por la persona 1:"))
nombre_persona2 = input("Ingrese nombre de la persona 2:")
inversion_persona2 = float(input("Ingrese la cantidad invertida por la persona 2:"))
nombre_persona3 = input("Ingrese nombre de la persona 3:")
inversion_persona3 = float(input("Ingrese la cantidad invertida por la persona 3:"))

total_inversion = inversion_persona1 + inversion_persona2 + inversion_persona3

porcentaje_inversion_persona1 = round((inversion_persona1 / total_inversion) * 100, 2)
porcentaje_inversion_persona2 = round((inversion_persona2 / total_inversion) * 100, 2)
porcentaje_inversion_persona3 = round((inversion_persona3 / total_inversion) * 100, 2)

formato = f"""
{nombre_persona1} invierte {inversion_persona1} pesos, su porcentaje de inversion es: {porcentaje_inversion_persona1} 
{nombre_persona2} invierte {inversion_persona2} pesos, su porcentaje de inversion es: {porcentaje_inversion_persona2}
{nombre_persona3} invierte {inversion_persona3} pesos, su porcentaje de inversion es: {porcentaje_inversion_persona3}
"""
print (formato)