#include "stdio.h"
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int entier;

    pid_t pid = fork();
    if (pid == 0) {
        printf("Veuillez entrer une veleur : ");
        scanf("%d", &entier);
        exit(entier);
    }
    wait(&entier);
    printf("Value : %d", WEXITSTATUS(entier));
    return 0;
}