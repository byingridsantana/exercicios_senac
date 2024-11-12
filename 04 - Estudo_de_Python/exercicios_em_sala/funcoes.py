def soma(num1, num2):
    return num1 + num2 

def somaLista(lista):
    rs = 0
    for i in lista:
        rs+=i
    print(f"O resultado da soma é: {rs}")