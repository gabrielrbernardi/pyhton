from datetime import date
ano = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
if idade > 18:
    print("O tempo do alistamento ja passou em {} anos".format(idade - 18))
elif idade == 18:
    print('Esta na hora de se alistar')
else:
    print('Voce precisara se alistar em {} anos'.format(18 - idade))