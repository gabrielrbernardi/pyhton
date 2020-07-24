pri = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razao da PA: '))
i = 1
ter = pri
while i <= 10:
    print('{} -> '.format(ter), end='')
    ter += raz
    i += 1
print('ACABOU!!!')