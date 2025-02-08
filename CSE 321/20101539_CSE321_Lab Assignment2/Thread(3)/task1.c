#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void *func_thread(void *arg);
int arr[5] = {1, 2, 3, 4, 5};

int main() {
    pthread_t t[5];

    for (int i = 0; i < 5; i++){
        pthread_create(&t[i], NULL, func_thread, &arr[i]);
        pthread_join(t[i], NULL);
    }
    return 0;
}

void *func_thread(void *arg){
    int x = *(int *)arg;
    printf("thread-%d running\n",x);
    printf("thread-%d closed\n", x);
    return NULL;
}
