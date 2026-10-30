from selectors import SelectSelector

produto = float(input('Qual é o valor do produto? '))
pago = int(input('Forma de pagamento? [1] para a vista e [2] para a prazo '))
avista = produto - produto * 0.12
aprazo = produto + produto * 0.08
parcela = aprazo / 5
if pago == 1:
    print ('O produto com valor R${:.2f} a vista terá 12% de desconto, ficando R${:.2f}'.format(produto,avista))
elif pago == 2:
    print ('O produto com valor R${:.2f} à prazo em 5x terá 8% de acréscimo, ficando R${:.2f}. Cada parcela será de R${:.2f}'.format(produto,aprazo,parcela))
else:
    print ('Opção errada! ')

