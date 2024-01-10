Learn C The Hard Way
=======

Exercise 37
----

Hashmaps



The Plan
====

Implement a Hashmap in C.
In Python these are called Dictionaries.


Hashmaps Visually
====

Hashmaps are very intuitive once you know how a DArray works.
It's all about the hashing function used.



Code Review
====

Conducting a review of Hashmap by following the test.



Improving It
====

* You can use a sort on each bucket so that they're always sorted. This increases your insert time but decreases your find time, because you can then use a binary search to find each node.  Right now,  it's looping through all of the nodes in a bucket just to find one.
```C
// /ex37/liblcthw/src/lcthw/hashmap.c
int Hashmap_set(Hashmap *map, void *key, void *data) {

    uint32_t hash = 0;
    DArray *bucket = Hashmap_find_bucket(map, key, 1, &hash);
    check(bucket, "Error can't create bucket.");

    HashmapNode *node = Hashmap_node_create(hash, key, data);
    check_mem(node);

    // TODO:xiaojiao, 1. sort DArray
    // 2. 
    DArray_push(bucket, node);
    DArray_heapsort(bucket, node_compare);

    return 0;

error:
    return -1;
}
```
* You can dynamically size the number of buckets, or let the caller specify the number for each *Hashmap* created.
```C
// /ex37/liblcthw/src/lcthw/hashmap.h
Hashmap *Hashmap_create(Hashmap_compare compare, Hashmap_hash hash, size_t num_buckets);
```
```C
// /ex37/liblcthw/src/lcthw/hashmap.c
Hashmap *Hashmap_create(Hashmap_compare compare, 
                        Hashmap_hash hash,
                        size_t num_buckets) {
    Hashmap *map = calloc(1, sizeof(Hashmap));
    check_mem(map);

    map->compare = compare == NULL ? default_compare : compare;
    map->hash = hash == NULL ? default_hash : hash;
    map->buckets = DArray_create(sizeof(DArray *), num_buckets);
    map->buckets->end = map->buckets->max;                      // fake out expanding it
    check_mem(map->buckets);

    return map;
error:
    if (map) {
        Hashmap_destroy(map);
    }

    return NULL;
}
```
* You can use a better *default_hash*.  There are tons of them.



Improving It
====

* This (and nearly every *Hashmap*) is vulnerable to someone picking keys that will fill only one bucket, and then tricking your program into processing them.  This then makes your program run slower because it changes from processing a *Hashmap* to effectively processing a single *DArray*.  If you sort the nodes in the bucket, this helps, but you can also use better hashing functions, and for the really paranoid programmer, add a random salt so that keys can't be predicted.



Improving It
====

* You could have it delete buckets that are empty of nodes to save space, or put empty buckets into a cache so you can save on time lost creating and destroying them.
* Right now, it just adds elements even if they already exist.  Write an alternative set method that only adds an element if it isn't set already.



Extra Credit
====

* Research the *Hashmap* implementation in your favorite programming language to see what features it has.
* Find out what the major disadvantages of a *Hashmap* are and how to avoid them.  For example, it doesn't preserve order without special changes, nor does it work when you need to find things based on parts of keys.
```
Here are the main disadvantages of hashmaps and ways to mitigate them in English:

1. High memory usage

Each key-value pair in a hashmap requires extra memory to store the hash value and next/bucket pointers. This imposes high memory demands. 

Ways to avoid:

- Consider more efficient data structures like balanced binary search trees when there are many key-value pairs.

2. High cost of resizing 

When the number of elements in a hashmap exceeds the current capacity, the hash table positions need to be recalculated, incurring additional overhead.

Ways to avoid: 

- Use constructor with estimated size to avoid multiple resizing operations.

- Use other data structures like balanced trees that have lower complexity during resizing.

3. Lookup efficiency depends on hash function quality

Poor hash functions can lead to severe collisions, impacting lookup performance.

Ways to avoid:

- Use high quality hash functions like the one used in Java HashMap.

- Preprocess keys like doing modulo on numeric keys to reduce collisions when needed.

4. Traversal order changes

Hashmap has no definite traversal order as it may change due to insertion order or rehashing.

Ways to avoid:

- Use ordered data structures like trees if order is needed. 

- Hashmaps can be used if order is not important.

In summary, hashmaps are best suited for scenarios where keys are unique, insertion and deletion are frequent but order is irrelevant. Other data structures may need to be considered to reduce resizing overhead or maintain order.
```
* Write a unit test that demonstrates the defect of filling a *Hashmap* with keys that land in the same bucket, then test how this impacts performance.  A good way to do this is to just reduce the number of buckets to something stupid, like five.



End Of Lecture 37
=====

