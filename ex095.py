dados = {}
gols = []
time = []
qtd_gols = 0
while True:
	dados.clear()
	dados['nome'] = str(input('Digite o nome do jogador: ')).strip().title()
	dados['qtd_partidas'] = int(input('Digite a quantidade de partidas de {}: '.format(dados['nome'])))
	gols.clear()
	for i in range(0, dados['qtd_partidas']):
		gol = int(input('Quantos gols {} fez na partida {}: '.format(dados['nome'], i+1)))
		qtd_gols += gol
		gols.append(gol)
	dados['gols_p_part'] = gols[:]
	dados['qtd_gols'] = sum(gols)
	time.append(dados.copy())
	choose = ' '
	while choose not in 'SN':
		choose = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
	if choose == 'N':
		break
print('cod ', end='')
for i in dados.keys():
	print(f'{i:<15}', end='')
print()
print('--'*50)
for i, j in enumerate(time):
	print('{:>3}'.format(i), end=' ')
	for d in j.values():
		print(f'{str(d):<15}', end=' ')
	print()
print('=='*50)
while True:
	bus = int(input('Deseja mostrar os dados de qual jogador? '))
	if bus == 999:
		break
	if bus >= len(time):
		print(f'ERRO! Jogador inexistente. Tente novamente')
	else:
		print('LEVANTAMENTO DO JOGADOR {}:'.format(time[bus]['nome']))
		for i, g in enumerate(time[bus]['gols_p_part']):
			print('	No jogo {} fez {} gols'.format(i+1, g))
	print('--'*40)
print('Programa finalizado com sucesso!')
