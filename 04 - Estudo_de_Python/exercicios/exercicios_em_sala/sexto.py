numero_placa = input("Digite o número final da placa do veículo: ")

match numero_placa:
    case "1" | "2": print("Rodizio na segunda-feira")
    case "3" | "4": print("Rodizio na terça-feira") 
    case "5" | "6": print("Rodizio na quarta-feira") 
    case "7" | "8": print("Rodizio na quinta-feira") 
    case "9" | "0": print("Rodizio na sexta-feira") 
    case _: print("Final de placa inválido") 