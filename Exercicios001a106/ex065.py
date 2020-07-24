ma = me = i = n = som = 0
choose = ''
while choose in 'Ss':
    i += 1
    n = int(input('Digite um numero: '))
    choose = str(input('Deseja continuar? [S/N]: '))
    if i == 1:
        ma = me = n
    if n > ma:
        ma = n
    elif n < me:
        me = n
    som += n
med = som/i
print('O menor numero foi {}\nO maior numero foi {}\nA media dos valores digitados foi {}'.format(me, ma, med))