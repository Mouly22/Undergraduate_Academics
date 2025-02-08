#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/wait.h>

void update_process_count() {
    int crt_process;
    int fd = open("textfile.txt", O_CREAT | O_RDWR, 0666);

    read(fd, &crt_process, sizeof(int));
    crt_process++;

    lseek(fd, -sizeof(int), SEEK_CUR);
    write(fd, &crt_process, sizeof(int));
      close(fd);
}

void handle_child_logic(pid_t a, pid_t b, pid_t c) {
    if (getpid() % 2 != 0) {
        update_process_count();
        fork();
        wait(NULL);
    }
    exit(EXIT_SUCCESS);
}

int main() {
    int fd = open("textfile.txt", O_CREAT | O_RDWR, 0666);

    if (fd < 0) {
        perror("Failed to open file");
        exit(EXIT_FAILURE);
    }

    int crt_process= 3; 
    write(fd, &crt_process, sizeof(int));
    lseek(fd, 0, SEEK_SET);

    pid_t origin_parent_pid = getpid();
    pid_t a = fork();
    pid_t b = fork();
    pid_t c = fork();
      close(fd);
    if (a == 0 && b != 0 && c != 0) {
        handle_child_logic(a, b, c);
    }

    if (a != 0 && b == 0 && c != 0) {
        handle_child_logic(a, b, c);
    }

    if (a != 0 && b != 0 && c == 0) {
        handle_child_logic(a, b, c);
    }


    wait(NULL);

    if (getpid() == origin_parent_pid) {
    
    int fd = open("textfile.txt", O_CREAT | O_RDWR, 0666);
        read(fd, &crt_process, sizeof(int));
        printf("Amount of Process got created:%d\n", crt_process);
    }

    close(fd);
    return 0;
}
