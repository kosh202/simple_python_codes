peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual a sua altura? (m)'))
imc = peso /(altura ** 2)
if imc < 18.8:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está no sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você está na obesidade')
elif imc > 40:
    print('Você está na obesidade mórbida. CUIDADO')
print('O imc dessa pessoa é de {:.1f}'.format(imc))