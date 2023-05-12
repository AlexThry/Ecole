//
// Created by Alexis Thierry on 12/05/2023.
//
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#include <ctype.h>

#define THREAD_NUM 2
#define SIZE_TAMPON 5

sem_t *sem_consumer;
sem_t *sem_producer;

volatile char buffer[SIZE_TAMPON];

char str = 'a';

/*
 * Fonction producteur  :
 * - Produit un caractère
 * - Le met dans le buffer
 * - Passe le sémaphore du consommateur
 * - Passe le sémaphore du producteur
 */
_Noreturn void * producer(void *args) {
    int iP = 0;
    while (1) {
        // Produit un caractère
        sem_wait(sem_producer);
        buffer[iP] = str;
        sem_post(sem_consumer);
        printf("Production à l'index %d : %c\n ", iP, str);


        str ++;
        iP ++;
        // Si on est à la case 5 -> on revient à la case 0
        if (iP == SIZE_TAMPON) {
            iP = 0;
        }
    }
}

/*
 * Fonction consommateur :
 * - Consomme un caractère
 * - Met le caractère en majuscule
 * - Passe le sémaphore du producteur
 * - Passe le sémaphore du consommateur
 * - Affiche le caractère consommé
 * - Attend 1 seconde
 */
_Noreturn void * consumer(void *args) {
    int iC = 0;
    while (1) {

        char c;
        // Consomme
        sem_wait(sem_consumer);
        c = buffer[iC];
        // Met le caractère en majuscule
        char maj_str = toupper(c);
        sem_post(sem_producer);

        printf("Consommation à l'index %d : %c\n ", iC, maj_str);

        iC ++;
        // Si on est à la case 5 -> on revient à la case 0
        if (iC == SIZE_TAMPON) {
            iC = 0;
        }

        sleep(1);

    }
}

int main(int argc, char* argv[]) {

    srand(time(NULL));
    pthread_t thread1, thread2;

    // initialisation des sémaphores
    sem_producer = sem_open("sem_producer", O_CREAT, 0644, 10);
    sem_consumer = sem_open("sem_consumer", O_CREAT, 0644, 0);

    // création des threads
    pthread_create(&thread1, NULL, &producer, NULL);
    pthread_create(&thread2, NULL, &consumer, NULL);

    // attente de la fin des threads
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    // destruction des sémaphores
    sem_close(sem_producer);
    sem_close(sem_consumer);



    return 0;
}

