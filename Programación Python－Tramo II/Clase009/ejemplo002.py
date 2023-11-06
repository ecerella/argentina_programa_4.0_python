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

    


def main():   
    lista_palabras = TEXTO[:].split()
    lista_palabras = limpiar(lista_palabras)
    
    lista_palabras_sin_repetir = list(set(lista_palabras))
    lista_palabras_sin_repetir.sort()
    print(lista_palabras_sin_repetir)
main()