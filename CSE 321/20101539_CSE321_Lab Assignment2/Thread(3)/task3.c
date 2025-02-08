#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *calculate_sum(void *arg);
void *check_results(void *arg);
int sums[3];

int main() {
    pthread_t threads[4];
    char strings[3][100] = {"pytho", "python", "chitah"};

    for (int i = 0; i < 3; i++) {
        pthread_create(&threads[i], NULL, calculate_sum, (void *)strings[i]);
    }

    for (int i = 0; i < 3; i++) {
        int *result;
        pthread_join(threads[i], (void *)&result);
        sums[i] = *result;
    
    }

    pthread_create(&threads[3], NULL, check_results, (void *)sums);
    pthread_join(threads[3], NULL);
    return 0;
}

void *calculate_sum(void *arg) {
    char *str = (char *)arg;
    int sum = 0;


    for (int i = 0; str[i] != '\0'; i++) {
        sum += str[i];
    }

    int *result = malloc(sizeof(int));
    *result = sum;
    pthread_exit((void *)result);
}

void *check_results(void *arg) {
    int *sums = (int *)arg;
    int sum1 = sums[0];
    int sum2 = sums[1];
    int sum3 = sums[2];

    if (sum1 == sum2 && sum1 == sum3) {
        printf("Youreka\n");
    } else if (sum1 == sum2 || sum1 == sum3 || sum2 == sum3) {
        printf("Miracle\n");
    } else {
        printf("Hasta la vista\n");
    }

    pthread_exit(NULL);
}
