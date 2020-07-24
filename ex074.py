from random import randint
# randomizando 5 numeros diferentes dentro de uma tupla
ran = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')
for i in ran:
	print('{} '.format(i), end='')
print('\nO maior valor sorteado foi {}'.format(max(ran)))
print('O menor valor sorteado foi {}'.format(min(ran)))