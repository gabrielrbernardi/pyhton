num = int(input('Digite um numero para ver a sua tabuada: '))
for i in range(0,11):
    res = num * i
    print('{} x {:2} = {:2}'.format(num, i, res))