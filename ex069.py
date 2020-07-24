idade = ma = ho = mu = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa: ')).strip().upper()[0]
    choose = ' '
    while choose not in 'SN':
        choose = str(input('Deseja continuar? ')).strip().upper()[0]
    if idade > 18:
        ma += 1
    elif sexo == 'M':
        ho += 1
    elif sexo == 'F' and idade < 20:
        mu += 1
    if choose == 'N':
        break
print('O numero de maior de idade eh {}'.format(ma))
print('{} homens foram cadastrados'.format(ho))
print('Foram cadastradas {} mulheres menores de 20 anos'.format(mu))