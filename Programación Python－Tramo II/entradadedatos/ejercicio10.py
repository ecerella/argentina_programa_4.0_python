
inversion_persona1 = float(input("Ingrese la cantidad invertida por la persona 1:"))
inversion_persona2 = float(input("Ingrese la cantidad invertida por la persona 2:"))
inversion_persona3 = float(input("Ingrese la cantidad invertida por la persona 3:"))

total_inversion = inversion_persona1 + inversion_persona2 + inversion_persona3

porcentaje_inversion_persona1 = round((inversion_persona1 / total_inversion) * 100, 2)
porcentaje_inversion_persona2 = round((inversion_persona2 / total_inversion) * 100, 2)
porcentaje_inversion_persona3 = round((inversion_persona3 / total_inversion) * 100, 2)

formato = f"Inversion persona1: {porcentaje_inversion_persona1} \nInversion persona2: {porcentaje_inversion_persona2} \nInversion persona3: {porcentaje_inversion_persona3}"
print (formato)