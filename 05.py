from math import hypot
co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
hip=hypot(ca, co)
print('A hipotenusa seria de {:.2f}'. format(hip))
