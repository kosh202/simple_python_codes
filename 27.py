frase=str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A aparece na {} letra.'. format(frase.find('a')+1))
print('A ultima letra A apareceu na {} letra.'.format(frase.rfind('a')+1))