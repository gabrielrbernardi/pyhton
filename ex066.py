i = n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
    i += 1
print('A soma dos {} numeros digitados eh {}'.format(i, s))