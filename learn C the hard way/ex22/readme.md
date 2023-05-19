Learn C The Hard Way
=======

Exercise 22
----

The Stack, Scope, and Globals



The Plan
====

* Start to learn about scope.
* Stack vs. global.
* Scope levels inside a function.
* The *extern* keyword.


The Code
====

This exercises requires two files:

    * ex22.c
    * ex22_main.c



The Analysis
====



Fixing It
====

Instead of breaking this one I'm going to fix it.

* Do not shadow a variable like *count* on ex22_main.c:11.
* Avoid using too many globals.
* When in doubt, put it on the heap (malloc).
* Don't use function static variables like I did in ex22.c:update_ratio.
  * [update_ratio on pythontutor website](https://pythontutor.com/visualize.html#code=double%20update_ratio%28double%20new_ratio%29%0A%7B%0A%20%20%20%20static%20double%20ratio%20%3D%201.0%3B%0A%0A%20%20%20%20double%20old_ratio%20%3D%20ratio%3B%0A%20%20%20%20ratio%20%3D%20new_ratio%3B%0A%0A%20%20%20%20return%20old_ratio%3B%0A%7D%0A%0Aint%20main%28%29%20%7B%0A%20%20update_ratio%283%29%3B%0A%20%20update_ratio%2810%29%3B%0A%20%20update_ratio%284%29%3B%0A%20%20return%200%3B%0A%7D&cppShowMemAddrs=true&cumulative=false&curInstr=18&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=c_gcc9.3.0&rawInputLstJSON=%5B%5D&textReferences=false)
* Avoid reusing function parameters.



Breaking It
====

* Try to directly access variables in ``ex22.c`` from ``ex22_main.c``
  that you think you can't.  For example, can you get at ``ratio``
  inside ``update_ratio``? What if you had a pointer to it?
  No, some error will happen...
```bash
 error: ‘ratio’ undeclared (first use in this function)
     printf("ratio address is ?", &ratio);
```

* Ditch the ``extern`` declaration in ``ex22.h`` to see what
  errors or warnings you get.
```bash
# it seems nothing happened...
```

* Add ``static`` or ``const`` specifiers to different variables,
  and then try to change them.
```C
// if I assigned THE_SIZE with constation in ex22.c, then some error will happend...
// const int THE_SIZE = 1000;
ex22.c:5:11: error: conflicting type qualifiers for ‘THE_SIZE’
 const int THE_SIZE = 1000;
           ^~~~~~~~
In file included from ex22.c:2:0:
ex22.h:5:5: note: previous declaration of ‘THE_SIZE’ was here
 int THE_SIZE;
     ^~~~~~~~

```


Extra Credit
====

* Research the concept of pass by value verses pass by reference.  Write an
  example of both.
```C
#include <stdio.h>
#include "ex22.h"
#include "dbg.h"

void swap_with_pointer(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int x = 1, y = 2;
    swap(x, y);
    printf("swap a, b without pointer x=%d, y=%d\n", x, y);
    swap_with_pointer(&x, &y);
    printf("swap a, b with pointer x=%d, y=%d\n", x, y);

    return 0;
}
```

* Use pointers to gain access to things you shouldn't have access to.
* Use your debugger to see what this kind of access looks like when you do it wrong.
* Write a recursive function that causes a stack overflow.  Don't know  what a recursive function is?  Try calling ``scope_demo`` at the  bottom of ``scope_demo`` itself so that it loops.
```C
// if I modified the scope_demo as suggested...
void scope_demo(int count) {
    log_info("count is:%d", count);

    if (count > 10) {
        int numbers = 100;  // BAD! BUGS!

        log_info("count in this scope is %d", numbers);
    }

    log_info("count is at exit:%d", count);

    count = 3000;

    log_info("count after assign: %d", count);
    scope_demo(count);
}

//   Console is outputting infinitely.
```

* Rewrite the ``Makefile`` so that it can build this.
```
please see the Makefile
```


End Of Lecture 22
=====

