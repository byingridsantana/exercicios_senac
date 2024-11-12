# Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo - Inválido

sexo = input("Digite F para Feminino ou M para Masculino: ")

# if sexo == 'f' or sexo == 'F':
#     print("Feminino")
# elif sexo == 'm' or sexo == 'M':
#     print("Masculino")
# else:
#     print("Sexo Inválido")

sexo = sexo.lower() 
if sexo == "f":
    print("Feminino")
elif sexo == "m":
    print("Masculino")
else:
    print("Sexo inválido")