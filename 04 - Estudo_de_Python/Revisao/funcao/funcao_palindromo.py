# Faça uma que verifique se uma palavra é um palindromo.

def verificar_palindromo(palavra):
    # Convertendo para minúsculas para ignorar diferenças de maiúsculas/minúsculas
    palavra = palavra.lower()
    
    # Verificando se a palavra é igual à sua versão invertida
    if palavra == palavra[::-1]:
        return "é um palíndromo"
    else:
        return "não é um palíndromo"


# Testando com uma palavra
resultado = verificar_palindromo("level")
print("A palavra level", resultado) 

# Testando com uma palavra que não é palíndromo
resultado = verificar_palindromo("computer")
print("A palavra computer", resultado)  
