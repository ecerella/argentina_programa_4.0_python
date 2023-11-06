from sys import path
path.insert(0,'recursos/')
from datos import TEXTO


def limpiar(lista:list[str])->list[str]:
    nueva_lista = []
    for palabra in lista:
        nueva_palabra=''
        for letra in palabra:
            letra = letra.lower()
            if letra.isalnum():
                nueva_palabra += letra  
        nueva_lista.append(nueva_palabra)        
    return nueva_lista

    
def orden_cantidad(t:tuple)->int:
    # palabra,cantidad = t
    #  0       1
    return t[1]

def main():       
    lista_palabras = limpiar(TEXTO[:].split())
    dic= {}
    for palabra in lista_palabras:
        if palabra in dic:
            dic[palabra]+=1
        else:
            dic[palabra] = 1
    
    """for palabra ,cantidad in dic.items():
        print(f'{palabra} {cantidad}')"""
    
    
    """for palabra in sorted(dic.keys()):
        print(f'{palabra} {dic[palabra]}')
"""

    for palabra,cantidad in sorted(dic.items(),key=orden_cantidad,reverse=True):
        print(f'{palabra} {cantidad}')

main()