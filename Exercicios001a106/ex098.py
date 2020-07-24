from time import sleep
def contador(a, b, c):
	print('Fazendo a contagem de {} ate {} de {} em {}'.format(a, b, c, c))
	if a < b:
		for i in range(a, b+1, c):
			print(i, end=' ', flush=True)
			sleep(0.25)
		print('FIM!\n')
	elif a > b:
		c = c - (2*c)
		for i in range(a, b+c, c):
			print(i, end=' ', flush=True)
			sleep(0.25)
		print('FIM!\n')


contador(1, 10, 1)
contador(10, 0, 2)
print('CONTADOR PERSONALIZADO')
i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
if p == 0:
	p = 1
contador(i, f, p)