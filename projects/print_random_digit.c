#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// class 3


int main(int argc, char *argv[]){
    // printf("%d\n", rand() % 1000);
    srand(time(0));
    // printf("%d\n", rand() % 1000);
    for (int i = 1; i <= 100; i++) {
        // srand(time(0));
        printf("%d\t", rand() % 100);
        if (i % 10 == 0) {
            printf("\n");
        }
    }
    return 0;
}