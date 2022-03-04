from tkinter import W


with open("economic-indicators.csv", "r") as boston:
	total = 0
	trafego = 0
	totalPassageiros = 0
	maiorMedia = 0
	ocupacaoHotel = 0
	menorDesemprego = 99999999999999999999999999999
	anoUsuario = input("Qual ano deseja procurar? ")
	for linha in boston.readlines()[1:-1]:
		lista = linha.split(",")
		total = total+float(lista[3])
		if float(lista[2]) > float(trafego):
			trafego = lista[2]
			ano = lista[0]
			mes = lista[1]
		if anoUsuario == lista[0]:
			totalPassageiros = totalPassageiros + float(lista[2])
			if float(lista[5]) > float(maiorMedia):
				maiorMedia = lista[5]
				mesMaiorMedia = lista[1]
			if float(lista[4]) > float(ocupacaoHotel):
				ocupacaoHotel = lista[4] 
				anoOcupacao = lista[0]
				mesocupacao = lista[1]
			if float(lista[7]) < float(menorDesemprego):
				menorDesemprego = lista[7]
				anoMenorDesemprego = lista[0]
				mesMenorDesemprego = lista[1]


	print("-----------------------------------------------------------------------------------------------------")		
	print("O total de voos é",total)
	print("A data com mais movimentação foi do mes",str(mes), "de", str(ano))
	print("O total de passageiros que passaram em logam no ano de",str(anoUsuario),"foram", totalPassageiros)
	print("O mes com a maior media diaria de passageiros em",str(anoUsuario),"foi",mesMaiorMedia)
	print ("O mes com maior ocupação de vagas de hoteis no ano de",anoOcupacao,"foi o mes",mesocupacao,"com ocupacao de",ocupacaoHotel)
	print("A menor taxa de desemprego de",anoMenorDesemprego,"foi no mes",mesMenorDesemprego,"com uma taxa de desemprego de",menorDesemprego)
	print("-----------------------------------------------------------------------------------------------------")		
