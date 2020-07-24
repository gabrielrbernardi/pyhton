nome = nome_prod = choose = ''
preco = prod = prod_barato = totmil = subtot = i = 0
cond = True
while cond == True:
    nome = str(input('Digite o nome do produto: ')).strip().upper
    preco = float(input('Digite o preco do produto: '))
    choose = ' '
    while choose not in 'SN':
        choose = str(input('Deseja continuar? ')).strip().upper()[0]
    if i == 0:
        prod = preco
        prod_barato = preco
        nome_prod = nome
    else:
        if preco < prod_barato:
            prod_barato = preco
    if preco > 1000:
        totmil += 1
    elif preco < prod_barato:
        nome_prod = nome
    subtot += preco
    if choose == 'N':
        break
    i += 1
print('Subtotal: R$ {:.2f}'.format(subtot))
print('{} produtos custam mais de R$ 1000.00'.format(prod))
print('{} eh o produto mais barato'.format(nome_prod))