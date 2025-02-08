#include <stdio.h>
#include<unistd.h>
#include<fcntl.h>
#include<sys/stat.h>
#include<string.h>
#include<sys/types.h>

int main(){

int out_file;
char arr[100];

for (int i =1; i >0; i++){

printf("Enter input Text: ");
fgets(arr, 100, stdin);

out_file = open("task1text.txt",O_WRONLY|O_APPEND|O_CREAT,0644);

if (arr[0] == '-' && arr[1] == '1'){
close(out_file);
return 0;
}
write(out_file,arr,strlen(arr));

}

}
