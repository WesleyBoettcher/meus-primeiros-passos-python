nome = input ("qual o nome do aluno: ")
nota = float(input("qual a nota do aluno: "))
if nota >= 7:
    print ("O aluno ", nome, " foi aprovado com nota ", nota)
elif nota >= 5 and nota < 7:
    print ("O aluno ", nome, " ficou em recuperação com nota ", nota)
else:
    print ("O aluno ", nome, " foi reprovado com nota ", nota)