
num1 = int(input("Ingrese valor para variable uno:"))
num2 = int(input("Ingrese valor para variable dos:"))

print("valores de variables:", num1, num2)

guarda_num = num1
num1 = num2
num2 = guarda_num

print("valores invertidos:", num1, num2)