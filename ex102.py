def fatorial(num, show=False):
	"""

	:param num: Numero inteiro a ser calculado o fatorial
	:param show: Parametro para mostrar se deseja apresentar o calculo feito na tela ('True' or 'False')
	:return: Nao possui retorno
	"""
	fat = 1
	print('O resultado de {}! = '.format(num), end=' ')
	while num != 0:
		if show == True:
			print('{}'.format(num),end='')
			fat = fat * num
			num -= 1
			if num >= 1:
				print(' x ', end='')
			else:
				print(' = ', end='')
		else:
			fat = fat * num
			num -= 1
	print('{}'.format(fat))


ajuda = ' '
while ajuda not in 'SN':
	ajuda = str(input('Deseja mostra ajuda? [S/N] ')).strip().upper()[0]
if ajuda == 'S':
	help(fatorial)
else:
	num = int(input('Digite um numero para saber o fatorial: '))
	show = ' '
	while show not in 'SN':
		show = str(input('Deseja mostrar o processo do calculo? [S/N] ')).upper().strip()[0]
	if show == 'S':
		fatorial(num, True)
	else:
		fatorial(num)
