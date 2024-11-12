nota = int(input("Digite a nota: "))

if nota > 85 and nota <= 100:
    print ("Parabéns você tirou nota A")
elif nota > 60 and nota <= 85:
    print("Parabéns você tirou nota B+")
elif nota > 40 and nota >= 60:
    print("Você tirou nota B")
elif nota > 30 and nota <= 40:
    print("Você tirou nota C")
else:
    print("Você está reprovado")