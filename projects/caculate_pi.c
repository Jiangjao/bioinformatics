#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// class 3


int main(int argc, char *argv[]){
    int n = 0, m = 0;
    for (int i = 0; i < 10000000; i++) {
        double x = 1.0 * rand() / RAND_MAX;
        double y = 1.0 * rand() / RAND_MAX;
        if (x * x + y * y <= 1.0){
            m += 1;
        }
        n += 1;
    }

    printf("%lf\n", 4.0 * m / n);
    return 0;
}


