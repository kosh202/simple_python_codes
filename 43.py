from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('O atleta está classificado como MIRIM')
elif idade > 9 and idade <= 14:
    print('O atleta está classificado como infantil.')
elif idade > 14 and idade <= 19:
    print('O atleeta é considerado como junior')
elif idade > 19 and idade <=25:
    print('O atleta é considerado na categoria sênior')
elif idade > 25:
    print('O atleta está na categoria de master')
