# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número
base = int(input("Digite um valor para base: "))
exponente = int(input("Digite um valor para o exponente "))

n = base
rs = 0 

for i in range (0,exponente-1):
    n = n * base

print("O resultado da potência é: "+str(n))