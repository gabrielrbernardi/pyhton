lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = lar * alt
qtd_tin = area / 2
print('A parede tem dimensao de {} x {} e a area eh {:.2f}m2'.format(lar, alt, area))
print('A quantidade necessaria de tinta para pintar a parede eh {:.4f}l'.format(qtd_tin))