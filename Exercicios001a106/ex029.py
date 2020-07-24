vel = int(input('Digite a velocidade do carro: '))
if vel > 80:
    print('Voce foi multado!')
    mul = (vel - 80) * 7
    print('O valor da multa será de R$ {:.2f}'.format(mul))
else:
    print('Voce nao foi multado')