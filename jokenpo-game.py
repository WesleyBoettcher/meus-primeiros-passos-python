from random import choice
escolha = input('Pedra, papel ou tesoura? ')
lista = ['pedra','papel','tesoura']
escolhaPC = choice(lista)
if escolha == 'pedra' and escolhaPC == 'pedra':
    print('escolheu {} e eu escolhi {}, empatamos! '.format('pedra','pedra'))
elif escolha == 'pedra' and escolhaPC == 'papel':
    print('escolheu {} e eu escolhi {}, voce perdeu! '.format('pedra','papel'))
elif escolha == 'pedra' and escolhaPC == 'tesoura':
    print('escolheu {] e eu escolhi {}, voce ganhou'.format('pedra','tesoura'))
elif escolha == 'papel' and escolhaPC == 'pedra':
    print('escolheu {} e eu escolhi {}, voce ganhou'.format('papel','pedra'))
elif escolha == 'papel' and escolhaPC == 'papel':
    print('escolheu {} e escolhi {}, empatamos! '.format('papel','papel'))
elif escolha == 'papel' and escolhaPC == 'tesoura':
    print('escolheu {} e eu escolhi {}, voce perdeu! '.format('papel','tesoura'))
elif escolha == 'tesoura' and escolhaPC == 'pedra':
    print('escolheu {} e eu escolhi {}, voce perdeu! '.format('tesoura','pedra'))
elif escolha == 'tesoura' and escolhaPC == 'papel':
    print('escolheu {} e eu escolhi {}, voce ganhou'.format('tesoura','papel'))
elif escolha == 'tesoura' and escolhaPC == 'tesoura':
    print('escolheu {} e escolhi {}, empatamos! '.format('tesoura','tesoura'))

