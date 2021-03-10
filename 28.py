n=str(input('digite seu nome completo: ')).strip()
nome=n.split()
print('O seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
