peso = float(input('Digite o peso: '))
ma = peso
me = peso
for i in range(0,4):
    peso = float(input('Digite o peso: '))
    if peso > ma:
        ma = peso
    elif peso < me:
        me = peso
print('O maior peso foi {:.2f}Kg e o menor peso foi {:.2f}Kg'.format(ma, me))