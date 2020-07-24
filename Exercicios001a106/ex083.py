exp = str(input('Digite a expressao de entrada: ')).strip()
lista = []
for simb in exp:
	if simb == '(':
		lista.append('(')
	elif simb == ')':
		if len(lista) > 0:
			lista.pop()
		else:
			lista.append(')')
			break
if len(lista) == 0:
	print('A expressao de entrada esta CORRETA!')
else:
	print('A expressao de entrada esta INCORRETA!')
