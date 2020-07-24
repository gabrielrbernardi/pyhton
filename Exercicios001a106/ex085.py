par = []
imp = []
numeros = []
num = 0
for i in range(0,7):
	num = int(input('Digite o {} valor: '.format(i+1)))
	if num % 2 == 0:
		par.append(num)
	else:
		imp.append(num)
par.sort()
imp.sort()
numeros.append(par)
numeros.append(imp)
print('Sao eles: {}'.format(numeros))
print('Os numeros pares sao: {}'.format(numeros[0]))
print('Os numeros impares sao: {}'.format(numeros[1]))