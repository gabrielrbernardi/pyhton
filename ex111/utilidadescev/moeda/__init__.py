def moeda(n=0, moeda='R$'):
	return f'{moeda}{n:.2f}'.replace('.', ',')

def metade(n, formato=False):
	res = n / 2
	return res if formato is False else moeda(res)


def dobro(n, formato=False):
	res = n * 2
	return res if formato is False else moeda(res)


def aumentar(n, p, formato=False):
	res = n + (n * p/100)
	return res if formato is False else moeda(res)


def diminuir(n, p, formato=False):
	res = n - (n * p/100)
	return res if formato is False else moeda(res)


def moeda(n=0, moeda='R$'):
	return f'{moeda}{n:.2f}'.replace('.', ',')

def resumo(n=0, p_a=10, p_r=5):
	print('-='*15)
	print('RESUMO DO VALOR'.center(30))
	print('-=' * 15)
	print(f'Preco analisado: \t{moeda(n)}')
	print(f'Dobro do preco: \t{dobro(n, True)}')
	print(f'Metade do preco: \t{metade(n, True)}')
	print(f'Aumento de {p_a}%: \t{aumentar(n, p_a, True)}')
	print(f'Diminuicao de {p_r}%: \t{diminuir(n, p_r, True)}')
	print('-='*15)
