def maior(*num):
	tam = len(num)
	print('Os numeros informados foram {}'.format(num))
	print('Foram informados {} numeros'.format(tam))
	if tam == 0:
		print('Nao possui maior valor')
		return 0
	val_max = max(num)
	print('O maior valor entre os numeros passados eh: {}'.format(val_max))
	print('-='*30)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()