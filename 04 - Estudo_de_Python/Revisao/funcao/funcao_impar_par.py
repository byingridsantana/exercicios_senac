# Escreva uma função que verifique se um número é par ou impar

def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
numero = 10
resultado = verificar_par_impar(numero)
print('O número ' + str(numero) + ' é ' + resultado)

numero = 15
resultado = verificar_par_impar(numero)
print('O número ' + str(numero) + ' é ' + resultado)

