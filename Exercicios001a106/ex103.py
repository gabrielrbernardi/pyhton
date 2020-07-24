def ficha(nome='<Desconhecido>', qtd_gols=0):
	print('O jogador {} fez {} gols'.format(nome.title(), qtd_gols))



name = str(input('Digite o nome do jogador: '))
qtd_gol = str(input('Digite a quantidade de gols feitos: '))
if qtd_gol.isnumeric():
	qtd_gol = int(qtd_gol)
else:
	qtd_gol = 0
if name.strip() == '':
	ficha(qtd_gols=qtd_gol)
else:
	ficha(name, qtd_gol)
# nome, qtd_gols = ficha(name, qtd_gol)
