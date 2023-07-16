#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// class 4

#define MAX_SIZE 10

int main(int argc, char *argv[]){

    // n less than 10, while m less than 10000
    int n, m, num;
    int sum[20005] = {0};
    // int numbers[MAX_SIZE];
    // m greater than 0, m also
    printf("the first character less than 10, while m less than 10000\n");
    scanf("%d %d", &n, &m);
    n = n % 10;
    m = m % 10000;

    printf("please input number , which less than %d\n", n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &num);
        for (int j = num; j <= m; j += num) {
            sum[j] = 1;
        }
    }

    for (int k = 1; k <= m; k ++) {
        if (sum[k] == 1) continue;
        printf("%d\t", k);
    }
    printf("\n");

    return 0;
}


