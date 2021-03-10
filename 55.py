ter = int(input('Primeiro termo: '))
razao = int(input('razão: '))
decimo = ter + (10 - 1) * razao
for c in range(ter, decimo + razao, razao):
    print(razao * c, end='->')
print('ACABOU')