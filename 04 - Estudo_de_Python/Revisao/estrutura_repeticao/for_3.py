vogal = ['a', 'e', 'i', 'o', 'u']
letra = input("Digite uma letra ")
letra = letra.lower()

for v in vogal: 
    if letra == v:
        print("A letra digitada é uma vogal")
        break