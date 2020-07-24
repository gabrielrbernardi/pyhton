s = qtd = n = 0
while n != 999:
    n = int(input('Digite um numero: '))
    s += n
    qtd += 1
s -= 999                     #Desconsiderando o valor da condicao de parada
qtd -= 1
print('A soma dos {} numeros digitados foi {}'.format(qtd, s))