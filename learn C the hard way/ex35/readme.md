Learn C The Hard Way
=======

Exercise 35
----

Sorting and Searching



The Plan
====

* Make a simple DArray sorting library using existing functions.
* Implement a new structure and algorithm called a "Radix Map".
* Create a binary search algorithm for the RadixMap.



The DArray Code
====

Continuing the code review method with a part of DArray.



The RadixMap Code
====

Code review this code next.



The Binary Search Code
====

Finally, code review of the BSTree code.



Improving It
====

* Use a binary search to find the minimum position for the new element, then only sort from there to the end.  You find the
minimum, put the new element on the end, and then just sort from the minimum on.   This will cut your sort space down considerably most of the time.
```C
// ex35/liblcthw/src/lcthw/radixmap.c
void RadixMap_sort_with_index(RadixMap *map, int index) {
    uint64_t *source = &map->contents[index].raw;
    uint64_t *temp = &map->temp[index].raw;
    radix_sort(0, map->end, source, temp);
    radix_sort(1, map->end, temp, source);
    radix_sort(2, map->end, source, temp);
    radix_sort(3, map->end, temp, source);
}


// https://github.com/hysonger/liblcthw/blob/master/src/lcthw/radixmap.c
int RadixMap_add(RadixMap *map, uint32_t key, uint32_t value) {
    check(key < UINT32_MAX, "Key can't be equal to UINT32_MAX");

    RMElement element = {.data = {.key = key, .value = value} };
    check(map->end + 1 < map->max, "RadixMap is full.");

    // 1. Use a binary search to find the minimum position for the new element
    // 2. sort from the position

    // 2.1 find the index 
    int insert_index  = binary_search(map, value);

    printf("%d value max digit\n", get_max_bit_uint8(value));
    // 2.2 the largest index
    // added by xiaojiao, 2023/10/11
    if (insert_index > map->end) {
        // no sort
        map->contents[map->end++] = element;
    } else {
        map->contents[map->end++] = element;
        RadixMap_sort_with_index(map, insert_index);
        RadixMap_sort(map); 

    }

    // map->contents[map->end++] = element;

    // RadixMap_sort(map);

    return 0;

error:
    return -1;
}
```
* Keep track of the biggest key currently being used, and then only sort enough digits to handle that key.  You can also keep track of the smallest number, and then only sort the digits necessary for the range.  To do this, you'll have to start caring about CPU integer ordering (endianness).
```C
// https://github.com/hysonger/liblcthw/blob/master/src/lcthw/radixmap.c
// maybe this works, xiaojiao

void RadixMap_sort_with_bit(RadixMap *map, int byte) {
    if (byte < 1) return;
    uint64_t *source = &map->contents[0].raw;
    uint64_t *temp = &map->temp[0].raw;

    if (byte > 1) {
        radix_sort(byte - 1, map->end, source, temp);
        radix_sort(byte, map->end, temp, source);
        // radix_sort(2, map->end, source, temp);
        // radix_sort(3, map->end, temp, source);
    }
    RadixMap_sort_with_bit(map, byte - 1);
}
```


Extra Credit
====

* Implement quicksort, heapsort, and merge sort and then provide a *#define*  that lets you pick between the two, or create a second set of functions you can call.  Use the technique I taught you to read the Wikipedia page for the algorithm, and then implement it with the psuedo-code.

>[source code sorting](sorting.c)

* Compare the performance of your optimizations to the original implementations.

>[bench_performance.sh](liblcthw/src/lcthw/bench_performance.sh)


Extra Credit
====

* Use these sorting functions to create a *DArray_sort_add* that adds elements to the *DArray* but sorts the array after.
* Write a *DArray_find* that uses the binary search algorithm from  *RadixMap_find* and the *DArray_compare* to find elements in a sorted *DArray*.




End Of Lecture 35
=====

