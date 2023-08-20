Learn C The Hard Way
=======

Exercise 34
----

Dynamic Array



The Plan
====

Learn about dynamic arrays, a very useful datastructure.



Code Review
====

Starting with the header file to implement, then the test, then the implementation.



The Analysis
====



DArray Advantages
====

* Iteration:  You can just use a basic for-loop and ``DArray_count`` with ``DArray_get``, and you're done.  No special macros needed, and it's faster because you aren't walking through pointers.
* Indexing:  You can use ``DArray_get`` and ``DArray_set`` to access any element at random, but with a ``List`` you have to go
  through N elements to get to N+1.
* Destroying:  You can just free the struct and the ``contents`` in two operations.  A ``List`` requires a series of ``free`` calls
  and walking every element.



DArray Advantages
=====

* Cloning: You can also clone it in just two operations (plus whatever it's storing) by copying the struct and ``contents``.  A list again requires walking through the whole thing and copying every ``ListNode``
  plus its value.
* Sorting: As you saw, ``List`` is horrible if you need to keep the data sorted.  A ``DArray`` opens up a whole class of great sorting algorithms, because now you can access elements randomly.
* Large Data: If you need to keep around a lot of data, then a ``DArray`` wins since its base, ``contents``, takes up less memory than the same number of ``ListNode`` structs.



DArray Disadvantages
====

* Insert and remove on the front (what I called shift).  A ``DArray`` needs special treatment to be able to do this efficiently, and usually it has to do some copying.
* Splitting or joining:  A ``List`` can just copy some pointers and it's done, but with a ``DArray``, you have copy all of the
  arrays involved.



DArray Disadvantages
====

* Small Data. If you only need to store a few elements, then typically the storage will be less in a ``List`` than a generic ``DArray``. This is because the ``DArray`` needs to expand the backing store to accommodate future inserts, while a ``List`` only makes what it needs.



Breaking It
====

* Forget to check the return value from malloc and then use the buffer.
* Getting the end and start count of the buffer wrong.  Easy to do an off-by-one here.
* Exploit the insert and delete costs to cause a denial of service.



Extra Credit
====

* Improve the unit tests to cover more of the operations, and test them using a for-loop to ensure that they work.
```C

// darray_tests.c, added by xiaojiao 2023/08/20
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
```

* Research what it would take to implement bubble sort and merge sort for DArray, but don't do it yet.  I'll be implementing DArray algorithms next, so you'll do this then.
```
Sure! I can provide you with an overview of how you can implement bubble sort and merge sort algorithms for the `DArray` data structure. Here's a brief explanation of each algorithm:

1. Bubble Sort:

   - Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
   - To implement bubble sort for `DArray`, you would need a loop that iterates through the array and compares adjacent elements. If they are out of order, you would swap them.
   - The loop continues until the array is sorted, which can be determined by keeping track of whether any swaps were made in the previous iteration.

1. Merge Sort:

   - Merge sort is a divide-and-conquer algorithm that recursively divides the array into two halves, sorts them independently, and then merges the sorted halves to produce a sorted array.
   - To implement merge sort for `DArray`, you would need to define a recursive function that takes the array and its boundaries as input. The function would divide the array into two halves and recursively call itself on each half.
   - The base case of the recursion would be when the array has only one element or is empty, in which case it is already considered sorted.
   - After sorting the two halves, the function would merge them by comparing elements and placing them in the correct order in a temporary array. Finally, the contents of the temporary array would be copied back to the original array.

When you're ready to implement these algorithms for the `DArray` data structure, feel free to ask, and I'll be happy to assist you with the code implementation.
```


Extra Credit
====

* Write some performance tests for common operations and compare them to the same operations in ``List``.  You did some of this already, but this time, write a unit test that repeatedly does the operation in question, and then in the main runner, do the timing.

```C
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
```


Extra Credit
====

* Look at how the ``DArray_expand`` is implemented using a constant increase (size + 300). Typically, dynamic arrays are implemented with a multiplicative increase (size * 2), but I've found this to cost needless memory for no real performance gain.  Test my assertion and see when you'd want a multiplicative increase instead of a constant increase.

```C
// learn_C_the_hard_way/ex34/liblcthw/src/lcthw/darray.h
int DArray_expand_with_double_increasement(DArray *array);
```

```C
// learn_C_the_hard_way/ex34/liblcthw/src/lcthw/darray.c
int DArray_expand_with_double_increasement(DArray *array) {
    size_t old_max = array->max;
    check(DArray_resize(array, array->max * 2) == 0,
            "Failed to expand array to new size: %d",
            array->max + (int)array->expand_rate);

    memset(array->contents + old_max, 0, array->expand_rate + 1);
    return 0;

error:
    return -1;
}
```

```C
// learn_C_the_hard_way/ex34/liblcthw/src/lcthw/darray.c
int DArray_expand_with_double_increasement(DArray *array) {
    size_t old_max = array->max;
    check(DArray_resize(array, array->max * 2) == 0,
            "Failed to expand array to new size: %d",
            array->max + (int)array->expand_rate);

    memset(array->contents + old_max, 0, array->expand_rate + 1);
    return 0;

error:
    return -1;
}
```

```C
// learn_C_the_hard_way/ex34/liblcthw/tests/darray_tests.c
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
```
End Of Lecture 34
=====

