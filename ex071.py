print('='*30)
print('{:^30}'.format('CAIXA ELETRONICO'))
print('='*30)
valor = int(input('Digite o valor a ser sacado R$ '))
tot = valor
ced = 50
tot_ced = 0
while True:
    if tot >= ced:
        tot -= ced
        tot_ced += 1
    else:
        if tot_ced > 0:
            print('Total de {} cedulas de R$ {}'.format(tot_ced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot_ced = 0
        if tot == 0:
            break
print('='*30)
print('{:^30}'.format('Volte Sempre!'))