#include <stdio.h>
#include <string.h>
#include "dbg.h"
#include <time.h>
#include <assert.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#define LAYDUFF(x,y)\
    case ((0 ## x ## y) + 1): *to ++ = *from ++

#define SEVEN_AT_ONCE(x) \
    LAYDUFF(x, 6); \
    LAYDUFF(x, 5); \
    LAYDUFF(x, 4); \
    LAYDUFF(x, 3); \
    LAYDUFF(x, 2); \
    LAYDUFF(x, 1); \
    LAYDUFF(x, 0);

#define EIGHT_AT_ONCE(x)    \
    LAYDUFF(x, 7);          \
    SEVEN_AT_ONCE(x)


int frequency = 1;  

void die(const char *message) {
    if (errno) {
        perror(message);
    } else {
        printf("ERROR: %s \n", message);
    }
    exit(1);
}

int deffs_device(char *from, char *to, int count) {
    {
        int n = (count + 31) / 32;

        switch(count % 32) {
            case 0: do {
                *to ++ = *from ++;
                SEVEN_AT_ONCE(3);
                EIGHT_AT_ONCE(2);
                EIGHT_AT_ONCE(1);
                EIGHT_AT_ONCE(0);
            } while(--n > 0);
        }
    }

    return count;
}



int main(int argc, char *argv[]) {
    char from[10] = {'a'};
    char to[10] = {'c'};
    frequency = 10;
    // setup the from to have some stuff
    memset(from, 'x', 10);

    // set it to a failure mode
    memset(to, 'y', 10);

    // reset
    memset(to, 'y', 10);

    // Using macro for copy operation
    deffs_device(from, to, 10);
    printf("Copied string: %s\n", to);

    return 0;
}