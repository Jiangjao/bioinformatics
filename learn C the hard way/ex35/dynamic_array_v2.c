#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int arrlen;
    int *array;
    int *arrayCopy;     // point to the element
    int i;
    printf("please enter length: ");
    scanf("%d", &arrlen);

    arrayCopy = array = (int *)malloc(arrlen * sizeof(int));
    if (!array) {
        printf("create error! \n");
        exit(1);
    }

    for (i = 0; i < arrlen; i++) {
        *arrayCopy ++ = i + 1;
    }
    arrayCopy = array;      // move to the first address of array
    for (i = 0; i < arrlen; i++) {
        printf("%d ", *arrayCopy++);
    }

    printf("\n");
    free(array);
    return 0;
}


