def saudacao(nome=""):
    print(f"Olá, {nome}! Seja bem-vindo(a)")

def area_retangulo(base = 0,altura = 0):
    area = base * altura
    return area

def potencia(base, expoente):
    resultado = base ** expoente
    return resultado 

def soma (*numeros):
    resultado = 0
    for i in numeros:
        resultado += i
    return resultado

def soma2(a,b):
    return a+b