
"""
Escribir un programa que calcule y muestre el sueldo neto de un empleado 
en base a su sueldo básico y su antigüedad en años. Si es soltero se le 
incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, 
mientras que si es casado se le incrementa el sueldo en 7% del salario bruto 
por cada año de antigüedad. También se le realizan los siguientes descuentos:

Jubilación: 11%
Obra Social: 3%
Sindicato: 3%

Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y 
estado civil (S: Soltero / C: Casado). Se debe informar: 
(reemplazando los 9 por los valores que correspondan)
Estado Civil: Soltero/Casado Sueldo básico: $ 999.99 Antigüedad: 99 años

Descuentos:

Jubilación - 999,99
Obra Social - 999,99
Sindicato - 999,99
Sueldo Neto 999,99
"""

sueldo_basico = float(input("Ingrese su sueldo basico: "))
antiguedad = int(input("Ingrese el valor de antiguedad: "))
estado_civil = input("Necesito su estado civil, S para soltero o C para casado ")


if estado_civil == "S":
    sueldo_neto = sueldo_basico + (sueldo_basico * antiguedad * 0.05)
    estado_civil_txt = "Soltero"
elif estado_civil == "C":
    sueldo_neto = sueldo_basico + (sueldo_basico * antiguedad * 0.07)
    estado_civil_txt = "Casado"
else:
    print("valor de estado civil incorrecto!")
    exit()

descuento_Jubilación = sueldo_neto * 0.11
descuento_ObraSocial = sueldo_neto * 0.03
descuento_Sindicato = sueldo_neto * 0.03

sueldo_neto -= (descuento_Jubilación + descuento_ObraSocial + descuento_Sindicato)

string_usuario = f"""
*********************************************
Estado Civil: {estado_civil_txt}
*********************************************
sueldo basico:             $ {sueldo_basico:.2f}
antiguedad:                  {antiguedad} años.

Descuentos:
jubilacion:                $ {descuento_Jubilación:.2f}
Obra Social:               $ {descuento_ObraSocial:.2f}
Sindiato:                  $ {descuento_Sindicato:.2f}
*********************************************
Sueldo Neto:               $ {sueldo_neto:.2f}
"""

print(string_usuario)