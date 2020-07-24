lista = []
while True:
	num = int(input('Digite um numero: '))
	if num not in lista:
		lista.append(num)
		print('Valor adcionado com sucesso!')
	else:
		print('Valor ja existente na lista. Tente outro numero!')
	choose = ' '
	while choose not in 'SN':
		choose = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
	if choose == 'N':
		break
lista.sort()
print('A lista foi composta por {}'.format(lista))
print('Programa finalizado com sucesso!!!')