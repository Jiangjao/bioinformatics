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

* The bubble sort description in Wikipedia mentions a few optimizations. Try to implement them.
* Can you use the ``List_split`` and ``List_join`` (if you implemented them) to improve merge sort?
* Go through of all the defensive programming checks and improve the robustness of
  this implementation, protecting against bad ``NULL`` pointers, and then create
  an optional debug level invariant that works like ``is_sorted`` does
  after a sort.



Breaking It
====

* Overload the data structure to hit the worst case time complexity.
* Give it a bad data structure.



Extra Credit
====

* Create a unit test that compares the performance of the two algorithms.  You'll want to look at ``man 3 time`` for a basic timer function,
  and run enough iterations to at least have a few seconds of samples.
* Play with the amount of data in the lists that need to be sorted and see if that changes your timing.
* Find a way to simulate filling different sized random lists, measuring how long they take. Then, graph the result to see how it compares to the
  description of the algorithm.



Extra Credit
====

* Try to explain why sorting linked lists is a really bad idea.
* Implement a ``List_insert_sorted`` that will take a given value, and using the ``List_compare``, insert the element at the
  right position so that the list is always sorted.  How does using this method compare to sorting a list after you've built it?
* Try implementing the bottom-up merge sort described on the Wikipedia page.  The code there is already C, so it should be easy to
  recreate, but try to understand how it's working compared to the slower one I have here.



End Of Lecture 33
=====

