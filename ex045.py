import random
import time
print('\033[33m-=-\033[m'*10)
print('\033[1;34mJOKENPO')
print('\033[33m-=-\033[m'*10)
opc = ('PEDRA', 'PAPEL', 'TESOURA')
print('''OPCOES DE JOGADA
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = int(input('Escolha: '))
com = random.randint(0,2)
print('\033[31mJO')
time.sleep(0.25)
print('KEN')
time.sleep(0.25)
print('PO!\033[m')
time.sleep(0.25)
print('-=' * 11)
print('Computador jogou {}'.format(opc[com]))
print('Jogador jogou {}'.format(opc[jog]))
print('-=' * 11)
if (jog == 0 and com == 1) or (jog == 1 and com == 2) or (jog == 2 and com == 0):
    print('Jogador \033[31;mPERDE\033[m')
elif (com == 0 and jog == 1) or (com == 1 and jog == 2) or (com == 2 and jog == 0):
    print('Jogador \033[32;mGANHA\033[m')
elif jog == com:
    print('\033[34mEMPATE\033[m')