prod = ('Lapis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34,9)
print('-='*20)
print('{:^35}'.format('LISTAGEM DE PRECOS'))
print('-='*20)
for i in range(0,18, 2):
	print('{:.<20}R$ {:>6.2f}'.format(prod[i], prod[i+1]))