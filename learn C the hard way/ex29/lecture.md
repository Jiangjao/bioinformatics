Learn C The Hard Way
=======

Exercise 29
----

Libraries and Linking



The Plan
====

* Learn about libraries and how to link against them.
* Learn how to load a dynamic library from inside C.



The Code
====

I'll use the project I started from the previous exercise.
This covers some of the extra credit.



The Analysis
====

This analysis might take a while, but be sure you know Exercise 28 well.



Breaking It
====

* Wreck the libex29.so file.



Extra Credit
====

* Were you paying attention to the bad code I have in the ``libex29.c`` functions? Do you see how, even though I use a for-loop they still check for ``'\0'`` endings?  Fix this so that the functions always take a length for the string to work with inside the function.

```C
#include <stdio.h>
#include <ctype.h>
#include "dbg.h"


int print_a_message(const char *msg) {
    printf("A STRING: %s\n", msg);

    return 0;
}



int uppercase(const char *msg) {
    int i = 0;    
    int len = strlen(msg);

    for (i = 0; i < len; i++) {
        printf("%c", tolower(msg[i]));
    }
    // // BUG: \0 termination problems
    // for(i = 0; msg[i] != '\0'; i++) {
    //     printf("%c", toupper(msg[i]));
    // }

    printf("\n");

    return 0;
}


int lowercase(const char *msg) {
    int i = 0;

    int len = strlen(msg);

    for (i = 0; i < len; i++) {
        printf("%c", tolower(msg[i]));
    }
    // BUG: \0 termination problems
    // for (i = 0; msg[i] != '\0'; i++) {
    //     printf("%c", tolower(msg[i]));
    // }

    printf("\n");

    return 0;
}


int fail_on_purpose(const char *msg) {
    return 1;
}

```

* Read the ``man dlopen`` documentation and read about all of the related functions.  Try some of the other options to ``dlopen``  beside ``RTLD_NOW``.

```text
please see the hello_test.c
```



End Of Lecture 29
=====

