from random import randint
computer = randint(0, 10)
while True:
    print('Irei pensar em um numero de 0 a 10.')
    jogador = int(input('Em qual numero estou pensando?'))
    if jogador == computer:
        print('Você acertou!!')
        resp = input('Deseja jogar novamente?[s/n]: ').strip().lower()[0]
        if resp == 's':
            computer = randint(0, 10)
            print('Vou pensar em um novo numero tente descobrir.')
            jogador = int(input('Em qual numero estou pensando?: '))
            if jogador == computer:
                print('Você acertou!')
        if resp == 'n':
            break
    if jogador != computer:
        print('Você errou', end=' ')
        if jogador <= computer:
            print('muito baixo')
        elif jogador >= computer:
            print('muito alto')
    resp = input('Deseja continuar?[s/n]: ').strip().lower()[0]
    if resp in 'n':
        break
