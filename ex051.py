pri = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razao da PA: '))
for i in range(pri, raz*10, raz):
    print(i, '->', end=' ')
print('ACABOU!!!')