#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

void exec_ChildProcess(char *program, char *argv[], int argc) {
    char *args[argc + 1];
    args[0] = program;
    for (int i = 1; i < argc; i++) {
        args[i] = argv[i];
    }
    args[argc] = NULL;

    execvp(args[0], args);
    perror("Exec failed");
    exit(1);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <numbers>\n", argv[0]);
        return 1;
    }

    pid_t v1 = fork();

    if (v1 < 0) {
        perror("Fork failed");
        return 1;
    } else if (v1 == 0) {
        printf("Sorted Array:\n");
        exec_ChildProcess("./sort", argv, argc);
    } else {
        wait(NULL);

        printf("Odd/even status:\n");
        exec_ChildProcess("./oddeven", argv, argc);
    }

    return 0;
}
