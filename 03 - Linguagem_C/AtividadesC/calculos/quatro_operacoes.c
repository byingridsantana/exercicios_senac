// Crie um programa em C que receba dois números e realize as quatro operações matemáticas; 

#include <stdio.h> 

int main() {
    int num1, num2, rs;

    printf("Digite um número: \n");
    
    scanf("%d", &num1);

    printf("Digite outro número: \n");
    scanf("%d", &num2);

    rs = num1 + num2;
    printf("O resultado da soma é: %d \n", rs);

    rs = num1 - num2;
    printf("O resultado da subtração: é %d \n", rs);

    rs = num1 * num2;
    printf("O resultado da multiplicação é: %d \n", rs);

    rs = num1 / num2;
    printf("O resultado da divisão é: %d \n", rs);

    return 0;
}