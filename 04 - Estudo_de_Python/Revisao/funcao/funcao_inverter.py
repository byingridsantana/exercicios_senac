# texto = "Quinta"
# tm = len(texto)
# print(tm)

# print(texto[0])  
# print(texto[5])    
# print(texto[6-1])      
# print(texto[tm-1])    
#for i in range(5,-1,-1):
#    print(texto[i], end="")

def inverter(texto):
    tam = len(texto)
    # Criar variavel que devolve o texto invertido
    txt_invertido=""
    for i in range(tam-1,-1,-1):
        txt_invertido += texto[i]
    return txt_invertido