#include <stdio.h>
#include <stdlib.h>

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int maxIdx = i; 
        for (int j = i + 1; j < n; j++) {
            if (arr[j] > arr[maxIdx]) { 
                maxIdx = j;
            }
        }
       
        int temp = arr[maxIdx];
        arr[maxIdx] = arr[i];
        arr[i] = temp;
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <numbers>\n", argv[0]);
        return 1;
    }

    int n = argc - 1;
    int numbers[n];

    for (int i = 0; i < n; i++) {
        numbers[i] = atoi(argv[i + 1]);
    }
    selectionSort(numbers, n);
    for (int i = 0; i < n; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    return 0;
}
