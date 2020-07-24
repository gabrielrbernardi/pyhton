som_idade = 0
med = 0
ma_hom = 0
nome_velho = ''
mul_me_20 = 0
for i in range(0,4):
    print('-----------{}a PESSOA-------------'.format(i))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: '))
    som_idade += idade
    if i == 0 and sexo in 'Mm':
        ma_hom = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > ma_hom:
        ma_hom = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mul_me_20 += 1
med = som_idade / 4
print('A media de idade do grupo eh de {} anos'.format(med))
print('O homem mais velho tem {} anos e se chama {}'.format(ma_hom, nome_velho))
print('A quantidade de mulheres com menos de 20 anos eh {}'.format(mul_me_20))