from random import randint
from time import sleep
from operator import itemgetter
print('-='*15)
print('SORTEANDO NUMEROS NOS DADOS')
print('-='*15)
jogo = {'Jogador 1': randint(1,6),
		'Jogador 2': randint(1,6),
		'Jogador 3': randint(1,6),
		'Jogador 4': randint(1,6)}
ranking = []
for i, j in jogo.items():
	print('{} tirou {}'.format(i, j))
	sleep(0.4)
print('-'*30)
print('RESULTADOS')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, j in enumerate(ranking):
	print(f'{i} lugar: {j[0]} com {j[1]}')
	sleep(0.25)