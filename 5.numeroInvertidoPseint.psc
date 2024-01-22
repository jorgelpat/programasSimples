Algoritmo numeroInvertido
	Definir number Como Entero
	Definir terDig Como Entero
	Definir segDig Como Entero
	Definir priDig Como Entero
	
	Escribir 'Indicame un numero de 3 digitos'
	Leer number
	terDig = number MOD 10
	segDig = Trunc(number/10) mod 10
	priDig = Trunc(Trunc(number/10)/10)mod 10
	Escribir terDig,segDig,priDig
FinAlgoritmo
