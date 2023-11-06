
"""
Un animal en rehabilitación después de una cirugía requiere ser alimentado y 
monitoreado en un zoológico. Se alimenta al animal 3 veces al día y se le 
da de comer hasta que ya no tenga ganas de comer.

Por cada tanda de comida, se debe ingresar la cantidad de alimento en kg 
(número entero) que se le dio y se le debe preguntar al animal si quiere 
seguir comiendo ('S', 'N').

Se desea conocer:
Cuál de las 3 comidas fue la que el animal comió más cantidad de alimento 
y cuánto fue esa cantidad.
El total en kg de alimento recibido.
Promedio de alimento por tanda.
"""

def comida_ilimitada():
    cantidad_comidas = []
    total_alimento = 0

    for dia in range(1, 4):
        cantidad = 0
        for comida in range(1, 4):
            alimento = int(input(f"Dia {dia}, Comida {comida}: Cantidad de alimento en kg: "))
            cantidad += alimento
            hambre = input("El animal quiere seguir comiendo ('S' o 'N'): ")
            if hambre == 'N':
                break
        cantidad_comidas.append(cantidad)
        total_alimento += cantidad

    promedio = total_alimento / 9 #9comidas total

    comida_max = max(cantidad_comidas)
    comida_max_dia = cantidad_comidas.index(comida_max) +1

    return comida_max_dia, comida_max, total_alimento, promedio


def main():
    comida_maxima_dia, comida_maxima, total_alimento, promedio_alimento = comida_ilimitada()


    print(f"El día {comida_maxima_dia} fue cuando el animal comió más cantidad de alimento ({comida_maxima} kg).")
    print(f"El total en kg de alimento recibido es: {total_alimento} kg.")
    print(f"El promedio de alimento por tanda es: {promedio_alimento:.2f} kg por comida.")


main()