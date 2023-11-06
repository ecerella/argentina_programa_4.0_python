
"""
Escribir un programa que permita controlar con validación el ingreso a un sitio 
web. Teniendo dos constantes con un nombre de usuario ("admin") y una 
contraseña ("123456"), el programa debe permitir al usuario ingresar sus 
credenciales. Si las mismas son erróneas, se volverán a pedir hasta un máximo 
de 3 intentos. Finalmente, la computadora debe mostrar alguno de los siguientes 
mensajes según sea el caso: "Acceso concedido" o "Se ha bloqueado la cuenta"
"""

NOMBRE_DE_USUARIO = "admin"
CONTRASENIA = "123456"

def UserPasword():
    user = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    return user, password #regresa tupla (user, password)


def ValidacionAccess():
    for a in range(3): #bucle de 3 intentos
        user, password = UserPasword() #llamada a funcion
        if user == NOMBRE_DE_USUARIO and password == CONTRASENIA:
            print("Acceso concedido")
            break # sale del ciclo si las contraseñas son correctas
        else:
            print("Usuario o clave incorrectas")
    else:
        print("Se ha bloqueado la cuenta")

ValidacionAccess()