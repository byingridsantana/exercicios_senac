#include <stdio.h> 
// para trabalhar com arquivos, é necessário importar a biblioteca stdlib
#include <stdlib.h>
// importar a biblioteca de texto(string) para escrever em arquivos de texto
#include <string.h>

int main(){
    system("clear"); //limpa o terminal

    // Declaração da variável palavra como um ponteiro
    // para guardar os caracteres que forma uma string
    char *palavra;
    char *label_name = "Nome: ";
    printf("Digite seu nome completo:\n");    
    //scanf ("%s", palavra);
    // O comando fgets (f -> file | gets -> obter). Assim iremos obter o texto que o usuário esta digitando no terminal.
    // Definimos também a quantidade de caracteres aceitos pelo fgets e o parâmetro stdin (std -> standard | in -> entrada)
    // ele olha para entrada padrão, que neste caso é teclado pelo terminal    
    fgets (palavra, 20, stdin);

    FILE *ar;
    ar = fopen("files/teste.txt", "a+"); //"w" = string
    fseek(ar,0, SEEK_END); // joga no final da linha
    fputs(label_name, ar); 
    fputs(palavra,ar); // escreve no arquivo

    printf("O arquivo está no endereço: %p\n", ar);
    fclose(ar);

    return 0;
}