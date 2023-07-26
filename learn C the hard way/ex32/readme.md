Learn C The Hard Way
=======

Exercise 32
----

Double Linked Lists



The Plan
====

Learn about your very first data structure:

Double Linked Lists
----



Creating A liblcthw Project
====

We'll need a project for the rest of the book called *liblcthw*.



Algorithms and Data Structures
====

A big step in going from amateur to professional is learning
about data structures and algorithms.

A double linked list is the easiest one.



Double Linked Lists Visually
====

I'll quickly draw some diagrams to show you how they work.



Automated Testing Demo
====

You can enter the code just fine, but watch me write
the test.



Code Reviews
====

Later videos will demonstrate how to code review to make code solid.



Improving It
====

* You can make ``List_clear_destroy`` more efficient by using
  ``LIST_FOREACH`` and doing both ``free`` calls inside one
  loop.
* You can add asserts for preconditions so that the program isn't given a ``NULL``
  value for the ``List *list`` parameters.



Improving It
====

* You can add invariants that check that the list's contents are always correct,
  such as ``count`` is never ``< 0``, and if ``count > 0``, then ``first`` isn't NULL.
* You can add documentation to the header file in the form of comments before
  each struct, function, and macro that describes what it does.



Extra Credit
====

* Research doubly vs. singly linked lists and when one is preferred over the other.

the differences and pros and cons between singly linked lists and doubly linked lists. 😊

Singly linked lists and doubly linked lists are both linear data structures used to store a series of elements. The main difference between them is that each node in a doubly linked list has two pointers, one pointing to the previous node and one pointing to the next node, while each node in a singly linked list only has one pointer, pointing to the next node.

Both singly linked lists and doubly linked lists have their own advantages and disadvantages that are suitable for different situations. Here are some comparisons:

- Doubly linked lists can be traversed from both directions, while singly linked lists can only be traversed from one direction. This means that doubly linked lists can more easily implement some operations, such as reversing, inserting, and deleting.
- Doubly linked lists require more space to store extra pointers, while singly linked lists only need to store one pointer. This means that doubly linked lists will occupy more memory, while singly linked lists will save memory.
- Modifying a doubly linked list requires updating two pointers, while modifying a singly linked list only requires updating one pointer. This means that modifying a doubly linked list will be more complex, while modifying a singly linked list will be simpler.

Overall, both singly linked lists and doubly linked lists have their own advantages and disadvantages, and there is no absolute good or bad. When choosing which data structure to use, it is necessary to weigh and judge based on specific needs and scenarios.

-   Sources:
  1. [Difference between Singly linked list and Doubly linked list ↗](https://www.geeksforgeeks.org/difference-between-singly-linked-list-and-doubly-linked-list/)
  2. [What is the difference between singly and doubly linked lists? ↗](https://www.quora.com/What-is-the-difference-between-singly-and-doubly-linked-lists)

* Research the limitations of a doubly linked list.  For example, while they are efficient for inserting and deleting elements, they are very slow for iterating over them all.l

```
- A doubly linked list is a data structure that allows for efficient insertion and deletion of elements in O(1) time complexity. However, there are limitations to using a doubly linked list, including:

- Slow iteration: Unlike arrays, doubly linked lists do not provide constant time access to their elements. Accessing an element in a doubly linked list requires traversing the list from the beginning or end, which results in a time complexity of O(n), where n is the length of the list. This makes iterating over a doubly linked list slower than iterating over an array.

- Memory overhead: Doubly linked lists require extra memory to store the pointers to the previous and next nodes, which can lead to memory overhead and cache unfriendliness. This is in contrast to arrays, which only require memory to store the elements themselves.

- No constant-time access: As mentioned, accessing an element in a doubly linked list requires traversing the list. Therefore, it does not support constant-time access to elements based on their index, unlike arrays.
```
* What operations are missing that you can imagine needing?  Some examples are copying, joining, and splitting.  Implement these operations and write the unit tests for them.

```C
// copy
List *List_copy(List *list) {
        check(list != NULL, "Invalid list.");
        List *list_dubp = List_create();
        list_dubp->first = list->first;

        LIST_FOREACH(list, first, next, cur) {
                List_push(list_dubp, cur->value);
    }
        return list_dubp;
error:
        return NULL;
}

// joining return new list
List *List_cat(List *list1, List *list2) {
        check(list1 != NULL, "Invalid list.");
        check(list2 != NULL, "Invalid list.");

        List *list_dubp = List_copy(list1);

        LIST_FOREACH(list2, first, next, cur) {
                List_push(list_dubp, cur->value);
        }



        return list_dubp;
error:
        return NULL;
}

// splitting
```


End Of Lecture 32
=====

