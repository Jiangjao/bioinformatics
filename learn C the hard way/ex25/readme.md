Learn C The Hard Way
=======

Exercise 25
----

Variable Argument Functions



The Plan
====

* Use variable argument functions.
* Write our own simple version of *scanf*.



The Code
====



The Analysis
====



Breaking It
====

* Change the code so that you forget to pass in the initial size for '%s' formats.
It cannot handle formatting errors.
* Give it more data than ``MAX_DATA``, and then see how omitting ``calloc`` in ``read_string`` changes how it works.
It will read a specific length string from the buffer, such as MAX_ The length of DATA and truncation
* There's a problem where fgets eats the newlines, so try to fix that using``fgetc`` but leave out the ``\0`` that ends the string.
```C
#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>
#include "dbg.h"

#define MAX_DATA 10

int read_string(char **out_string, int max_buffer) {
    *out_string = calloc(1, max_buffer);
    check_mem(*out_string);

    int i = 0;
    char c;
    // char *result = NULL;
    //  read character, stop by '\n' or size limitation
    ;
    while (i < max_buffer - 1 && (c = fgetc(stdin)) != '\n' && c != EOF) {
        (*out_string)[i++] = c;
    }
    (*out_string)[i] = '\0';
    // char *result = fgets(*out_string, max_buffer, stdin);
    check(*out_string != NULL, "Input error.");

    return 0;

error:
    if (*out_string) free(*out_string);
    *out_string = NULL;
    return -1;
}

int read_int(int *out_int) {
    char *input = NULL;
    int rc = read_string(&input, MAX_DATA);
    check(rc == 0, "Failed to read number.");

    *out_int = atoi(input);

    free(input);
    return 0;

error:
    if (input) free(input);
    return -1;
}

int read_scan(const char *fmt, ...) {
    int i = 0;
    int rc = 0;
    int *out_int = NULL;
    char *out_char = NULL;
    char **out_string = NULL;
    int max_buffer = 0;

    va_list argp;
    va_start(argp, fmt);

    for (i = 0; fmt[i] != '\0'; i++) {
        if (fmt[i] == '%') {
            i++;
            switch (fmt[i]) {
                case '\0':
                    sentinel("Invalid format, you ended with %%.");
                    break;
                
                case 'd':
                    out_int = va_arg(argp, int *);
                    rc = read_int(out_int);
                    check(rc == 0, "Failed to read int.");
                    break;

                case 'c':
                    out_char = va_arg(argp, char *);
                    *out_char = fgetc(stdin);
                    break;

                case 's':
                    max_buffer = va_arg(argp, int);
                    out_string = va_arg(argp, char **);
                    rc = read_string(out_string, max_buffer);
                    check(rc == 0, "Failed to read string");
                    break;

                default:
                    sentinel("Invalid format.");
            }
        } else {
            fgetc(stdin);
        }

        check(!feof(stdin) && ! ferror(stdin), "Input error.");
    }

    va_end(argp);
    return 0;

error:
    va_end(argp);
    return -1;
}

int main(int argc, char *argv[]) {
    char *first_name = NULL;
    char initial = ' ';
    char *last_name = NULL;
    int age = 0;

    printf("What's your first name?");
    int rc = read_scan("%s", MAX_DATA, &first_name);
    check(rc == 0, "Failed first name.");

    printf("What's your initial?");
    rc = read_scan("%c\n", &initial);
    check(rc == 0, "Failed initial.");

    printf("What's your last name?");
    rc =  read_scan("%s", MAX_DATA, &last_name);
    check(rc == 0, "Failed last name.");

    printf("How old are you?");
    rc = read_scan("%d", &age);

    printf("---- RESULTS ----\n");
    printf("First Name: %s\n", first_name);
    printf("Initial: '%c'\n", initial);
    printf("Last Name: %s\n", last_name);
    printf("Age: %d\n", age);

    free(first_name);
    free(last_name);
    return 0;
error:
    return -1;
}

```


Extra Credit
====

* Make double and triple sure that you know what each of the ``out_``  variables are doing.  Most importantly, you should know what is ``out_string`` is and how it's a pointer to a pointer, , so that you understand when you're setting the pointer versus the contents is important.  Break down each of the  ``out_string``


``Out_string`` is a second level pointer because read_ The string function needs to dynamically allocate memory to store the input string and assign the allocated memory address to out_ The pointer pointed to by the string. If out_ If string is a first level pointer, then read_ The string function can only modify the content of the string pointed to by the pointer, and cannot modify the value of the pointer itself, which means it cannot return the dynamically allocated memory address to the caller.

Maybe we should look at stack and heap of each function...


Extra Credit
====

* Write a similar function to ``printf`` that uses the varargs system, and rewrite ``main`` to use it.
* As usual, read the man page on all of this so that you know what it does on your platform.  Some platforms will use macros, others will use functions, and some will have these do nothing.  It all depends on the compiler and the platform you use.



End Of Lecture 25
=====
