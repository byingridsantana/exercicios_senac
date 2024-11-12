# Faça um programa que peça dois números e imprima o maior deles
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))

if num1 > num2:
    print(f"O maior número é {num1}")
elif num2 > num1:
    print(f"O maior número é {num2}")
else: 
    print("Os dois números são iguais")
  