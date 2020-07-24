from random import randint
from time import sleep
jogo = []
mega = []
tot = 0
qtd = int(input('Digite a quantidade de palpites: '))
print('-='*20)
print('Os jogos sorteados foram')
while  tot < qtd:
	cont = 0
	while True:
		num = randint(1,60)
		if num not in jogo:
			jogo.append(num)
			cont += 1
		if cont >= 6:
			break
	jogo.sort()
	mega.append(jogo[:])
	jogo.clear()
	tot += 1
for i, l in enumerate(mega):
	# sleep(0.25)
	print('Jogo {}: {}'.format(i+1, l))