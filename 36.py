n1=float(input('digite o primeiro segmento: '))
n2=float(input('digite o segundo segmento: '))
n3=float(input('digite o terceiro segmento: '))
if n1 + n2 > n3 and n1 < n2 + n3:
    print('Esses tres segmentos podem formar um triangulo.')
else:
    print('nao é possivel formar um triangulo com esses segmentos')
