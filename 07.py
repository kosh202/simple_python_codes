import random
n1=input('digite o nome de um aluno:')
n2= input('digite o nome de outro aluno:')
n3=input('o nome de outo aluno:')
n4=input('digite o nome do ultimo aluno:')
lista=[n1, n2, n3, n4]
random.shuffle(lista)
print('A sequencia das apresentações sera:')
print(lista)