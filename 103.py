aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Media do aluno: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
else:
    aluno['media'] = 'reprovado'
print(f'Situação igual a {aluno["situação"]}')
