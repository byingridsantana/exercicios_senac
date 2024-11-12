// Crie um programa onde o vendedor entra com o preço do produto,
// um percentual de desconto e programa exiba: O valor do desconto e preço final do produto

#include <stdio.h>

int main(){
    float preco, percentual_desconto, valor_desconto, preco_final;

    printf("Digite o preço do produto: R$ ");
    scanf("%f", &preco);

    printf("Digite o percentual de desconto (em %%): ");
    scanf("%f", &percentual_desconto);

    valor_desconto = (percentual_desconto / 100) * preco;

    preco_final = preco - valor_desconto;

    printf("Valor do desconto: R$ %.2f\n", valor_desconto);
    printf("Preco final do produto: R$ %.2f\n", preco_final);

    return 0;
}
