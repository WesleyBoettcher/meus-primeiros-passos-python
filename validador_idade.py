ano_nasc = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
if ano_atual - ano_nasc >= 18:
    print ("Parabéns, você ja chegou na maioridade ")
else:
    print ("Que pena, você ainda não chegou na maioridade :( ")