def area(b, h):
	a = b*h
	print(f'O terreno de dimensoes {b:.2f} x {h:.2f} tem area de {a:.2f} m2')


b = float(input('Digite a largura do terrendo: '))
h = float(input('Digite o comprimento do terreno: '))
area(b,h)