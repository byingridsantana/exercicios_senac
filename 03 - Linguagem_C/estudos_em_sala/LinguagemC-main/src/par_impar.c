#include <stdio.h>

int main (){
 int num; 
 printf("Digite um número:\n");
 scanf("%d", &num);
 if (num % 2 == 0){
    printf("O número digitado é PAR\n");
}
 else{
    printf("O número digitado é IMPAR\n");
} 
    
return 0;

}

