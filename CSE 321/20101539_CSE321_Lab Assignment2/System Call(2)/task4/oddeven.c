#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    for (int i = 1; i < argc; i++) {
        int num = atoi(argv[i]);
        if (num % 2 != 0) {
            printf("%d is Odd Number!\n", num);
        } else {
            printf("%d is Even Number!\n", num);
        }
    }

    return 0;
}
