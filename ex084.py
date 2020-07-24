dados = []
dados_geral = []
qtd  = 0
while True:
	dados.append(str(input('Digite o nome da pessoa: ')))
	dados.append(float(input('Digite o peso da pessoa: ')))
	dados_geral.append(dados[:])
	qtd += 1
	choose = ' '
	while choose not in 'SN':
		choose = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
	if choose == 'N':
		break
	dados.clear()
print('-='*30)
print('Foram cadastradas {} pessoas'.format(qtd))
print('Os dados digitados foram: {}'.format(dados_geral))
print('\nPessoas acima do peso')
for p in dados_geral:
	if p[1] > 100:
		print(p[0])
print('\nPessoas abaixo do peso: ')
for p in dados_geral:
	if p[1] < 70:
	   print(p[0])