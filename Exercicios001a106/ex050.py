s = 0
for i in range(0,6):
    num = int(input('Digite o {} numero: '.format(i+1)))
    if num % 2 == 0:
        s += num
print('A soma eh {}'.format(s))