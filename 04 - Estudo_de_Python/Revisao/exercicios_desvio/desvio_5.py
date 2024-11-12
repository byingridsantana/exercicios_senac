# Faça um programa que leia três números e mostre o maior deles.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

if num1 >= num2 and num1 >= num3:
    print(f"O maior número é {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"O maior número é {num2}")
else: 
    print(f"O maior número é {num3}")