# # FAZENDO COM STRINGS
# num = str(input('Digite um numero: '))
# un = num[3]
# dez = num[2]
# cen = num[1]
# mil = num[0]
# print('Unidades {}'.format(un))
# print('Dezenas {}'.format(dez))
# print('Centenas: {}'.format(cen))
# print('Milhares: {}'.format(mil))

# FAZENDO DE FORMA MATEMATICA
num = int(input('Digite um numero: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))