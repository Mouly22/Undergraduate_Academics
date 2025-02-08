#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>


int main() {
    pid_t Parentpid,childpid;
    int status;
    int counter = 1;

    Parentpid = fork(); 

    if (Parentpid == -1) {
        perror("Parent fork failed");
        exit(EXIT_FAILURE);
    } else if (Parentpid == 0) {
        counter += 1;
        printf("%d.Child process ID: %d\n",counter,getpid());
        
        
        for (int i =0;i<3;i++){
        childpid = fork(); 
        counter += 1;
        
        
         if (childpid ==0) {
                printf("%d.Grand Child process ID: %d\n",counter,getpid());
                 
                exit(EXIT_SUCCESS); 
        }
         wait(&status); 
    }
    exit(EXIT_SUCCESS); 
    } else {
        printf("%d.Parent process ID: %d\n",counter,getpid());
        
        wait(&status); 

    }

    return EXIT_SUCCESS;
}
