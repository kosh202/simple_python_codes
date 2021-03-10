from datetime import datetime
dados = {}
dados['nome'] =str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteir de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Sálario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] +35) -datetime.now().year)
print('-='*30)
for k, v in dados.items():
    print(f'  - {k} tem o valor de {v}')