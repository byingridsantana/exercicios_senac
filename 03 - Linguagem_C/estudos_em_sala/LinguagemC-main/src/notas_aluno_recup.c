#include <stdio.h>

int main(){

    float nota1, nota2, nota3, nota4, mediafinal;

    printf("Digite a primeira nota:\n");
     scanf("%f",&nota1);
    printf("Digite a segunda nota:\n");
     scanf("%f",&nota2);
    printf("Digite a terceira nota\n");
     scanf("%f",&nota3);
    printf("Digite a quarta nota\n");
     scanf("%f",&nota4);
    
    mediafinal = (nota1 + nota2 + nota3 + nota4) / 4;

    /*
    Para alunos com média maior ou igual a 6, aprovado!
    Para alunos com média menor ou igual a 4, reprovado!
    Para os demais com notas entre maior 4 e menor 6, recuperação!
    */

    if (mediafinal >= 6){
        printf("O ALUNO ESTÁ APROVADO! - Sua média final é: %.2f\n", mediafinal);
}

    else if (mediafinal <= 4){   
    printf("O ALUNO ESTÁ REPROVADO! - Sua média final é: %.2f\n", mediafinal);
} 

    else {
    printf("O ALUNO ESTÁ EM RECUPERAÇÃO! - Sua média final é: %.2f\n", mediafinal);
    }

}