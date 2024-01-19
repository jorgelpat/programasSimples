#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, 
#y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.


c1 = int(input("Indique la nota del certamen 1\n"))
c2 = int(input("Indique la nota del certamen 2\n"))
nl = int(input("Indique la nota laboratorio\n"))
nf = 60
nc = (nf - (nl*0.3))/0.7
c3 = (3*nc)-(c1+c2)
print(f"Necesita nota {c3} del certamen 3")
