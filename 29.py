from random import randint
from time import sleep
computador =randint(0, 5)
print('irei pensar em um numero de 0 a 5')
print('-=-'*20)
jogador=int(input('em que numero estou pensando? '))
print('PROCESSANDO...')
sleep(3)
if jogador ==computador:
    print('Parabens, voce conseguiu me vencer.')
else:
    print('ganhei! eu pensei no numero {} não no numero {}!'.format(computador, jogador))
