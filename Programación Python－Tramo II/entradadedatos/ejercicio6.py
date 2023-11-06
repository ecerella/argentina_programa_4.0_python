
nota1 = int(input("Ingrese la primer nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

promedio = float((nota1 + nota2 + nota3)/3)

format = f"NOTAS: {nota1}, {nota2}, {nota3} \nPROMEDIO: {promedio}"
print(format)