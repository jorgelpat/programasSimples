#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:
r = float(input("Ingrese el radio\n"))
perimeter = (2*3.14)*r
area = 3.14*(r**2)
print(f"Perímetro: {round(perimeter,1)}")
print(f"Áera: {round(area,1)}")
