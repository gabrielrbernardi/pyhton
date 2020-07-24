from time import sleep
choose = n1 = n2 = s = m = 0
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
ma = n1
while choose != 5:
    print('-=-='*10)
    print('OPCOES')
    print(' [ 1 ] Soma ')
    print(' [ 2 ] Multiplicar')
    print(' [ 3 ] Verificar o maior numero ')
    print(' [ 4 ] Novos numeros ')
    print(' [ 5 ] Sair do programa')
    choose = int(input('>>>>> Qual a opcao: '))
    if choose == 1:
        print('Opcao escolhida: SOMA')
        s = n1 + n2
        print('A soma de {} + {} = {}'.format(n1, n2, s))
    elif choose == 2:
        print('Opcao escolhida: MULTIPLICAR')
        m = n1 * n2
        print('A multiplicacao de {} x {} = {}'.format(n1, n2, m))
    elif choose == 3:
        print('Opcao escolhida: VERIFICAR O MAIOR NUMERO')
        if n2 > ma:
            ma = n2
        print('O maior numero entre {} e {} eh {}'.format(n1, n2, ma))
    elif choose == 4:
        print('Opcao escolhida: Novos numeros')
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo numero: '))
        ma = n1
    elif choose == 5:
        print('Finalizando...')
    elif choose > 5 or choose < 1:
        print('Opcao invalida! Tente novamente')
    sleep(0.5)
print('Obrigado por utilizar o programa!\nVolte sempre!')
