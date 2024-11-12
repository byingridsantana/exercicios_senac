// Crie um programa em C que receba um número e exiba ao usuário o resto da divisão

#include <stdio.h>

int main(){
 int num1, resto, rs; 

 printf("Digite um número: \n");
 scanf("%d", &num1); 

 rs = num1 % 2;
 printf("O resto da divisão é: %d \n", rs);

}