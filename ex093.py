dados = {}
gols = []
qtd_gols = 0
dados['nome'] = str(input('Digite o nome do jogador: ')).strip().title()
dados['qtd_partidas'] = int(input('Digite a quantidade de partidas de {}: '.format(dados['nome'])))
for i in range(0, dados['qtd_partidas']):
	gol = int(input('Quantos gols {} fez na partida {}: '.format(dados['nome'], i+1)))
	qtd_gols += gol
	gols.append(gol)
tam_list = len(gols)
dados['gols_p_part'] = gols
dados['qtd_gols'] = qtd_gols
print('=='*50)
print(dados)
print('=='*50)
for i, j in dados.items():
	print(f'{i.upper()} tem o valor: {j}')
print('=='*50)
print('O jogados {} jogou {} partidas'.format(dados['nome'], dados['qtd_partidas']))
for i in range(0, tam_list):
	print('=> Na partida {}, fez {} gols'.format(i+1, gols[i]))
print('Foi um total de {}'.format(dados['qtd_gols']))