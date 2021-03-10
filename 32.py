distancia = float(input('Digite a distancia da viagem: '))
preço1=0.45*distancia
preço2=distancia*0.5
if distancia <= 200:
    print('O preço da viagem sera de {:.2f} reais.'.format(preço2))
else:
    print('O preço da viagem sera de {:.2f} reais.'.format(preço1))