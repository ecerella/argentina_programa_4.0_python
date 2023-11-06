from sys import path
path.insert(0,'recursos/')
from datos import ARTICULOS_ALMACEN

def filtrar(articulos:list,filtro:str)->list:
    lista_salida = []
    # (codigo, nombre, precio,categoria)
    for codigo, nombre, precio,categoria in articulos:
        if filtro == categoria:
            lista_salida.append([codigo, nombre, precio])

    return lista_salida

def orden_precio(dato:tuple)->float:
    return dato[2]
def orden_categoria(dato:tuple)->str:
    return dato[3]
def orden_nombre(dato:tuple)->str:
    return dato[1]
def orden_codigo(dato:tuple)->str:
    return dato[0]

def main():
    articulos = ARTICULOS_ALMACEN[:]
    alm = filtrar(articulos,'ref')
    alm.sort(key=orden_precio,reverse=True)
    
    # print( ("2003", "Huevos", 2.50, "ref")  >  ("2003", "Huevos", 100.00, "alm"))
    for codigo, nombre, precio in alm:
        print(f"{codigo:10} {nombre[:30]:30} {precio:10.2f}")
main()


