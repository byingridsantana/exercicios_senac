#include <stdio.h>
#include "../lib/maior_menor.h" 

int main(){

    int numeros[7] = {15,78,6,0,48,12,4};

    printf("O maior valor do array é: %d\n", maior_valor(numeros,7)); 
    printf("O menor valor é: %d\n", menor_valor(numeros,7)); 

    return 0;
}