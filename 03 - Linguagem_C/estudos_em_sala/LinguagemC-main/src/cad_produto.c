#include <stdio.h>
#include "../lib/produto.h"

int main(){
    system("clear");
    Produto prod;
    printf("-------------------------------------------------\n");
    printf("--------------- Cadastro de Produto -------------\n");
    printf("-------------------------------------------------\n");

    printf("Digite o nome do produto:\n");
    fgets(prod.nome, sizeof(prod.nome),stdin);

    printf("Digite a categoria do produto:\n");
    fgets(prod.categoria, sizeof(prod.categoria),stdin);

     printf("Digite o código do produto:\n");
    scanf("%d", &prod.codigo); 

    printf("Digite o estoque do produto:\n");
    scanf("%d",&prod.estoque);

    printf("Digite o preço do produto:\n");
    scanf("%f",&prod.preco);

    // Exibindo o produto cadastrado

    printf("\n--------------------- Produto Cadastrado -------------------------\n");
    printf("%d - %s - %s - %d - %.2f\n", prod.codigo, prod.nome, prod.categoria, prod.estoque, prod.preco);


}