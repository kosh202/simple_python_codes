toth = tot18 = totm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(('Sexo: [M/F]'))).strip().upper()[0]
    if idade >= 18:
            tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'S':
        print('-'*30)
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'E temos {totm20} mulheres com menos de 20 anos')