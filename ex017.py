import math
co = float(input('Digite a dimensao do cateto oposto: '))
ca = float(input('Digite a dimensao do cateto adjacente: '))
hip1 = math.sqrt(math.pow(co,2) + math.pow(ca,2))                #CALCULO DE FORMA MATEMATICA
hip2 = math.hypot(co,ca)                                         #CALCULO USANDO MODULOS
print('A dimensao da hipotenusa, com a formula eh {}'.format(hip1))
print('A dimensao da hipotenusa, usando modulos eh {}'.format(hip2))