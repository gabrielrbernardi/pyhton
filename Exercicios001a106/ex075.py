num = (int(input('Digite um numero: ')),
	   int(input('Digite um numero: ')),
	   int(input('Digite um numero: ')),
	   int(input('Digite um numero: ')),)
qtd9 = num.count(9)
pos = num.index(3)
print('O numero 9 apareceu {} vezes'.format(qtd9))
print('O numero 3 foi digitado pela primeira vez na posicao {}'.format(pos))
print('Os numeros pares digitados foram: ', end='')
par = 0
for i in range(0,4):
	if num[i] % 2 == 0:
		print(num[i], end=' ')
		par += 1
if par == 0:
	print('NAO HOUVE NUMERO PAR')