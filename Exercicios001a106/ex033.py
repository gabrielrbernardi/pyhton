num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))
ma = num1
me = num1

if num2 > num1 and num2 > num3:
    ma = num2
if num3 > num1 and num3 > num2:
    ma = num3
print('O maior numero eh {:.2f}'.format(ma))
if num2 < num1 and num2 < num3:
    me = num2
if num3 < num1 and num3 < num2:
    me = num3
print('O menor numero eh {:.2f}'.format(me))