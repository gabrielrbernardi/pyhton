sal = float(input('Digite o valor do salario: '))
if sal <= 1250.00:
    sal1 = sal * 1.15
else:
    sal1 = sal * 1.10
print('O salario que era de R$ {:.2f} passara a ser de {:.2f}'.format(sal, sal1))