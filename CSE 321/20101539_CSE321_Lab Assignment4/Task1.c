#include <pthread.h>
#include <stdio.h>
#include <string.h>

#define MAX 10      // Producers and consumers can produce and consume up to MAX
#define BUFLEN 6    
#define NUMTHREAD 2

void *consumer(void *id);
void *producer(void *id);

char buffer[BUFLEN];
char source[BUFLEN]; 
int pCount = 0; 
int cCount = 0; 
int buflen;

pthread_mutex_t count_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t nonEmpty = PTHREAD_COND_INITIALIZER;
pthread_cond_t full = PTHREAD_COND_INITIALIZER;
int thread_id[NUMTHREAD] = {0,1};
int i = 0;
int j = 0;

int main() {
    int i;
    pthread_t thread[NUMTHREAD];
    strcpy(source,"abcdef");
    buflen = strlen(source);
    
    pthread_create(&thread[0], NULL, producer, NULL);
    pthread_create(&thread[1], NULL, consumer, NULL);
    
    pthread_join(thread[0], NULL);
    pthread_join(thread[1], NULL);
    
    return 0;
}

void *producer(void *id) {
    int val1 = 0;
    while (val1 < MAX) {
        pthread_mutex_lock(&count_mutex);
        
        
        while ((pCount - cCount) >= 2) {  
            pthread_cond_wait(&full, &count_mutex);
        }
    
        buffer[pCount % buflen] = source[pCount % 6];  
        printf("%d produced %c by Thread 0\n", pCount, buffer[pCount % buflen]);
        pCount++;
        
        pthread_cond_signal(&nonEmpty);
        pthread_mutex_unlock(&count_mutex);
        val1 += 1;
    }
    return NULL;
}

void *consumer(void *id) {
    int val2 = 0;
    while ( val2 < MAX) {
        pthread_mutex_lock(&count_mutex);
   
        while (pCount <= cCount) {
            pthread_cond_wait(&nonEmpty, &count_mutex);
        }
        
        char consumed = buffer[cCount % buflen];
        buffer[cCount % buflen] = 'K';
        printf("%d consumed %c by Thread 1\n", cCount, consumed);
        cCount++;
        
        pthread_cond_signal(&full);
        pthread_mutex_unlock(&count_mutex);
        val2 += 1;
    }
    return NULL;
}