#Escriba un programa que pida al usuario un entero de tres dígitos, 
#y entregue el número con los dígitos en orden inverso:


number = int(input("Indicame un número de 3 dígitos\n"))
terDig = number%10
segDig = (number/10)%10
priDig = ((number/10)/10)%10
print(f"{terDig}{int(segDig)}{int(priDig)}")
