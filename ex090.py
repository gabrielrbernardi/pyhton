aluno = {}
aluno['nome'] = str(input('Digite o nome: ')).strip().title()
aluno['med'] = float(input('Digite a media de {}: '.format(aluno['nome'])))
if aluno['med'] >= 7.0:
	aluno['sit'] = 'Aprovado'
elif aluno['med'] < 7.0 and aluno['med'] >= 5:
	aluno['sit'] = 'Recuperacao'
else:
	aluno['sit'] = 'Reprovado'
print('O nome eh {}'.format(aluno['nome']))
print('A media eh {:.2f}'.format(aluno['med']))
print('O aluno foi {}'.format(aluno['sit'].upper()))