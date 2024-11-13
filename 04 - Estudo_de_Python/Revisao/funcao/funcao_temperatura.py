# Faça uma função que converta uma temperatura em Celsius para Fahrenheit

def celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperatura_fahrenheit = celsius_fahrenheit(25)
print(f'A temperatura de 25°C é igual a {temperatura_fahrenheit}°F')
