from random import randint
num = ran = s = qtd = 0
print('='*40)
print('{:^35}'.format('PAR ou IMPAR'))
print('='*40)
while True:
    num = int(input('Digite um valor: '))
    ran = randint(0,10)
    s = num + ran
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR [P/I]: ')).strip().upper()[0]
    print(f'Voce jogou {num} e o computador jogou {ran}. Total de {s}')
    if tipo == 'I':
        if s % 2 == 1:
            print('Voce GANHOU')
            qtd += 1
        else:
            print('Voce PERDEU')
            break
    elif tipo == 'P':
        if s % 2 == 0:
            print('Voce GANHOU')
            qtd += 1
        else:
            print('Voce PERDEU')
            break
print('Voce venceu {} vezes'.format(qtd))