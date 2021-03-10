import random
n1 = input('coloque o nome de um aluno: ')
n2 = input('coloque o nome de outro aluno: ')
n3 = input('o nome de outro aluno:')
n4 = input('digite o nome do ultimo aluno:')
lista=[n1, n2, n3, n4]
x = random.choice(lista)
print('O aluno sorteado foi', x)