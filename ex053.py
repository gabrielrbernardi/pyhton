frase = str(input('Digite uma frase: ')).strip().upper()
pal = frase.split()
jun = ''.join(pal)
print('Voce digitou a frase {}'.format(jun))
tam = int(len(jun))
inverso = ''
for i in range(tam-1, -1, -1):
    inverso += jun[i]
if inverso == jun:
    print('A frase {} EH palindromo'.format(frase))
else:
    print('A frase {} NAO EH palindromo'.format(frase))