#include "minunit.h"
#include "lcthw/list_algos.h"
#include <assert.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

char *values[] = {"XXXX", "1234", "abcd", "xjvef", "NDSS"};

#define NUM_VALUES 5
#define RUN_TIMES 10000000

typedef int (*List_compare)(const void *a, const void *b);


List *create_words() {
    int i = 0;
    List *words = List_create();

    for (i = 0; i < NUM_VALUES; i++) {
        List_push(words, values[i]);
    }

    return words;
}

int is_sorted(List *words) {
    LIST_FOREACH(words, first, next, cur) {
        if (cur->next && strcmp(cur->value, cur->next->value) > 0) {
            debug("%s %s ", (char *)cur->value, (char *)cur->next->value);
            return 0;
        }
    }

    return 1;
}

char *test_bubble_sort() {
    List *words = create_words();

    // should work on a list that needs sorting
    int rc = List_bubble_sort(words, (List_compare) strcmp);
    mu_assert(rc == 0, "Bubble sort failed.");
    mu_assert(is_sorted(words), "Words are not sorted after bubble sort.");

    // should word on an already sorted list
    rc = List_bubble_sort(words, (List_compare) strcmp);
    mu_assert(rc == 0, "Bubble sort of already sorted failed.");
    mu_assert(is_sorted(words), "Words should be sorted if empty.");

    List_destroy(words);

    // should work on an empty list
    words = List_create(words);
    rc = List_bubble_sort(words, (List_compare) strcmp);
    mu_assert(rc == 0, "Bubble failed on empty list.");
    mu_assert(is_sorted(words), "Words should be sorted if empty.");

    List_destroy(words);

    return NULL;
}

char *test_merge_sort() {
    List *words  = create_words();

    // should work on a list that needs sorting
    List *res = List_merge_sort(words, (List_compare) strcmp);
    mu_assert(is_sorted(res), "Words are not sorted after merge sort.");

    List *res2 = List_merge_sort(res, (List_compare) strcmp);
    mu_assert(is_sorted(res), "Should still be sorted after merge sort.");
    List_destroy(res2);
    List_destroy(res);

    List_destroy(words);
    return NULL;
}

char *test_performance_of_merge_sort() {
    List *words  = create_words();

    // test 1000 times;
    
    // List *res = NULL;

    // start $$ calculate time
    clock_t start = clock();
    for (int i = 0; i < RUN_TIMES; i++) {
        List_merge_sort(words, (List_compare) strcmp);
    }
    clock_t end = clock();

    // time spends
    double tim_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("\nMerge Sort Time: %f seconds \n", tim_used);

    List_destroy(words);
    return NULL;
}


char *test_performance_of_bubble_sort() {
    List *words  = create_words();

    // test 1000 times;
    
    // List *res = NULL;

    // start $$ calculate time
    clock_t start = clock();
    for (int i = 0; i < RUN_TIMES; i++) {
        List_bubble_sort(words, (List_compare) strcmp);
    }
    clock_t end = clock();

    // time spends
    double tim_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("\nbubble_sort Time: %f seconds \n", tim_used);

    List_destroy(words);
    return NULL;
}

char *generate_random_string(int length) {
    char *random_string = malloc((length + 1) * sizeof(char));
    srand(time(NULL));

    const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int charset_length = sizeof(charset) - 1;

    for (int i = 0; i < length; i++) {
        int random_index = rand() % charset_length;
        random_string[i] = charset[random_index];
    }

    random_string[length] = '\0';
    return random_string;
}


List *create_list_by_specific_words(int word_length, int list_length) {
    List *words = List_create();

    // added into list
    for (int j = 0; j < list_length; j++) {
        char *value = generate_random_string(word_length);
        List_push(words, value);
    }
    return words;    
}

void *create_different_size_of_bubble_sort(int list_length) {
    List *words = create_list_by_specific_words(3, list_length);

    // start $$ calculate time
    clock_t start = clock();
    for (int i = 0; i < RUN_TIMES; i++) {
        List_bubble_sort(words, (List_compare) strcmp);
    }
    clock_t end = clock();

    // time spends
    double tim_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("\nbubble_sort Time: %f seconds \n", tim_used);

    List_destroy(words);

    return NULL;
}

void *create_different_size_of_merge_sort(int list_length) {
    List *words = create_list_by_specific_words(3, list_length);

    // start $$ calculate time
    clock_t start = clock();
    for (int i = 0; i < RUN_TIMES; i++) {
        List_merge_sort(words, (List_compare) strcmp);
    }
    clock_t end = clock();

    // time spends
    double tim_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("\nmerge_sort Time: %f seconds \n", tim_used);

    List_destroy(words);

    return NULL;
}

char *test_different_size_of_bubble_sort() {
    for (int i = 0; i < RUN_TIMES; i++) {
        create_different_size_of_bubble_sort(i);
    }
    return NULL;
}

char *test_different_size_of_merge_sort() {
    for (int i = 0; i < RUN_TIMES; i++) {
        create_different_size_of_merge_sort(i);
    }
    return NULL;
}

char *test_list_insert_sorted() {
    List *words  = create_words();

    // should work on a list that needs sorting

    List *res = List_merge_sort(words, (List_compare) strcmp);
    mu_assert(is_sorted(res), "Should still be sorted after merge sort.");
    mu_assert(List_count(res) == 5, "Wrong count after spliting list.");
    List *res2 = List_insert_sorted(res, "2233", (List_compare) strcmp);
    
    mu_assert(is_sorted(res2), "Should still be sorted after inserted value.");
	mu_assert(List_count(res) == 5, "Wrong count after insert list on source.");
    mu_assert(List_count(res2) == 6, "Wrong count after insert list.");
    List_destroy(res);

    List_destroy(words);
    return NULL;

}

char *all_tests() {
    mu_suite_start();

    // mu_run_test(test_bubble_sort);
    // mu_run_test(test_merge_sort);
    // mu_run_test(test_performance_of_merge_sort);
    // mu_run_test(test_performance_of_bubble_sort);

    // mu_run_test(test_different_size_of_merge_sort);
    // test_list_insert_sorted
    mu_run_test(test_list_insert_sorted);
    return NULL;
}

RUN_TESTS(all_tests);



