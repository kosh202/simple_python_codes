casa = float(input('Valor da casa: R$'))
salario=float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação= casa / (anos*12)
minimo = salario * 30/100
print('para pgar uma casa de {:.2f} reais em {} anos.'.format(casa, anos), end='')
print('a prestação será de {:.2f} reais '.format(prestação))
if prestação <=minimo:
    print('Emprestimo pode ser concedido')
else:
    print('Emprestimo negado')