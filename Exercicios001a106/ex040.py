n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
med = (n1+n2) / 2
if med > 7.0:
    print('Aluno aprovado')
elif med >= 5.0 and med <= 6.9:
    print('Aluno em recuperacao')
else:
    print('Aluno reprovado')