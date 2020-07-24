num = int(input('Digite um numero: '))
choose = int(input('Qual conversao deseja fazer\n 1 - Decimal para binario\n 2 - Decimal para Octal\n 3 - Decimal para hexadecimal\nEscolha: '))
if choose == 1:
    bin = bin(num)[2:]
    print('O numero {} em binario eh {}'.format(num, bin))
elif choose == 2:
    oct = oct(num)[2:]
    print('O numero {} em octal eh {}'.format(num, oct))
else:
    hex = hex(num)[2:]
    print('O numero {} em hexadecimal eh {}'.format(num, hex))