lista = []
lista_par = []
lista_imp = []
while True:
	lista.append(int(input('Digite um numero: ')))
	choose = ' '
	while choose not in 'SN':
		choose = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
	if choose == 'N':
		break
tam = len(lista)
for i in range(0,tam):
	if lista[i] % 2 == 0:
		lista_par.append(lista[i])
	else:
		lista_imp.append(lista[i])
print('Os numeros digitados foram: {}'.format(lista))
print('Os numeros pares sao: {}'.format(lista_par))
print('Os numeros impares sao: {}'.format(lista_imp))