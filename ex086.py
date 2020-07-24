linhas = []
mat = []
for i in range(0,3):
	for j in range(0,3):
		linhas.append(int(input('Digite um valor pra posicao [{},{}]: '.format(i,j))))
	mat.append(linhas[:])
	linhas.clear()
print('-='*30)
print('A matriz digitada foi')
for i in range(0,3):
	for j in range(0,3):
		print('[ {} ]'.format(mat[i][j]), end='')
	print()