lista = []
lista_mul = []
lista_p_ma_med = []
med = qtd_pes = s_idade = 0
while True:
	dados = {}
	dados['nome'] = str(input('Digite o nome da pessoa: ')).strip().title()
	dados['idade'] = int(input('Digite a idade de {}: '.format(dados['nome'])))
	dados['sexo'] = str(input('Digite o sexo de {} [M/F]: '.format(dados['nome']))).strip().upper()[0]
	s_idade += dados['idade']
	lista.append(dados.copy())
	if dados['sexo'] == 'F':
		lista_mul.append(dados.copy())
	dados.clear()
	qtd_pes += 1
	choose = ' '
	while choose not in 'SN':
		choose = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
	if choose == 'N':
		break
med = s_idade / qtd_pes
print('='*50)
print('Os dados de entrada foram\n{}'.format(lista))
print('Foram cadastradas {} pessoas'.format(qtd_pes))
print('A media de idade do grupo eh {:.2f} anos'.format(med))
# print('As mulheres cadastradas foram:\n{}'.format(lista_mul, end=' '))
print('As mulheres cadastradas foram: ', end=' ')
for i in lista:
	if i['sexo'] == 'F':
		print(i['nome'], end=' ')
print('\nAs pessoas que estao com a idade acima da media sao: ', end=' ')
for i in lista:
	if i['idade'] > med:
		print(i['nome'], end=' ')