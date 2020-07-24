lista = []
qtd = 1
while True:
	lista.append(float(input('Digite um numero: ')))
	choose = ' '
	while choose not in 'SN':
		choose = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
	if choose == 'N':
		break
	qtd += 1
print('A lista eh formada por {}'.format(lista))
print('Foram digitados {} numeros'.format(qtd))
lista.sort(reverse=True)
print('A lista em ordem decrescente eh {}'.format(lista))
if 5 in lista:
	print('O numero 5 ESTA na lista')
else:
	print('O numero 5 NAO ESTA na lista')
print('Programa finalizado com sucesso!!!')