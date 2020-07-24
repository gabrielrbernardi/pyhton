timesA = 'Palmeiras', 'Santos', 'Flamengo', 'Atlético-MG', 'Internacional', 'Botafogo', 'Goias', 'Corinthians', 'Sao Paulo', 'Gremio'
timesB = 'Bahia', 'Athletico-PR', 'Fortaleza', 'Ceara', 'Vasco', 'Cruzeiro', 'Fluminense', 'Chapecoense', 'CSA', 'Avai'
times = timesA + timesB
print('-=' * 25)
print('Classificacao Brasileirao 2019 (14/07/2019 23:50) ')
print('-=' * 25)
print('Os 5 primeiros colocados sao: ')
for i in range(0,5):
	print('{}. {}'.format(i+1,times[i]))
print('\nOs ultimos 4 colocados sao: ')
for i in range(16,20):
	print('{}. {}'.format(i+1, times[i]))
print(sorted(times))
chape = times.index('Chapecoense')+1
print('A Chapecoense esta na {}ª posicao'.format(chape))