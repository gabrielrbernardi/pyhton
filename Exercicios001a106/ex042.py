print('\033[33m-=-\033[m' * 15)
print('\033[4;30;47mANALISADOR DE TRIANGULOS\033[m')
print('\033[33m-=-\033[m' * 15)
l1 = int(input('Digite o lado 1 do triangulo: '))
l2 = int(input('Digite o lado 2 do triangulo: '))
l3 = int(input('Digite o lado 3 do triangulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos PODEM formar um triangulo')
    if l1 == l2 and l2 == l3:
        print('Triangulo EQUILATERO')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('Triangulo ISOSCELES')
    else:
        print('Trianglo ESCALENO')
else:
    print('Os segmentos NAO PODEM formar um triangulo')