Algoritmo huevosAlaCopa
	Definir t Como Real
	Definir t0 Como Real
	Escribir "Indique la temperatura original del huevo"
	Leer t0
	m = 63
	c = 3.7
	p = 1.038
	k = 5.4*(10^(-3))
	tw = 100
	oper1 = ((m^(2/3))*c*(p^(1/3)))/((k*PI^(2))*((4*PI)/3)^(2/3))
	oper2 = ln(0.76*(t0-tw)/(70-tw))
	ecuac = oper1*oper2
	Escribir ecuac," segundos"
	Escribir ecuac/60," minutos"
FinAlgoritmo
