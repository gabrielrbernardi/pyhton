from time import sleep
c = ('\033[m',				# 0 - sem cores
	 '\033[0;30;41m',		# 1 - vermelho
	 '\033[0;30;42m',		# 2 - verde
	 '\033[0;30;43m',		# 3 - amarelo
	 '\033[0;30;44m',		# 4 - azul
	 '\033[0;30;45m',		# 5 - roxo
	 '\033[7;30m'			# 6 - branco
	 );


def titulo(msg, cor=0):
	tam = len(msg) + 2
	sleep(0.5)
	print(c[cor], end='')
	print('~' * tam)
	print(msg.upper())
	print('~' * tam)
	print(c[0], end='')


def pyhelp(msg):
	titulo('  Acessando o manual do comando {}'.format(msg), 4)
	print(c[6], end='')
	sleep(0.5)
	help(msg)
	print(c[0])


titulo('  PyHELP', 2)
while True:
	txt = str(input('>>> ')).strip()
	if txt in 'FIMfim':
		break
	else:
		pyhelp(txt)
titulo('Finalizado com sucesso!', 1)
