cont = n = total = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    cont += 1
    total += n
print('Você digitou {} numeros e a soma foi de {}'.format(cont, total))