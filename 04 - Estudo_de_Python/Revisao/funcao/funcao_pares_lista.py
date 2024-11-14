#Faça uma funcao que receba uma lista e retorne uma nova lista com os elementos pares da lista original

def filtrar_pares(lista):
    lista_pares = []  # Lista vazia para armazenar os pares
    for num in lista:  # Percorre cada elemento da lista 
        if num % 2 == 0:  # Verifica se o número é par
            lista_pares.append(num)  # Adiciona o número par na nova lista
    return lista_pares

# Lista de exemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Chamando a função
pares = filtrar_pares(numeros)

# Exibindo o resultado
print(pares)
