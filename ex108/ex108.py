import moeda
val = float(input('Digite o preco: R$ '))

print(f'A metade de {moeda.moeda(val)} eh {moeda.moeda(moeda.metade(val))}')
print(f'O dobro de {moeda.moeda(val)} eh {moeda.moeda(moeda.dobro(val))}')
print(f'Aumentando 10% fica {moeda.moeda(moeda.aumentar(val, 10))}')
print(f'Reduzindo 13% fica {moeda.moeda(moeda.diminuir(val, 13))}')
