#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
#include <unistd.h>

#define MaxCrops 5
#define warehouseSize 5

pthread_mutex_t count_mutex= PTHREAD_MUTEX_INITIALIZER;
sem_t empty;
sem_t full;
int in = 0;
int out = 0;
char crops[warehouseSize] = {'R', 'W', 'P', 'S', 'M'};
char warehouse[warehouseSize] = {'N', 'N', 'N', 'N', 'N'};
pthread_mutex_t mutex;

void *Farmer(void *far) {
    int *num1 = (int *)far;
    int farmerprogress = 0;
    char farmerslist[warehouseSize] = {'R', 'W', 'P', 'S', 'M'};

    while (farmerprogress < MaxCrops) {
        pthread_mutex_lock(&count_mutex);

        if (warehouse[in] == 'N' && farmerslist[in] != 'N') {
            sem_wait(&empty);
            warehouse[in] = crops[in % warehouseSize];
            printf("Farmer %d: Insert crops %c at %d\n", *num1, warehouse[in], in);
            farmerslist[in] = 'N';
            in = (in + 1) % warehouseSize;
            farmerprogress++;
            sem_post(&full);
        }

        pthread_mutex_unlock(&count_mutex);
    }

    printf("Farmer%d: ", *num1);
    int i = 0;
    while (i < warehouseSize) {
        printf("%c", warehouse[i]);
        i++;
    }
    printf("\n");
    return 0;
}

void *ShopOwner(void *sho) {
    int *num1 = (int *)sho;
    int shopownerprogress = 0;

    while (shopownerprogress < MaxCrops) {
        pthread_mutex_lock(&count_mutex);
        char shoplist[warehouseSize] = {'N', 'N', 'N', 'N', 'N'};

        if (warehouse[out] != 'N' && shoplist[out] == 'N') {
            sem_wait(&full);
            char crop = warehouse[out];
            printf("Shop owner %d: Remove crops %c from %d\n", *num1, crop, out);
            warehouse[out] = 'N';
            shoplist[out] = crop;
            out = (out + 1) % warehouseSize;
            shopownerprogress++;
            sem_post(&empty);
        }

        pthread_mutex_unlock(&count_mutex);
    }

    printf("ShopOwner%d: ", *num1);
    int i = 0;
    while (i < warehouseSize) {
        printf("%c", warehouse[i]);
        i++;
    }
    printf("\n");
    return 0;
}

int main() {
    pthread_mutex_init(&mutex, NULL);
    sem_init(&empty, 0, warehouseSize);
    sem_init(&full, 0, 0);

    pthread_t Far[5], Sho[5];
    int a[5] = {1, 2, 3, 4, 5};

    int val = 0;
    while (val < 5) {
        pthread_create(&Far[val], NULL, Farmer, (void *)&a[val]);
        val++;
    }

    val = 0;
    while (val < 5) {
        pthread_create(&Sho[val], NULL, ShopOwner, (void *)&a[val]);
       val++;
    }

   val = 0;
    while (val < 5) {
        pthread_join(Far[val], NULL);
        val++;
    }

    val = 0;
    while (val < 5) {
        pthread_join(Sho[val], NULL);
        val++;
    }

    pthread_mutex_destroy(&mutex);
    sem_destroy(&empty);
    sem_destroy(&full);

    return 0;
}