from datetime import datetime
tem_contrat = 0
for i in range(0,1):
	dados = dict()
	dados['nome'] = str(input('Digite o nome: ')).strip().title()
	ano_nasc = int(input('Digite o ano de nascimento: '))
	dados['idade'] = datetime.now().year - ano_nasc
	dados['ctps'] = int(input('Carteira de trabalho (Digite 0 se nao possui): '))
	if dados['ctps'] == 0:
		break
	else:
		dados['ano_contrat'] = int(input('Digite o ano de contratacao: '))
		dados['sal'] = float(input('Digite o salario: '))
		tem_contrat = datetime.now().year - dados['ano_contrat']
		if tem_contrat < 35:
			idade_aposent1 = abs(tem_contrat - 35)
			dados['idade_apos'] = idade_aposent1 + dados['idade']
for i, j in dados.items():
	print(f'{i.upper()} tem o valor: {j}')
