#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int arrlen;
    int *array;
    int i;
    printf("please enter length:");
    scanf("%d", &arrlen);

    array = (int *)malloc(arrlen * sizeof(int));
    if (!array) {
        printf("create error!\n");
        exit(1);
    }
    for (i = 0; i < arrlen; i++) {
        array[i] = i + 1;
    }

    for (i = 0; i < arrlen; i++) {
        printf("%d ", array[i]);
    }

    printf("\n");
    free(array);
    return 0;
}


// source from https://zhuanlan.zhihu.com/p/368983422