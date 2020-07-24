from datetime import date
ma = 0
me = 0
ano = date.today().year
for i in range(0,7):
    ano1 = int(input('Digite o ano de nascimento: '))
    idade = ano - ano1
    if idade >= 21:
        ma += 1
    else:
        me += 1
print('A quantidade de pessoas maiores 21 anos eh {} e a de menores de 21 anos eh {}'.format(ma, me))