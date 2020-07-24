num = int(input('Digite um numero para saber o fatorial: '))
fat = 1
print('O resultado de {}! = '.format(num), end=' ')
while num != 0:
    print('{}'.format(num),end='')
    fat = fat * num
    num -= 1
    if num >= 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
print('{}'.format(fat))