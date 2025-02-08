#include <stdio.h>
#include <string.h>

int num_Perfect(int num){
    int count,rem1;

        count = 0;
        for (int i = 1; i < num; i ++){
            
            rem1 = num % i;
            
            if (rem1 == 0){
                count += i;
            }
            
        }
        if (count == num){
            return 1;
            
        }
    return 0;
    
}


int main() {

    int q1,q2,flag;
    scanf("%d", &q1);
    scanf("%d", &q2);
    
    for (int number = q1; number <= q2; number ++){
        flag = num_Perfect(number);
        
        if(flag ==1){
            printf("%d\n",number);
        }
    }

  

    
  return 0;
}
