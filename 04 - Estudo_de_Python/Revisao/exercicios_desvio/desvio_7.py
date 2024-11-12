# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
salario = float(input("Digite o seu salário: "))

valor_aumento = 0
novo_salario = 0

if salario <= 280:
    valor_aumento = salario * 20/100
    novo_salario = salario + valor_aumento
    print("O seu salário atual é "+str(salario)+" 20% de aumento. O valor do aumento é "+str(valor_aumento))+ "e o novo salario é "+str(novo_salario)

elif salario < 700: 
    valor_aumento = salario * 15/100
    novo_salario = salario + valor_aumento
    print("O seu salário atual é "+str(salario)+" 20% de aumento. O valor do aumento é "+str(valor_aumento))+ "e o novo salario é "+str(novo_salario)

elif salario < 1500: 
    valor_aumento = salario * 10/100
    novo_salario = salario + valor_aumento
    print("O seu salário atual é "+str(salario)+" 10% de aumento. O valor do aumento é "+str(valor_aumento))+ "e o novo salario é "+str(novo_salario)

else: 
    valor_aumento = salario * 5/100
    novo_salario = salario + valor_aumento
    print("O seu salário atual é "+str(salario)+" 5% de aumento. O valor do aumento é "+str(valor_aumento))+ "e o novo salario é "+str(novo_salario)