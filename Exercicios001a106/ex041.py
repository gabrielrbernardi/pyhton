import datetime
ano = int(input('Digite o ano de nascimento: '))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano
if ano <= 9:
    print('Categoria MIRIM')
elif ano > 9 and ano <= 14:
    print('Categoria INFANTIL')
elif ano > 14 and ano <= 19:
    print('Categoria JUNIOR')
elif ano > 19 and ano <= 20:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER')