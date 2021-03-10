r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triangulo', end='')
    if r1 == r2 == r3:
        print('equilatero')
    if r1 != r2 != r3:
        print('escaleno')
    else:
        print('isoceles')
else:
    print('Os segmentos acima não podem fazer um triangulo.')