vel = int(input("Qual a velocidade o carro passou no radar "))

if vel > 80:
    multa = (vel - 80) * 7
    multa = multa + 40
    print ("Você foi multado ")
    print ("Sua multa é de R$", multa)
else:
    print ("Tenha uma boa viagem! ")