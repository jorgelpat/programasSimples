#Escriba un programa que reciba como entrada la temperatura original 
#del huevo y muestre como salida el tiempo en segundos que le toma alcanzar 
#la temperatura máxima para prepararlo a la copa.
import math
t = float()
t0 = float(input("Inique la temperatura original del huevo\n"))

m = 63
c = 3.7
p = 1.038
k = 5.4*(10**(-3))
tw = 100

oper1 = ((m**(2/3))*c*(p**(1/3)))/((k*math.pi**(2))*((4*math.pi)/3)**(2/3))
oper2 = math.log(0.76*(t0-tw)/(70-tw))

ecuac = oper1*oper2

print(f"{ecuac} segundos")
print(f"{ecuac/60} minutos")

