age = int(input("Digite sua idade: "))
if age < 4:
    print("Entrada Gratuita")
elif age >= 4 and age < 18:
    print("Ingresso R$ 5,00")
elif age >= 8 and age < 65:
    print("Ingresso R$ 10,00")
elif age >= 65 and age < 101:
    print("Entrada Gratuita")
