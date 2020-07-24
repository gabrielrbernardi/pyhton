import random
import time
print('=====JOGO DA ADVINHACAO=====')
num_ran = random.randint(0,5)
num = int(input('Digite um numero entre 0 e 5: '))
print('PROCESSANDO...')
time.sleep(3)
if num == num_ran:
    print('Voce venceu')
else:
    print('Voce perdeu')
print('O numero escolhido pelo computador foi {}'.format(num_ran))