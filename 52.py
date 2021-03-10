soma = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count = count + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(count, soma))