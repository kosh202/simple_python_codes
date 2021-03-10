salario=float(input('Qual o salario do funcionario? R$ '))
valor1=salario+(0.1*salario)
valor2=salario+(0.15*salario)
if salario <= 1250:
    print('O salario do funcionario será de {:.2f} reais.'.format(valor2))
else:
    print('O novo salario do funcionario é de {:.2f} reais.'.format(valor1))