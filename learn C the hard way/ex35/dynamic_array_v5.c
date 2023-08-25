#include <stdio.h>
#include <stdlib.h>

#define DEFAULT_CAPACITY 100

typedef struct Dynamic_array {
    int arrlen;
    int index;
    void **content;
    int capacity;
} Darray;


Darray *Darray_create(int arrlen) {
    Darray *darray = malloc(sizeof(Darray));

    darray->arrlen = arrlen;
    // start from 0
    darray->index = 0;
    darray->content = malloc(darray->arrlen * sizeof(void *));
    darray->capacity = DEFAULT_CAPACITY;
    return darray;
}

// don't limit the type of element
void *Darray_push(Darray * darray, void *element) {
    if (darray == NULL) {
        printf("array is NULL\n");
        return NULL;
    }

    if ((darray->index < darray->arrlen) && (darray->arrlen <= darray->capacity)) {
       darray->content[darray->index] = element;
       darray->index ++;
    } else {
        printf("overflow...\n");
        exit(1);
    }
    // darray->index ++;
    return NULL;
}

void *Darray_pop(Darray * darray) {
    if (darray == NULL) {
        printf("array is NULL\n");
        return NULL;
    }

    if (darray->index <= darray->arrlen) {
       darray->content[darray->index] = NULL;
       darray->index -= 1;
    } else {
        printf("overflow pop...\n");
        exit(1);
    }
    // darray->index ++;
    return NULL;
}

void *Darray_clear(Darray * darray) {
    if (darray == NULL) {
        printf("array is NULL\n");
        return NULL;
    }

    for (int i = 0; i < darray->index; i --) {
        Darray_pop(darray);
    }

    return NULL;
}

int Darray_repalce_element(Darray *darray, int index, void *element){
    if (darray == NULL) {
        printf("array is NULL\n");
        return 0;
    }
    
    if (index < 0) {
        printf("index starts from 0...\n");
    }

    if (index <= darray->index) {
        darray->content[index] = element;
        return 0; 
    }

    // else error
    return 1;
}

void *Darray_destroy(Darray *darray) {
    // Darray_clear(darray);
    
    // free memory
    free(darray->content);
    free(darray);

    return NULL;
}

int *Darray_resize(Darray *darray, int arrlen) {
    // darray->capacity = darray->capacity + DEFAULT_CAPACITY;
    // darray->arrlen = darray->arrlen + darray->arrlen;

    // re alloc memeory
    if (darray == NULL) {
        return 1;
    }
    void *content = realloc(darray->content, arrlen * sizeof(void *));
    if (content == NULL) {
        printf("realloc memeory failed.\n");
        free(darray->content);
        free(darray);
    }
    
    // darray->content = content;
    if (array < darray->capacity) {
        darray->arrlen = arrlen;
        return 0;
    } else {
        printf("more work on the way...\n");
        exit(1);
    }
    // darray->capacity = arrlen;
    return 1;
}

int main(int argc, char *argv[]) {
    int i, arrlen;

    printf("please enter length: ");
    scanf("%d", &(arrlen));

    Darray *darray =  Darray_create(arrlen);

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
        Darray_push(darray, i + 1);
    }

    Darray_pop(darray);
    Darray_push(darray, 13);
    int rc = Darray_repalce_element(darray, 3, 2);
    if (rc == 0) {
        printf("create succesfully.\n");
    } else {
        printf("replacement low down\n");
    }

    for (i = 0; i < darray->index; i++) {
        printf("%d ", darray->content[i]);
    }

    Darray_resize(darray, 20);
    printf("darray size %d", darray->arrlen);
    printf("\n");
    // Darray_destroy(darray);

    return 0;
}

