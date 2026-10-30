salario = float(input ("Diga o valor do seu salario? "))
if 1250 >= salario:
    salario = salario + salario * 0.15
    print ("Seu salario teve um aumento de 15% e seu novo salario será de R$", salario )
else:
    salario = salario + salario * 0.10
    print ("Seu salário teve um aumento de 10% e seu novo salario será de R$", salario )

