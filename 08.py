import math
an = float(input('digite um angulo: '))
seno=math.sin(math.radians(an))
print('O angulo {} tem o seno de {:.2f}'. format(an, seno))
cos=math.cos(math.radians(an))
print('O angulo de {} tem o cos de {:.2f}'. format(an, cos))
tang=math.tan(math.radians(an))
print('O angulo de {} tem a tangente de {:.2f}'.format(an, tang))