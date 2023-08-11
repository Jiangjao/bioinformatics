Learn C The Hard Way
=======

Exercise 33
----

Linked List Algorithms



The Plan
====

Learn two sorting algorithms for double linked lists.

Watch how to conduct a simple code review.



The Code
====

You should be able to create this and figure out how it works.

I will assume you've done that, and now to code review.



Bubble Sort
====

Code review of bubble sort.

Start with the unit test and move from there.



Merge Sort
====

Code review of merge sort.



Improving It
====

* The merge sort does a crazy amount of copying and creating lists, so find ways to reduce this.

Reduce memory allocation and release: every recursive call to List_ Merge_ When using the sort function, both left and right new lists are created and destroyed after the sorting is completed. Such frequent memory allocation and release can bring certain overhead. You can consider using pointers and indexes instead of creating a new list and directly manipulating the original array during the merge process.

Optimize the merge process: In the current merge process, you have used List_ Shift function to extract elements from the left and right lists, and then use List_ The push function adds elements to the result list. This operation involves frequent element movement and memory allocation. You can consider using pointers and indexes to directly access elements in the list and place them directly in the result list, avoiding additional copying operations.

Consider performance optimization: List was used during the iteration process_ The count function is used to determine whether the list is empty, which results in each iteration having to traverse the list to calculate the number of elements. You can add a field to the List structure to record the number of elements in the list, and update it during element addition and deletion operations to improve performance.

```C
// https://github.com/preslavmihaylov/learn-c-the-hard-way/blob/master/33.LinkedListAlgorithms/liblcthw/src/lcthw/list_algos.c

// Use pointer make ..

List *List_merge_sort(List *list, List_compare cmp) {
    if (List_count(list) <= 1) return list;

    List *left = List_create();
    List *second = List_create();
    List *result = List_create();

    int i = 0;
    LIST_FOREACH(list, first, next, cur) {

        if (i < List_count(list) / 2) {
            List_push(left, cur->value);
        } else {
            List_push(second, cur->value);
        }

        i++;
    }

    left = List_merge_sort(left, cmp);
    second = List_merge_sort(second, cmp);
	
    ListNode *firstNode = left->first;
    ListNode *secondNode = second->first;
    while (firstNode != NULL && secondNode != NULL) {
        if (cmp(firstNode->value, secondNode->value) <= 0) {
            List_push(result, firstNode->value);
            firstNode = firstNode->next;
        } else {
            List_push(result, secondNode->value);
            secondNode = secondNode->next;
        }
    }

    while (firstNode != NULL) {
        List_push(result, firstNode->value);
        firstNode = firstNode->next;
    }
    
    while (secondNode != NULL){
        List_push(result, secondNode->value);
        secondNode = secondNode->next;
    }
	
	//printList("RESULT ARRAY: ", result);
    
    List_destroy(left);
    List_destroy(second);

	return result;
}
```

* The bubble sort description in Wikipedia mentions a few optimizations. Try to implement them.

1. Use the ListNode pointer cur instead of LIST_FOREACH macros: The LIST_FOREACH macro was used in the original code to traverse the linked list, but the next node is refetched in each loop, which is less efficient. Improved use of a ListNode pointer cur to explicitly traverse the linked list, avoiding repeated macro calls.

2. Use while loops instead of LIST_FOREACH macros: LIST_FOREACH macros were used in the original code to traverse the linked list, but the implementation of such macros can cause additional overhead. After the improvement, use a while loop to traverse the linked list, which is more concise and efficient.

3. Optimize comparison and swap operations: The ListNode_swap function was used in the original code to exchange the values of the node, and you can consider exchanging the node pointer directly to avoid additional value exchange operations. In addition, the comparison operation can be moved out of the inner if condition judgment to reduce the number of repeated comparisons.
```C
int List_bubble_sort(List *list, List_compare cmp) {
    int sorted = 1;

    if (List_count(list) < 1) {
        return 0;               // already sorted
    }

    ListNode *cur = NULL;
    do {
        sorted = 1;
        // LIST_FOREACH(list, first, next, cur) {
        //     if (cur->next) {
        //         if (cmp(cur->value, cur->next->value) > 0) {
        //             ListNode_swap(cur, cur->next);
        //             sorted = 0;
        //         }
        //     }
        // }
        cur = list->first;
        while(cur->next) {
            if (cmp(cur->value, cur->next->value) > 0) {
                ListNode_swap(cur, cur->next);
                sorted = 0;
            }
            cur = cur->next;
        }
    } while(!sorted);

    return 0;
}
```
* Can you use the ``List_split`` and ``List_join`` (if you implemented them) to improve merge sort?
* Go through of all the defensive programming checks and improve the robustness of this implementation, protecting against bad ``NULL`` pointers, and then create an optional debug level invariant that works like ``is_sorted`` does
  after a sort.



Breaking It
====

* Overload the data structure to hit the worst case time complexity.
* Give it a bad data structure.



Extra Credit
====

* Create a unit test that compares the performance of the two algorithms.  You'll want to look at ``man 3 time`` for a basic timer function,  and run enough iterations to at least have a few seconds of samples.
* Play with the amount of data in the lists that need to be sorted and see if that changes your timing.
* Find a way to simulate filling different sized random lists, measuring how long they take. Then, graph the result to see how it compares to the description of the algorithm.



Extra Credit
====

* Try to explain why sorting linked lists is a really bad idea.
* Implement a ``List_insert_sorted`` that will take a given value, and using the ``List_compare``, insert the element at the
  right position so that the list is always sorted.  How does using this method compare to sorting a list after you've built it?
* Try implementing the bottom-up merge sort described on the Wikipedia page.  The code there is already C, so it should be easy to
  recreate, but try to understand how it's working compared to the slower one I have here.



End Of Lecture 33
=====

