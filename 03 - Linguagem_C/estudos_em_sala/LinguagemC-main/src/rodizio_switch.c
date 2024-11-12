#include <stdio.h>

int main (){
    int final_placa;
    printf("Digite o número final da placa do seu veículo:\n");
    scanf("%d", &final_placa);

    switch(final_placa){
        case 1:
            printf("Rodizio na segunda-feira\n");
            break;
    
        case 2:
            printf("Rodizio na segunda-feira\n");
            break;
   
        case 3:
            printf("Rodizio na terça-feira\n");
            break;
        case 4:
        printf("Rodizio na terça-feira\n");
            break;
        case 5:
        printf("Rodizio na quarta-feira\n");
            break;
        case 6:
        printf("Rodizio na quarta-feira\n");
            break;
        case 7:
        printf("Rodizio na quinta-feira\n");
            break;
        case 8:
        printf("Rodizio na quinta-feira\n");
            break;
        case 9:
        printf("Rodizio na sexta-feira\n");
            break;
        case 0: 
        printf("Rodozio na sexta-feira\n");
            break;
        default:
        printf("Final da placa inexistente\n");
    }       
    
}