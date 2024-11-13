# Faça uma que verifique se uma palavra é um palindromo.

def verificar_palindromo(palavra):
    # Convertendo para minúsculas para ignorar diferenças de maiúsculas/minúsculas
    palavra = palavra.lower()
    
    # Verificando se a palavra é igual à sua versão invertida
    if palavra == palavra[::-1]:
        return "É um palíndromo"
    else:
        return "Não é um palíndromo"


# Testando com uma palavra
resultado = verificar_palindromo("level")
print("Resultado:", resultado) 

# Testando com uma palavra que não é palíndromo
resultado = verificar_palindromo("computer")
print("Resultado:", resultado)  
