num1=int(input('Digite um numero qualquer: '))
num2=int(input('Digite outro numero qualquer: '))
if num1 > num2:
    print('O primeiro numero é maior.')
elif num2 > num1:
    print('O segundo numero é o maior')
elif num2 == num1 or num1 == num2:
    print('Não existe valor maior, os dois são iguais.')