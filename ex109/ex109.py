from ex109 import moeda
val = float(input('Digite o preco: R$ '))

print(f'A metade de {moeda.moeda(val)} eh {moeda.metade(val, True)}')
print(f'O dobro de {moeda.moeda(val)} eh {moeda.dobro(val)}')
print(f'Aumentando 10% fica {moeda.aumentar(val, 10)}')
print(f'Reduzindo 13% fica {moeda.diminuir(val, 13)}')
