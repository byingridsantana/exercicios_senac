# Escreva uma função que receba uma lista de números e retorne a media aritmética

def calcular_media(lista):
    # Verifica se a lista não está vazia
    if len(lista) == 0:
        return "A lista está vazia, não é possível calcular a média."
    
    # Calculando a soma dos números na lista
    soma = sum(lista)
    
    # Calculando a quantidade de elementos na lista
    quantidade = len(lista)
    
    # Calculando a média
    media = soma / quantidade
    
    return media

# Testando com uma lista de números
numeros = [10, 20, 30, 40, 50]
resultado = calcular_media(numeros)
print(f"A média dos números é: {resultado}")

