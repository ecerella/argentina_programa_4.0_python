
"""
Escribir un programa que permita ingresar nombre y edad de un grupo de personas 
(para cada una, nombre y edad). La carga termina cuando en el nombre de la persona 
se ingresa un asterisco ('*'). Mostrar al final cómo se llama la persona más joven.
"""

def nombre_edad():
    personas = [] #lista vacia
    while True:
        nombre = input("Ingresa nombre de la persona, si deseas terminar ingresa (*): ")
        if nombre == "*":
            break
        edad = int(input("Ingresa la edad de la persona: "))
        personas.append((nombre, edad)) #agrego nombre y edad como tuplas en la lista

    return personas



def persona_joven(personas): #funcion que busca la persona mas joven
    joven = min(personas, key=lambda x: x[1]) #usando función lambda es decirle a min() que debe comparar las tuplas de la lista personas en función de sus edades (el segundo elemento de cada tupla).
    return joven[0]
                 
personas = nombre_edad()
mas_joven = persona_joven(personas)


print(f"La persona mas joven es: {mas_joven}")


# Sitios web como LeetCode, HackerRank y CodeSignal ofrecen una amplia 
# variedad de problemas de programación para resolver.