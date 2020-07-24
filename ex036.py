val_casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do salario: '))
ano = int(input('Digite em quantos anos deseja quitar a casa: '))
val_prest = val_casa / (ano*12)
print('Para pagar uma casa de R$ {:.2f} em {} anos a prestacao sera de {:.2f}'.format(val_casa,ano,val_prest))
if val_prest > (sal*0.3):
    print('Emprestimo negado!')
else:
    print('Emprestimo concedido!')
