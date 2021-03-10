print('{:=^40}'.format('LOJAS'))
preço = float(input('preço das compras: R$'))
print('''formas de pagamentos
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opçao = int(input('Qual é a opção? '))
if opçao == 1:
    total = preço - (preço * 10/100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opçao == 4:
    total = preço + (preço * 20/100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totalparc, parcela))
print('Sua coompra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
