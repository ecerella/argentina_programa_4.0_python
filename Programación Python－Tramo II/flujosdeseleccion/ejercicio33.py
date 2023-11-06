
"""
La farmacia Sindical efectúa descuentos a sus afiliados según el importe de 
la compra con la siguiente escala:

Menor de $5500.0 el descuento es del 4.5%
Entre $5500.0 y $10000.0 el descuento es del 8%
Más de $10000.0 el descuento es del 10.5%
Escribir un programa que reciba un importe e informe: el descuento y 
el precio neto a cobrar, con mensajes aclaratorios.
"""

Descuento_Menor = 0.045
Descuento_Medio = 0.08
Descuento_Alto = 0.105

importe = float(input("Ingrese el importe a abonar: "))

if importe < 5500.0:
    descuento = importe * Descuento_Menor
    descuento_txt = "Descuento_Menor = 4.5%"
elif importe >= 5500.0 and importe <= 10000.0:
    descuento = importe * Descuento_Medio
    descuento_txt = "Descuento_Medio = 8%"
else:
    descuento = importe * Descuento_Alto
    descuento_txt = "Descuento_Alto = 10.5%"

precio_neto = importe - descuento

string_usuario = f"""
*********************************************
El importe de su compra es de: $ {importe:,.2f}
*********************************************
descuento aplicado:  {descuento_txt:20}

El precio Neto:                $ {precio_neto:,.2f}
*********************************************
"""

print (string_usuario)