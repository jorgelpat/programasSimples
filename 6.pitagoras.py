#Escriba un programa que reciba como entrada las longitudes de los dos catetos a
# y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
# del triangulo, dado por el teorema de Pitágoras: c2=a2+b2

cata = float(input("Indique el valor del cateto a\n"))
catb = float(input("Indique el valor del cateto b\n"))

hip2 = (cata**2) + (catb**2)
hip = hip2**(1/2)
print(f"la hipotenusa es {hip}")
