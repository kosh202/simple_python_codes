listaimpar = []
listapar = []
listanum = []
while True:
    n = int(input('Digite um numero: '))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    listanum.append(n)
    if n % 2 == 0:
        listapar.append(n)
    if n % 2 > 0:
        listaimpar.append(n)
    if resp == 'N':
        break
print('-='*30)
print(f'A lista completa é {listanum}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')
