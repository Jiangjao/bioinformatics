#include <stdio.h>
#include <stdlib.h>

typedef struct Dynamic_array {
    int arrlen;
    int start;
    void **content;
} Darray;



int main(int argc, char *argv[]) {
    int arrlen;
    int *array;
    int i;
    Darray *darray = malloc(sizeof(Darray));

    printf("please enter length: ");
    scanf("%d", &(darray->arrlen));

    darray->content = malloc(darray->arrlen * sizeof(int));
    if (!darray) {
        printf("create error!\n");
        exit(1);
    }

    if (darray->content == NULL) {
        printf("Memory allocation failed.\n");
        free(darray);
        exit(1);
    }
    for (i = 0; i < darray->arrlen; i++) {
        // darray[i] = i + 1;
        darray->content[i] = i + 1;
    }

    for (i = 0; i < darray->arrlen; i++) {
        printf("%d ", darray->content[i]);
    }

    printf("\n");
    // free(darray->content);
    // free(darray);
    return 0;
}

