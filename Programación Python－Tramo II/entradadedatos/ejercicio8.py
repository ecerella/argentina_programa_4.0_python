
dias_habiles = 5
valor_hora = float(input("Ingrese el valor de una hora de trabajo: "))
horas_trabajadas_por_dia = float(input("Ingrese la cantidad de horas trabajadas:"))

salario_diario = valor_hora * horas_trabajadas_por_dia
salario_semanal = salario_diario * dias_habiles
horas_sabado = horas_trabajadas_por_dia / 2

salario_horas_sabado = valor_hora * horas_sabado

salario_total_semanal = salario_semanal + salario_horas_sabado

print("El salario semanal es:", salario_total_semanal)