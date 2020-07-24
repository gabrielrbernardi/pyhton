km = int(input('Digite a qtd de km rodados: '))
dias = int(input('Digite a qtd de dias que o carro foi alugado: '))
prec = (60*dias) + (0.15*km)
print('O total a pagar eh: {:.2f}'.format(prec))