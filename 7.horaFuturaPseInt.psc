Algoritmo horaFutura
	Definir t Como Real
	Definir h Como Entero
	Definir x Como Entero
	Escribir "Indique la hora actual"
	Leer t
	Escribir "Indique la cantidad de horas"
	Leer h
	x = Trunc(h+Trunc(t))mod 24
	Escribir "En ",h," horas el reloj marcara las ",x
FinAlgoritmo
