// Somatório com for  
// Fig. 4.5: fig04_05.c

#include <stdio.h> 
 
// função main inicia a execução do programa 
 
int main(void) 
{ 
int soma = 0;                                           // inicializa soma
int número;                                             // número a ser acrescido à soma

for (número = 2; número <= 100; número += 2) { 
soma += número;                                         // adiciona número à soma 
}                                                       // fim do for  

printf("Soma é %d\n", soma);                            // exibe soma 
return 0;                                               // indica que o programa foi concluído com sucesso
}                                                       // fim da função main