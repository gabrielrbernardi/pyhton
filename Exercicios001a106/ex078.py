lista1 = []
pos_max = []
pos_min = []
for i in range(0,5):
	lista1.append(int(input('Digite o {} valor: '.format(i+1))))
val_max = max(lista1)
val_min = min(lista1)
print('A lista digitada eh {}'.format(lista1))
print('O maior valor da lista eh {}'.format(val_max))
print('O menor valor da lista eh {}'.format(val_min))
print('Os maiores valores estao nas posicoes: ', end='')
for i, v in enumerate(lista1):
	if v == val_max:
		print('{}...'.format(i), end=' ')
print('\nOs menores valores estao nas posicoes: ', end='')
for i, v in enumerate(lista1):
	if v == val_min:
		print('{}...'.format(i), end=' ')
print('\nPrograma finalizado com sucesso!!!')