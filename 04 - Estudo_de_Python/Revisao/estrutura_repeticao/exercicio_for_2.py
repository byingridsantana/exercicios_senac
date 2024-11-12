# Faça um programa que leia 5 números e informe a soma e a média dos números.
numeros = []
for x in range(0,5):
    n = int(input("Digite um valor: "))
    numeros.append(n)

# Exibir os números adicionados
    print(numeros)

# variável da soma
soma = 0 
for i in numeros:
    soma+=1

#exibir a soma
print("A soma dos valores é: "+str(soma))
print("A média dos valores é: "+str(soma/len(numeros)))