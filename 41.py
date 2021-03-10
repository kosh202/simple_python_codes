from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = idade - 18
    print('Você ainda não tem 18 anos. ainda faltam {} anos para o alistamento '.format(saldo))
    ano
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {}anos'.format(saldo))