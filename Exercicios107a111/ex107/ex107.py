from ex107 import moeda

val = float(input('Digite o preco: R$ '))
metade = moeda.metade(val)
dobro = moeda.dobro(val)
aum = moeda.aumentar(val, 10)
red = moeda.diminuir(val, 13)
print('A metade de {} eh {}'.format(val, metade))
print('O dobro de {} eh {}'.format(val, dobro))
print('Aumentando 10% fica {}'.format(aum))
print('Reduzindo 13% fica {}'.format(red))
