import random
import time
print('=====JOGO DA ADVINHACAO=====')
num_ran = random.randint(0,10)
print('PENSANDO EM UM NUMERO...')
time.sleep(0.5)
num = ''
ten = 0
while num != num_ran:
    print('\nVoce nao acertou! Tente novamente')
    num = int(input('Digite um numero entre 0 e 10: '))
    ten += 1
    if num > num_ran:
        print('\nMenos... Tente mais uma vez')
    elif num < num_ran:
        print('\nMais... Tente mais uma vez')
print('-='*20)
print('\033[32mParabens! Voce acertou\033[m')
print('Voce precisou de {} tentativas'.format(ten))
print('O numero escolhido pelo computador foi {}'.format(num_ran))