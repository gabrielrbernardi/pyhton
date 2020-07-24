# sexo = str(input('Digite o sexo da pessoa: [M/F]: ')).strip().upper()
# while sexo != 'M' and sexo != 'F':
#     print('Opcao invalida! Por favor insira os dados corretamente')
#     sexo = str(input('Digite o sexo da pessoa: [M/F]: '))
# print('O sexo da pessoa eh {}'.format(sexo))

# -=-=-=-=-=-=-=-=-=-=-=-=-OUTRA MANEIRA DE RESOLVER O MESMO PROBLEMA=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
sexo = str(input('Digite o sexo da pessoa: [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    print('Opcao invalida! Por favor insira os dados corretamente')
    sexo = str(input('Digite o sexo da pessoa: [M/F]: ')).strip().upper()[0]
print('O sexo da pessoa eh {}'.format(sexo))