from datetime import date
atual = date.today().year
menor = 0
maior = 0
idoso = 0
idade = 0
for c in range(1,6):
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    if idade < 18:
        menor += 1
    elif idade >= 18 and idade < 60:
        maior += 1
    else:
        idoso += 1
print('Existem {} pessoas menores de idade'.format(menor))
print('Existem {} pessoas maiores de 18 e menores que 60 anos'.format(maior))
print('Existem {} pessoas maiores que 60 anos'.format(idoso))
