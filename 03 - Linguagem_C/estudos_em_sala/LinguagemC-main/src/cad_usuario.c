#include <stdio.h>
#include "../lib/usuario.h"

int main (){
    // Seclaração da estrutura Usuario como us
    Usuario us;  

    // Declaração do tipo FILE para manipular arquivos

    FILE *arq;

    // Limpar a tela do terminal
    system("clear");
    printf("**************************************************\n");
    printf("**************Cadastro do Usuário*****************\n");
    printf("**************************************************\n");
    printf("Digite o nome de usuário:\n");
    //fgets pega o que o usuário escreveu no terminal
    fgets(us.nomeusuario,20,stdin);
    printf("%s", us.nomeusuario); 
    printf("%d\n", sizeof(us.nomeusuario),stdin);

    printf("Digite a senha do usuário:\n");
    fgets(us.senha,sizeof(us.senha),stdin);

    printf("Digite o nivel de acesso:\n");
    fgets(us.nivel, sizeof(us.nivel),stdin);

    // Vamos abrir o arquivo para salvar o usuário
    arq = fopen("file/usuarios.txt", "a+"); 

    // Gravar os dados no arquivo de texto
    fputs(us.nomeusuario,arq); 
    fputs(us.senha,arq);
    fputs(us.nivel,arq); 

    // Para retirar o arquivo da memória será usado o comando fclose
    fclose(arq); 

    return 0;
}