nome = str(input('Digite um nome composto: ')).upper().strip()
pos1 = nome.find(' ')
pos2 = nome.rfind(' ') + 1
print('O primeiro nome eh {}'.format(nome[:pos1]))
print('O ulitmo nome eh {}'.format(nome[pos2:]))
