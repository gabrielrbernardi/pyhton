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

