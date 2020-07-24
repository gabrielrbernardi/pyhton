num = int(input('Digite um numero: '))
pri = 0
for i in range(1,num+1):
    if num % i == 0:
        pri += 1
        print('\033[33m{}\033[m'.format(i), end=' ')
    else:
        print('\033[31m{}\033[m'.format(i), end=' ')
print('\nO numero {} foi divisivel {} vezes'.format(num, pri))
if pri == 2:
    print('Logo, o numero {} EH primo'.format(num))
else:
    print('Logo, o numero {} NAO EH primo'.format(num))