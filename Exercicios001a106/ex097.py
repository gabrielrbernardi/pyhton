def escreva(msg):
	tam = len(msg) + 4
	print('~' * tam)
	print('  {}'.format(msg))
	print('~' * tam)


qtd = int(input('Quantas mensagens serao escritas: '))
for i in range(0, qtd):
	msg = str(input('Digite a mensagem {}: '.format(i+1))).strip().upper()
	escreva(msg)