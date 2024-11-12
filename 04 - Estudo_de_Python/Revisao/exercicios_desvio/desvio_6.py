# Faça um programa que pergunte em que turno você estuda. Peça para digitar M- matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom dia", "Boa tarde", "Boa Noite" ou "Valor Inválido", conforme o caso.


turno = input("Em que turno você estuda? (M- matutino ou V-Vespertino ou N- Noturno): ")

if turno == 'M' or turno == 'm':
    print("Bom dia")
elif turno == 'V' or turno == 'v':
    print("Boa tarde")
elif turno == 'N' or turno == 'n':
    print("Boa Noite")
else:
    print("Valor Inválido Inválido")