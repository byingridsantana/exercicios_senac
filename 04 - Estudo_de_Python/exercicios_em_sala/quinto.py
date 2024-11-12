nota1 = input("Digite a primeira nota do aluno:")
nota2 = input("Digite a segunda nota do aluno:")
nota3 = input("Digite a terceira nota do aluno:")
nota4 = input("Digite a quarta nota do aluno:")

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

media = (nota1 + nota2 + nota3 + nota4) / 4 

if media >= 6:
    print("Aprovado")
elif media <= 4:
    print("Reprovado")
else:
    print("Recuperação")