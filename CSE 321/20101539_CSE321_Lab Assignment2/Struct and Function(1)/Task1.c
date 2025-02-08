#include <stdio.h>
#include <string.h>





int main() {
    
    
    struct Paratha {
      int count;
      int unitcount;
    } obj1;
    
    
    struct Vegetable {
      int count;
      int unitcount;
    } obj2;
    
    
    struct Water {
      int count;
      int unitcount;
    } obj3;

float friendspay,friendcount,totalPayment;
  
  
    printf("Quantity Of Paratha:");
    scanf("%d", &obj1.count);
    printf("Unit Price:");
    scanf("%d", &obj1.unitcount);
    
    printf("Quantity Of Vegetables:");
    scanf("%d", &obj2.count);
    printf("Unit Price:");
    scanf("%d", &obj2.unitcount);

    printf("Quantity Of Mineral Water:");
    scanf("%d", &obj3.count);
    printf("Unit Price:");
    scanf("%d", &obj3.unitcount);
    

    
    
    printf("Number of People:");
    scanf("%f", &friendcount);
    
    totalPayment = obj1.count * obj1.unitcount + obj2.count * obj2.unitcount + obj3.count * obj3.unitcount;
    //printf("%d\n",total_sum);
  friendspay = totalPayment / friendcount;
  
  printf("Individual people will pay: %.2ftk\n",friendspay);
    
  return 0;
}
