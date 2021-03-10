n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input(('Digite sua segunda nota: ')))
media = (n1 + n1)/2.0
if media < 5.0:
    print('Voce está REPROVADO')
elif media >=5.0 and media <= 6.9:
    print('Você está de RECUPERAÇÃO.')
elif media >= 7.0:
    print('Você está APROVADO')
print('Tirando {} e {} a sua media é {:.2f}.'.format(n1, n2, media))