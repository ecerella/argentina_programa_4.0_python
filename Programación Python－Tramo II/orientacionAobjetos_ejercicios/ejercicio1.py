"""
Defina dos clases, Paciente y Médico. Un paciente puede tener asignado un médico, pero un médico puede tener muchos pacientes.
"""

class Medico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.pacientes = []  # Inicialmente, la lista de pacientes está vacía

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.medico_asignado = None  # Inicialmente, el paciente no tiene médico asignado

    def asignar_medico(self, medico):
        self.medico_asignado = medico
        medico.agregar_paciente(self)

# Crear instancias de médicos y pacientes
medico1 = Medico("Dr. García", "Cardiólogo")
medico2 = Medico("Dra. López", "Pediatra")

paciente1 = Paciente("Juan", 35)
paciente2 = Paciente("Ana", 8)

# Asignar pacientes a médicos
paciente1.asignar_medico(medico1)
paciente2.asignar_medico(medico2)

# Mostrar la información
print(f"Paciente 1 ({paciente1.nombre}) tiene asignado al médico: {paciente1.medico_asignado.nombre}")
print(f"Paciente 2 ({paciente2.nombre}) tiene asignado al médico: {paciente2.medico_asignado.nombre}")

# Ver la lista de pacientes de cada médico
print(f"El Dr. García tiene {len(medico1.pacientes)} pacientes.")
print(f"La Dra. López tiene {len(medico2.pacientes)} pacientes.")
