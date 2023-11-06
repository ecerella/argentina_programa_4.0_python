"""
Crea un diccionario donde las llaves sean las diferentes categorías de productos ("ref" para refrigerados, "alm" para alimentos no refrigerados, "lim" para limpieza, "per" para productos personales), y los valores sean listas de los nombres de los productos en esa categoría.

("2002", "Huevos", 2.50, "ref")

{"ref":['Huevos','Carne],'alm':["Pan","fideos",]}

"""


import sys

sys.path.insert(0, 'recursos/')
import datos

def crear_dicc(lista_productos: list) -> dict:
    dic_cat = {}
    for _, nombre, _, ref in lista_productos:
        if ref in dic_cat.keys():
            dic_cat[ref].append(nombre)
        else:
            dic_cat[ref] = [nombre]
    return dic_cat

def precio_promedio_por_ref(lista_productos:list)->dict:
    dic = {}
    """
    {
        'ref': {
            'suma':0,
            'cont':0
        }
        'ref': {
            'suma':0,
            'cont':0
        }
    }
    """
    for _, _, precio, ref in lista_productos:
        if ref in dic.keys():
            dic[ref]['suma'] += precio
            dic[ref]['cont'] += 1
        else:
            dic[ref] = {'suma':precio,'cont': 1}

    for ref, dic_info in dic.items():   
        dic[ref] = dic_info['suma']/dic_info['cont']     
    
    return dic

def precio_promedio_por_categoria(lista_productos: list[tuple]) -> dict:
    precios_promedio = {}
    for _, _, precio, ref in lista_productos:
        if ref in precios_promedio:
            precios_promedio[ref]["sum_precios"] += precio
            precios_promedio[ref]["cantidad"] += 1
            precios_promedio[ref]["promedio"] = precios_promedio[ref]["sum_precios"] / precios_promedio[ref]["cantidad"]
        else:
            precios_promedio[ref] = {"sum_precios": precio, "cantidad": 1, "promedio": precio}
    return precios_promedio


def main():
    
    lista_productos = datos.ARTICULOS_ALMACEN[:]
    dic = crear_dicc(lista_productos)
    print(dic)
    for ref,precio in precio_promedio_por_ref(lista_productos).items():
        print(f"{ref:5} ${precio:8.2f}")


main()
