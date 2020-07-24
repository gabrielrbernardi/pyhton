from random import randint
lista = []

############# FUNCOES
def sorteia():
	for i in range(0, 5):
		num = randint(1,10)
		lista.append(num)
	print('Os valores sorteados foram', end=' ')
	for i in range(0,5):
		print(lista[i], end=' ')
	somaPar(lista)

def somaPar(lista):
	s = 0
	for v in lista:
		if v % 2 == 0:
			s += v
	print('\nA soma dos valores pares eh {}'.format(s))

############## Programa principal
sorteia()