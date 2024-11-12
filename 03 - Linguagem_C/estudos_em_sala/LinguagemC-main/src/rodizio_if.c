#include <stdio.h>

int main(){
    int final_placa;
        printf("Digite o final da placa do seu veículo:\n");
    scanf("%d",&final_placa);

    if(final_placa == 1){
        printf("Você não pode sair com veículo na segunda-feira\n");
    }
    else if(final_placa == 2){
        printf("Você não pode sair com veículo na segunda-feira\n");
    }
    else if (final_placa == 3){
        printf("Você não pode sair com veículo na terça-feira\n");
    }
    else if (final_placa == 4){
        printf("Você não pode sair com veículo na terça-feira\n");
    }
    else if (final_placa == 5){
        printf("Você não pode sair com veículo na quarta-feira\n");
    }
    else if (final_placa == 6){
        printf("Você não pode sair com veículo na quarta-feira\n");
    }
    else if (final_placa == 7){
        printf("Você não pode sair com veículo na quinta-feira\n");
    }
    else if (final_placa == 8){
        printf("Você não pode sair com veículo na quinta-feira\n");
    }
    else if (final_placa == 9){
        printf("Você não pode sair com veículo na sexta-feira\n");
    }
    else if (final_placa == 0){
        printf("Você não pode sair com veículo na sexta-feira\n");
    }
    else{
        printf("Final de placa inexistente\n");
    }

    return 0;
}