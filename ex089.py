ficha = []
while True:
	nome = str(input('Digite o nome do aluno: ')).strip()
	nota1 = float(input('Digite a nota 1: '))
	nota2 = float(input('Digite a nota 2: '))
	med = (nota1 + nota2)/2
	ficha.append([nome, [nota1, nota2], med])
	choose = ' '
	while choose not in 'SN':
		choose = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
	if choose == 'N':
		break
print('-='*15)
print('{:<4}{:<10}{:>8}'.format('No.', 'NOME', 'MEDIA'))
print('-'*30)
for i, a in enumerate(ficha):
	print('{:<4}{:<10}{:8.1f}'.format(i, a[0], a[2]))