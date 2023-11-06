
"""
Escribir un programa que permita ingresar la estatura (en metros con decimales) 
de cada jugador de un equipo de básquet La carga finalizará al ingresar cero. 
Calcular y mostrar la estatura promedio del equipo.
"""

def entrada_datos():
    lista_estatura = []
    while True:
        altura = float(input("Ingrese estatura en metros con dos decimales, para salir ingrese 0: "))
        if altura == 0:
            break
        else:
            lista_estatura.append(altura) 
    print(f"estaturas: {lista_estatura}")
    return lista_estatura



def promedio(lista_estatura):
    promedio = sum(lista_estatura) / len(lista_estatura)
    return promedio



# Llama a la función entrada_datos() para obtener la lista de estaturas
lista_estatura = entrada_datos()

# Llama a la función promedio() pasando la lista como argumento
resultado_promedio = promedio(lista_estatura)

print(f"El promedio de estaturas es: {resultado_promedio:.2f}")