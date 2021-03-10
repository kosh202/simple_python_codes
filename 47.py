import ansi
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
#print('Computador escolheu {}'.format(itens[computador]))->escolhe entre papel tesoura pedra
jogador = int(input('Qual é a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-='*50)
if computador == 0:
   if jogador == 0:
       print('VOCÊ EMPATOU')
   elif jogador == 1:
       print('\033[32mVOCÊ GANHOU!')
   elif jogador == 2:
       print('\033[31VOCÊ PERDEU')
   else:
       print('\033[41mJOGADA INVALIDA\033[0m')
elif computador == 1:
    if jogador == 0:
        print('\033[31mVOCÊ PERDEU')
    elif jogador == 1:
        print('VOCÊ EMPATOU')
    elif jogador == 2:
        print('\033[32mVOCÊ GANHOU!')
    else:
        print('\033[41mJOGADA INVALIDA\033[0m')
elif computador == 2:
    if jogador == 0:
        print('\033[32mVOCÊ GANHOU!')
    elif jogador == 1:
        print('\033[31mVOCÊ PERDEU')
    elif jogador == 2:
        print('VOCÊ EMPATOU')
    else:
        print('\033[41mJOGADA INVALIDA\033[0m')
print('\033[0m-='*50)