#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <bsd/stdlib.h>
// please install bsd library...

// #define to choose between sorting algorithms
#define QUICKSORT 1
#define HEAPSORT 2
#define MERGESORT 3

#define SIZE 1500  // 数组大小

int cmp(const void *a, const void *b);

int* generateRandomArray() {
    int* arr = malloc(SIZE * sizeof(int));
    int i;

    // 使用当前时间作为随机数种子
    srand(time(NULL));

    // 生成随机数组
    for (i = 0; i < SIZE; i++) {
        arr[i] = rand() % 100;  // 生成0到99之间的随机数
    }

    return arr;
}

void heapSort(int arr[], int size) {
    heapsort(arr, size, sizeof(int), cmp);
}

void mergeSort(int arr[], int size) {
    mergesort(arr, size, sizeof(int), cmp);
}
// int DArray_qsort(DArray *array, DArray_compare cmp) {
//     qsort(array->contents, DArray_count(array), sizeof(void *), cmp);
//     return 0;
// }

// int DArray_heapsort(DArray *array, DArray_compare cmp) {
//     return heapsort(array->contents, DArray_count(array), sizeof(void *), cmp);
// }

// int DArray_mergesort(DArray *array, DArray_compare cmp) {
//     return mergesort(array->contents, DArray_count(array), sizeof(void *), cmp);
// }



int cmp(const void *a, const void *b) {
  return *(int*)a - *(int*)b; 
}

// FIXME:xiaojiao, comparation function failed...
// int cmp(char **a, char **b) {
//     return strcmp(*a, *b);
// }

int main(int argc, char *argv[]) {

    // complie like this
    // gcc sort_original.c -o sort_original -lbsd
    int size = 0;
    if (argc > 1) {
        size = atoi(argv[1]); // 将字符串转换为整数
        printf("Array size: %d\n", size);
    } else {
        printf("Array size: %d\n", SIZE);
    }

    int *arr = generateRandomArray();
    int choice = QUICKSORT;

    clock_t start, end;
    double cpu_time_used;

    switch (choice) {
        case QUICKSORT:
            start = clock();
            qsort(arr, 0, size - 1, cmp);
            end = clock();
            printf("Sorted array using Quick Sort:\n");
            cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC;;
            printf(" Time spends %f s\n", cpu_time_used);
            // break;
        case HEAPSORT:
            start = clock();
            heapSort(arr, size);
            // heapsort(arr, size - 1, sizeof(int), cmp);
            end = clock();
            printf("Sorted array using Heap Sort:\n");
            cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC;;
            printf(" Time spends %f s\n", cpu_time_used);
            // break;
        case MERGESORT:
            start = clock();
            mergeSort(arr, size - 1);
            end = clock();
            printf("Sorted array using Merge Sort:\n");
            cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC;;
            printf(" Time spends %f s\n", cpu_time_used);
            break;
        default:
            printf("Invalid choice.\n");
            // return 0;
    }

    free(arr);
    
    return 0;
}