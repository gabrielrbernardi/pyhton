from datetime import datetime
def voto(ano):
	idade = datetime.now().year - ano
	if idade < 16:
		sit = 'negado'
	elif (idade >= 16 and idade <18) or idade > 65:
		sit = 'opcional'
	else:
		sit = 'obrigatorio'
	return idade, sit

ano_nasc = int(input('Digite o ano de nascimento: '))
idade, sit = voto(ano_nasc)
print('A pessoa que nasceu em {} tem {} anos e tem a situacao de voto {}'.format(ano_nasc, idade, sit.upper()))