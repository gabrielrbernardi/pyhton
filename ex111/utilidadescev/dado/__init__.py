def leiaDinheiro(msg):
	val = False
	while not val:
		entrada = str(input(msg)).replace(',', '.').strip()
		if entrada.isalpha() or entrada == '':
			print(f'ERRO! \"{entrada}\" eh preco invalido!')
		else:
			val = True
			return float(entrada)