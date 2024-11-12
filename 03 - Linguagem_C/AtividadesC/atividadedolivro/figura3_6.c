// Programa de média da turma com repetição controlada por contador 

// Figura 3.6: fig03_06

#include <stdio.h>
 
int main(void) {
int contador;                                   // número da nota a digitar em seguida
int nota;                                       // valor da nota
int total;                                      // soma das notas inseridas pelo usuário
int média;                                      // média das notas

// fase de inicialização

total = 0;                                      // inicializa total
contador = 1;                                   // inicializa contador do loop

// fase de processamento

while ( contador <= 10 ) {                      //loop 10 vezes
printf( "Digite a nota:" );                     // prompt para inserção 
scanf( "%d", &nota );                           // lê a nota do usuário
 total = total + nota;                          // soma nota ao total
contador = contador + 1;                        // incrementa contador
}                                               // fim do while

// fase de término

média = total / 10;                             // divisão de inteiros 

printf( "Média da turma é %d\n", média );       //exibe resultado

return 0;                                       // indica que programa foi concluído com sucesso
}                                               // fim da função main 