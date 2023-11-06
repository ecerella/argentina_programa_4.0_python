"""
Defina clases Empresa y Empleado. Una empresa tiene varios empleados,
pero un empleado trabaja en una sola empresa.
"""

class Empresa():
    def __init__(self, nombre, rubro):
        self.nombre = nombre
        self.rubro = rubro
        self.empleados = []

    def empleados_empresa(self, nombre, puesto):
        empleado = Empleado(nombre, self, puesto)
        self.empleados.append(empleado)
        return empleado

class Empleado():
    def __init__(self, nombre, empresa, puesto):
        self.nombre = nombre
        self.empresa = empresa
        self.puesto = puesto

def main():
    empresa1 = Empresa("Nestle", "alimentos")
    empresa2 = Empresa("cocacola", "alimentos")
    empleado1 = empresa1.empleados_empresa("ezequiel", "maquinista")
    empleado2 = empresa1.empleados_empresa("toto", "oficina")
    empleado2 = empresa2.empleados_empresa("pepitito", "ventas")
    empleado3 = empresa1.empleados_empresa("cacho", "limpieza")

    for empleado in empresa1.empleados:
        print(f"empleado: {empleado.nombre}, empresa: {empleado.empresa.nombre}, puesto: {empleado.puesto}")

    for empleado in empresa2.empleados:
        print(f"empleado: {empleado.nombre}, empresa: {empleado.empresa.nombre}, puesto: {empleado.puesto}")

if __name__ == "__main__":
    main()