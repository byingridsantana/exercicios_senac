#include <stdio.h>

    int main(){
        char nome[]= "Ingrid";
        int i = 0;

        for(i ; i <= 5 ; i++){
        printf("%c -> %d -> %p\n", nome[i], nome[i], &nome[i]);
        }
        return 0;
    }