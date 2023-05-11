#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"
#include "sys/wait.h"

int main() {
    char commande[20];
    sprintf(commande, "pstree %d", getpid());
    pid_t pid = fork();
    if (pid == 0) {
        printf("pid enfant : %d, pid parent : %d\n", getpid(), getppid());
        exit(0);
    } else {
        system(commande);
        sleep(5);
        wait(NULL);
    }
}