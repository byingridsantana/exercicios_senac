numeros = []

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

#adicionar os numeros a lista

numeros.append(n1)
numeros.append(n2)
numeros.append(n3)

maior = numeros[0]
for n in numeros:
    if n > maior:
        maior = n
print("O maior número é ",maior)