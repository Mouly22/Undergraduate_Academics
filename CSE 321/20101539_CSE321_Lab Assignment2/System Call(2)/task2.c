#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>

int main() {
    pid_t Parentpid,childpid;
    int status;

    Parentpid = fork(); 

    if (Parentpid == -1) {
        perror("Parent fork failed");
        exit(EXIT_FAILURE);
    } 
    else if (Parentpid == 0) {
        childpid = fork(); 
        
        if (childpid == -1) {

        perror("Child fork failed");
        exit(EXIT_FAILURE);
        } else if (childpid >0){
            
                    wait(&status); 
                    printf("I am child\n");
                    exit(EXIT_SUCCESS); 
        }
        else {
                printf("I am grandchild\n");
                exit(EXIT_SUCCESS); 
        }
    } else {

        wait(&status); 
        printf("I am parent\n");
    }

    return EXIT_SUCCESS;
}
