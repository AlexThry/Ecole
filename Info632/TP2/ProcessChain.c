#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>


int main(int argc, char *argv[]) {
    int n;
    pid_t pid;

    if (argc != 2) {
        printf("Usage: %s <n>\n", argv[0]);
    }

    n = atoi(argv[1]);

    for (int i = 0; i < n; i++) {
        pid = fork();

        if (pid == -1) {
            perror("fork");
            exit(1);
        } else if (pid == 0) {
            printf("Child : %d, pid : %d, ppid : %d\n", i+1, getpid(), getppid());
        } else {
            wait(NULL);
            exit(0);
        }
    }

    system("pstree");
    return 0;
}
