
"""
Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, 
más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas. 
Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde 
en un determinado mes.
Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y 
el valor total de las mismas.
¿Sobran datos? ¿Qué datos sobran?
"""

SALARIO_BASE = 100000
COMISION_FIJA_POR_VENTA = 5000
comision_ventas = 0.05

vendedor = input("Ingrese el nombre del vendedor: ")
cantidad_ventas = int(input("Ingrese la cantidad de ventas del vendedor: "))
importe_total_ventas = float(input("Ingrese el importe total de las ventas: "))

comision_por_ventas = importe_total_ventas * comision_ventas
total_comision_fija = COMISION_FIJA_POR_VENTA * cantidad_ventas

salario = SALARIO_BASE + comision_por_ventas + total_comision_fija

print(f"""
      Nombre del vendedor: {vendedor}
      Salario: {salario}
""")
