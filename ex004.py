a = input('Digite algo: ')
print('O tipo primitivo eh {}'.format(type(a)))
print('So tem espacos? {}'.format(a.isspace()))
print('Eh numero? {}'.format(a.isnumeric()))
print('Eh alfabetico? {}'.format(a.isalpha()))
print('Eh alfanumerico? {}'.format(a.isalnum()))
print('Esta em caixa alta? {}'.format(a.isupper()))
print('Esta em caixa baixa? {}'.format(a.islower()))
print('Esta capitalizada? {}'.format(a.istitle()))