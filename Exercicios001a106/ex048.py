s = 0
print('A soma dos numeros imapres, multiplos de 3, no intervalo de 1 a 500 eh: ', end=' ')
for i in range (1,501):
    if i % 2 == 1 and i % 3 == 0:
        s += i
print(s)