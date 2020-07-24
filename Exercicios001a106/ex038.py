n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
if n1 > n2:
    print('O primeiro numero ({:.2f}) eh maior que o segundo ({:.2f})'.format(n1, n2))
elif n2 > n1:
    print('O segundo numero ({:.2f}) eh maior que o primeiro ({:.2f})'.format(n2, n1))
else:
    print('O primeiro ({:.2f}) e o segundo ({:.2f}) numero sao iguais'.format(n1,n2))