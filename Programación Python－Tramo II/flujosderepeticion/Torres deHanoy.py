def print_towers(towers):
    max_height = max(len(tower) for tower in towers)
    tower_spacing = 4  # Espacio horizontal entre las torres

    for level in range(max_height, 0, -1):
        row = ""
        for tower in towers:
            if len(tower) >= level:
                disc_width = tower[level - 1]
                disc = "*" * (disc_width * 2 - 1)  # Representa el disco con asteriscos
                row += disc.center(max_height * 2 + 1)
            else:
                row += "|".center(max_height * 2 + 1)  # Torre vacía
            row += " " * tower_spacing  # Agrega espacios horizontales entre las torres

        print(row)

# Solicitar al usuario el número de discos
num_discos = int(input("Ingrese el número de discos: "))

# Inicializar las torres
torres = [[] for _ in range(3)]
torres[0] = list(range(num_discos, 0, -1))

while True:
    print_towers(torres)
    
    # Solicitar movimiento al usuario
    from_tower = input("Mover desde la torre (A, B, C): ").upper()
    to_tower = input("Mover a la torre (A, B, C): ").upper()

    if from_tower not in ["A", "B", "C"] or to_tower not in ["A", "B", "C"]:
        print("Entrada no válida. Use A, B o C para las torres.")
        continue

    from_tower_index = ord(from_tower) - ord("A")
    to_tower_index = ord(to_tower) - ord("A")

    if not torres[from_tower_index]:
        print("La torre de origen está vacía.")
        continue

    if not torres[to_tower_index] or torres[to_tower_index][-1] > torres[from_tower_index][-1]:
        disc = torres[from_tower_index].pop()
        torres[to_tower_index].append(disc)
    else:
        print("Movimiento no válido. El disco más grande debe estar en la parte inferior.")

    if torres[2] == list(range(num_discos, 0, -1)):
        print("¡Felicidades, has ganado!")
        break  # Sale del bucle si has ganado