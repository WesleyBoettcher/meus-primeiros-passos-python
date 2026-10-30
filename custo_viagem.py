km = float(input('Quantos km voce irá rodar? '))
litro = float(input('Quantos km por litros seu carro faz? '))
combustivel = float(input('Qual o valor do litro? '))
total = km / litro * combustivel
print ('O custo total da viagem será de {:.2f}'.format(total))