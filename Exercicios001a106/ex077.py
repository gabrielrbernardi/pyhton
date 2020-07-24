palavras = ('aprender', 'programar', 'linguagem', 'pyhton', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for i in palavras:
	print('\nNa palavra {} temos '.format(i.upper()), end='')
	for l in i:
		if l.upper() in 'AEIOU':
			print('{}'.format(l), end=' ')