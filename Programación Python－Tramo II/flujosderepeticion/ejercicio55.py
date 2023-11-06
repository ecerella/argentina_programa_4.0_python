
"""
Escribir un programa que permita para cada cliente que va al banco "Express"
indicar su número de documento y aguardar a ser atendido, cuando finaliza la 
atención del día se ingresa -1 para indicar que no hay más clientes.
El banco desea saber quién fue el primer cliente atendido y quién fue el último.
"""


def ClientesBanco():

  clientes = []
  while True:
    print(f"""
      *****************************
        Bienvenido al EXPRESSbank
      *****************************
      """)
    nombre = input("Ingrese su nombre: ")
    documento = input("Ingrese su documento (-1 para finalizar): ")
    if documento == "-1":
      break
    else:
      clientes.append((nombre, documento)) #doble parentesis para almacenar como tupla

  return clientes



def PrimerUltimoCliente():
  clientesTotal = ClientesBanco()
  if clientesTotal: #verifica que haya clientes en la lista
    primer_cliente = clientesTotal[0] #el primero de la lista
    ultimo_cliente = clientesTotal[-1] #el ultimo de la lista

    print(f"""
    *****************************
           EXPRESSbank
    *****************************
    el primer cliente fue: {primer_cliente}
    el ultimo cliente fue: {ultimo_cliente}
    """)
  else:
    print("no hubo clientes hoy.")



PrimerUltimoCliente()








