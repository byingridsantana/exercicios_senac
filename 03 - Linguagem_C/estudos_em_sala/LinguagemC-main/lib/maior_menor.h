int maior_valor(int array[], int qtd){                     // [] é um array
     int m = array[0];
     int i = 1;
     while(i <= qtd-1){
        if(array[i] > m){
        m = array[i];
        }   
        i++;     
     }
     
    return m; 
}                   

int menor_valor(int array[], int qtd){                     // [] é um array
     int m = array[0];
     int i = 1;
     while(i <= qtd-1){
        if(array[i] < m){                                  // menor valor
        m = array[i];
        }   
        i++;     
     }
     
    return m; 
}  