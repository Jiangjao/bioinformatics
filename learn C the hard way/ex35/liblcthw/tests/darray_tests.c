#include <time.h>
#include "minunit.h"
#include "lcthw/darray.h"

#define RUN_TIMES 3000

static DArray *array = NULL;
static int *val1 = NULL;
static int *val2 = NULL;

char *test_create() {
    array = DArray_create(sizeof(int), 100);
    mu_assert(array != NULL, "DArray_create failed.");
    mu_assert(array->contents != NULL, "contents are wrong in darray.");
    mu_assert(array->end == 0, "end isn't at the right spot.");
    mu_assert(array->element_size == sizeof(int), "element size is wrong");
    mu_assert(array->max == 100, "wrong max length on initial size");

    return NULL;
}

char *test_destroy() {
    DArray_destroy(array);

    return NULL;
}

char *test_new() {
    val1 = DArray_new(array);
    mu_assert(val1 != NULL, "failed to make a new element");

    val2 = DArray_new(array);
    mu_assert(val2 != NULL, "failed to make a new element");

    return NULL;
}

char *test_set() {
    DArray_set(array, 0, val1);
    DArray_set(array, 1, val2);

    return NULL;
}

char *test_get() {
    mu_assert(DArray_get(array, 0) == val1, "Wrong first value");
    mu_assert(DArray_get(array, 1) == val2, "Wrong second value");

    return NULL;
}

char *test_remove() {
    int *val_check = DArray_remove(array, 0);
    mu_assert(val_check != NULL, "Should not get NULL.");
    mu_assert(*val_check == *val1, "Should get the first value.");
    mu_assert(DArray_get(array, 0) == NULL, "Should be gone");
    DArray_free(val_check);

    val_check = DArray_remove(array, 1);
    mu_assert(val_check != NULL, "Should not get NULL.");
    mu_assert(*val_check == *val2, "Should get the first value");
    mu_assert(DArray_get(array, 1) == NULL, "Should be gone");
    DArray_free(val_check);

    return NULL;
}

char *test_expand_contract() {
    int old_max = array->max;
    DArray_expand(array);
    mu_assert((unsigned int)array->max == old_max + array->expand_rate, "wrong size after expand.");

    DArray_contract(array);
    mu_assert((unsigned int)array->max == array->expand_rate + 1, "Should stay at the expand_rate at least.");

    DArray_contract(array);
    mu_assert((unsigned int)array->max == array->expand_rate + 1, "Should stat at the expand_rate at least.");

    return NULL;
}

char *test_push_pop() {
    int i = 0;
    for(i = 0; i < 1000; i++) {
        int *val = DArray_new(array);
        *val = i * 333;
        DArray_push(array, val);
    }

    mu_assert(array->max == 1201, "Wrong max size.");

    for (i = 999; i >= 0; i--) {
        int *val = DArray_pop(array);
        mu_assert(val != NULL, "Shouldn't get a NULL");
        mu_assert(*val == i * 333, "Wrong value.");
        DArray_free(val);
    }

    return NULL;
}

char *test_element_get() {
    int i = 0;
    for(i = 0; i < 1000; i++) {
        int *val = DArray_new(array);
        *val = i * 333;
        DArray_push(array, val);
    }
    printf(" %d value :\n", i);
    // printf(" %p val is \n", val);
    // mu_assert(array->max == 1201, "Wrong max size.");
    mu_assert(DArray_first(array) == DArray_get(array, 0), "Wrong first element value.")
    mu_assert(DArray_last(array) == DArray_get(array, 1000), "Wrong last element value.")

    for (i = 999; i >= 0; i--) {
        int *val = DArray_pop(array);
        mu_assert(val != NULL, "Shouldn't get a NULL");
        mu_assert(*val == i * 333, "Wrong value.");
        DArray_free(val);
    }

    mu_assert(DArray_count(array) == array->end, "Wrong end.")


    return NULL;
}

void *generate_DArray_with_size(int size) {
    int i = 0;
    for(i = 0; i < size; i++) {
        int *val = DArray_new(array);
        *val = i * 333;
        DArray_push(array, val);
    }


    for (i = size; i >= 0; i--) {
        int *val = DArray_pop(array);
        DArray_free(val);
    }

    return NULL;
}

char *test_performance_of_push_pop_with_different_size_Drray() {

    clock_t start = clock();
    for (int i = 0; i < RUN_TIMES; i++) {
        generate_DArray_with_size(i);
    }
    clock_t end = clock();

    // time spends
    double tim_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("\npush_pop Time: %f seconds \n", tim_used);

    return NULL;
}

char *test_expand_contract_with_double_increasement() {
    int old_max = array->max;
    DArray_expand_with_double_increasement(array);
    mu_assert((unsigned int)array->max == old_max * 2, "wrong size after expand.");

    DArray_contract(array);
    mu_assert((unsigned int)array->max == array->expand_rate + 1, "Should stay at the expand_rate at least.");

    DArray_contract(array);
    mu_assert((unsigned int)array->max == array->expand_rate + 1, "Should stat at the expand_rate at least.");

    return NULL;
}

char *all_tests() {
    mu_suite_start();

    mu_run_test(test_create);
    mu_run_test(test_new);
    mu_run_test(test_set);
    mu_run_test(test_get);
    mu_run_test(test_remove);
    mu_run_test(test_expand_contract);
    mu_run_test(test_push_pop);
    mu_run_test(test_element_get);
    // mu_run_test(test_performance_of_push_pop_with_different_size_Drray);
    mu_run_test(test_expand_contract_with_double_increasement);
    mu_run_test(test_destroy);

    return NULL;
}

RUN_TESTS(all_tests);
