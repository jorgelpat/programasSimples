Algoritmo queNotaNecesito
	Definir c1 Como Entero
	Definir c2 Como Entero
	Definir nl Como Entero
	Definir nf Como Entero
	Escribir "Indique la nota del certamen 1"
	Leer c1
	Escribir "Indique la nota del certamen 2"
	Leer c2
	Escribir "La nota laboratorio"
	Leer nl
	nf = 60
	nc = (nf - (nl*0.3))/0.7
	c3 = (3*nc)-(c1+c2)
	Escribir "Necesita nota ",c3," del certamen 3"
	
FinAlgoritmo
