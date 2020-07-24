nome = str(input('Digite seu nome: ')).strip()                          #Funcao utilizada para retirar os espacos antes e depois da frase
print('Seu nome em maiusculas eh {}'.format(nome.upper()))
print('Seu nome em minusculas eh {}'.format(nome.lower()))
print('Seu nome sem espacos tem o tamanho de {} letras'.format(len(nome) - nome.count(' ')))    #fazendo a contagem de letras, subtraindo a quantidade de espacos
print('O primeiro nome tem {} letras'.format(nome.find(' ')))           # A funcao foi usada para achar a posicao do 1º espaco, e com isso achar o tamanho do primeiro nome
