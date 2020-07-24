pre = float(input('Digite o preco: '))
print('Condicoes de pagamento\n 1 - Dinheiro/cheque\n 2 - A vista no cartao\n 3 - 2x no cartao\n 4 - 3x ou mais no cartao')
choose = int(input('Escolha: '))
if choose == 1:
    print('Dinheiro/cheque')
    pre = pre * 0.9
    print('O novo preco a ser pago sera de R$ {:.2f}'.format(pre))
elif choose == 2:
    print('A vista no cartao')
    pre = pre * 0.95
    print('O novo preco a ser pago sera de R$ {:.2f}'.format(pre))
elif choose == 3:
    print('2x no cartao')
    print('O preco se mantera. Valor a ser pago R$ {}'.format(pre))
else:
    print('3x ou mais no cartao')
    pre = pre * 1.2
    print('O novo preco a ser pago sera de R$ {:.2f}'.format(pre))