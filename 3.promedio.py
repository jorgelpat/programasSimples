#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
amount = 4
suma = float(0)
for i in range(amount):
    notes = float(input(f"Indique la nota {i+1}\n"))
    suma = suma + notes
    
print(f"El promedio de las notas es {suma/amount}")
