num = 0
m = 1
while True:
    num = int(input('Digite um numero para ver a sua tabuada: '))
    if num < 0:
        break
    else:
        print('-='*15)
        for i in range(0,11):
            m = num * i
            print('{} x {:2} = {:2}'.format(num, i, m))
        print('-=' * 15)
print('Programa finalizado!!!')