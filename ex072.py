numero = 'ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',  'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE'
while True:
	num = int(input('Digite um numero: '))
	if num > 0 and num < 20:
		break
for i in range(0,20):
	if num == i:
		print('O numero {} por extenso eh {}'.format(num, numero[i]))
