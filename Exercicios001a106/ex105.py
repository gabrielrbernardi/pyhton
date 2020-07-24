res = {}
def notas(*notas, sit=False):
	"""
	=>Funcao para analisar notas e situacoes de alunos
	:param notas: Notas com tipo float
	:param sit: Opcional, indicando se mostra ou nao a situacao do conjunto de notas passadas
	:return: Dicionario, com os valores adicionados na funcao
	"""
	tam = len(notas)
	res['total_notas'] = tam
	res['notas'] = notas
	s = sum(notas)
	med = s / tam
	res['maior'] = max(notas)
	res['manor'] = min(notas)
	res['media'] = med
	if sit == True:
		if med > 7:
			res['situacao'] = 'BOA'
		elif med >=5 and med < 7:
			res['situacao'] = 'RAZOAVEL'
		else:
			res['situacao'] = 'RUIM'
	return res

resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)