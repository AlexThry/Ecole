#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>
/* Global variables */
int x = 0;
int count = 0;
sem_t *sem1, *sem2, *sem3;

void a1();
void a2();
void b1();
void b2();



/* Thread function */

void a1(){
    printf("a1\n");
    sleep(1);

}
void a2(){
    printf("a2\n");
}

void b1() {
    printf("b1\n");
    sleep(1);
}
void b2() {
    printf("b2\n");
}

void *p1(void *arg) {
    a1();
    /* send signal to the created thread */
    sem_post(sem1);
    sem_wait(sem2);
    a2();
}

void *p2(void *arg) {
    /* wait for signal from main thread */
    sem_wait(sem1);
    b1();
    sem_post(sem2);
    b2();
}


int main () {
    sem1 = sem_open("sem1", O_CREAT, 0644, 0);
    sem2 = sem_open("sem2", O_CREAT, 0644, 0);

    pthread_t thread1, thread2;
    /* semaphore sync should be initialized by 0 */
    if (sem1 == SEM_FAILED) {
        perror("Could not initialize mylock semaphore");
        exit(2);
    }
    if (pthread_create(&thread1, NULL, p1, NULL) < 0) {
        perror("Error: thread cannot be created");
        exit(1);
    }
    if (pthread_create(&thread2, NULL, p2, NULL) < 0) {
        perror("Error: thread cannot be created");
        exit(1);
    }
    /* wait for created thread to terminate */
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    /* destroy semaphore sync */

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    sem_close(sem1);
    sem_close(sem2);
    exit(0);
    return 0;
}
