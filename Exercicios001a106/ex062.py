pri = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razao da PA: '))
ter = pri
i = 1
mais = 10
qtd = tot = 0
while mais != 0:
    tot += mais
    while i <= tot:
        print('{} -> '.format(ter), end='')
        ter += raz
        i += 1
        qtd += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar a mais? '))
print('Foram mostrados {} numeros'.format(tot))