#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

void create_binary_tree(int level, int max_level) {
    pid_t pid1, pid2;

    if (level < max_level) {
        if ((pid1 = fork()) == 0) {
            printf("pid processus gauche : %d, processus parent : %d \n", getpid(), getppid());
            create_binary_tree(level+1, max_level);
            exit(0);
        }

        if ((pid2 = fork()) == 0) {
            printf("pid processus droite : %d, processus parent : %d \n", getpid(), getppid());
            create_binary_tree(level+1, max_level);
            exit(0);
        }
        if (level == max_level-1){
            system("pstree");
        }
        wait(NULL);
        wait(NULL);
    }
}

int main(int argc, char *argv[]) {
    int n;

    if (argc != 2) {
        printf("Usage : %s <n>\n", argv[0]);
    }
    n = atoi(argv[1]);
    printf("pid processus racine : %d\n", getpid());

    create_binary_tree(0, n);


    return 0;
}

