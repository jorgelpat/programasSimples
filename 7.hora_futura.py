#Escriba un programa que pregunte al usuario la hora actual t del reloj y 
#un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas

t = float(input("Indique la hora actual\n"))
h = int(input("Indique la cantidad de horas\n"))

x = (h + t) % 24
print(f"En {h} horas el reloj marcará las {x}")

