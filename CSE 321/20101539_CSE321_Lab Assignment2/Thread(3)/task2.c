#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

int num = 1;
int count = 0;

void *worker(int *val) {
    int i = 0;
    while(i < 5) {
        printf("Thread %d prints %d \n", count, *val);
        *val += 1;
        i++;
    }
    count += 1;
}

int main() {
    pthread_t threads[5];
    int i = 0;
    
    while(i < 5) {
        pthread_create(&threads[i], NULL, (void *)worker, &num);
        pthread_join(threads[i], NULL);
        i++;
    }
    
    return 0;
}
