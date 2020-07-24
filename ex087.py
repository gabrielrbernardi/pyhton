linhas = []
mat = []
s_par = s_3_col = 0
for i in range(0,3):			# Fazer a leitura dos valores
	for j in range(0,3):
		linhas.append(int(input('Digite um valor pra posicao [{},{}]: '.format(i,j))))
	mat.append(linhas[:])
	linhas.clear()
for i in range(0,3):
	for j in range(0,3):
		if mat[i][j] % 2 == 0:
			s_par += mat[i][j]
for i in range(0,3):
	s_3_col += mat[i][2]
max_2_l = max(mat[1])
print('-='*30)
print('A matriz digitada foi')
for i in range(0,3):			# Imprimindo os valores
	for j in range(0,3):
		print('[ {} ]'.format(mat[i][j]), end='')
	print()
print('A soma dos valores pares foi: {}'.format(s_par))
print('A soma dos valores da 3a coluna foi: {}'.format(s_3_col))
print('O maior valor da segunda linha foi: {}'.format(max_2_l))