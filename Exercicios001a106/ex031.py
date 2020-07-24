km = int(input('Digite a distancia da viagem: '))
if km <= 200:
    pre = km * 0.5
else:
    pre = km * 0.45
print('O valor da passagem sera de R$ {:.2f}'.format(pre))