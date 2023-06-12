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
fixme(xiaojiao):2023/06/12


The purpose of passing the pointer is to modify the value of the pointer itself inside the function, so that the function can modify the External variable. Specifically, if we only pass the pointer itself as a parameter, the modification of the pointer within the function will only affect the value of the pointer itself, and will not affect variables outside the function. However, if we pass the pointer of the pointer as a parameter, the function can access the pointer itself through the pointer, and modify the value in the memory address pointed to by the pointer itself, so as to modify the External variable.

>[stack and function on pythontutor](https://pythontutor.com/visualize.html#code=%23include%20%3Cstdlib.h%3E%0A%23include%20%3Cstdio.h%3E%0A%23include%20%3Cstdarg.h%3E%0A%0A%23define%20MAX_DATA%2010%0A%0Aint%20read_string%28char%20**out_string,%20int%20max_buffer%29%20%7B%0A%20%20%20%20*out_string%20%3D%20calloc%281,%20max_buffer%29%3B%0A%20%20%20%20int%20i%20%3D%200%3B%0A%20%20%20%20char%20c%3B%0A%20%20%20%20while%20%28i%20%3C%20max_buffer%20-%201%20%26%26%20%28c%20%3D%20fgetc%28stdin%29%29%20!%3D%20'%5Cn'%20%26%26%20c%20!%3D%20EOF%29%20%7B%0A%20%20%20%20%20%20%20%20%28*out_string%29%5Bi%2B%2B%5D%20%3D%20c%3B%0A%20%20%20%20%7D%0A%20%20%20%20%28*out_string%29%5Bi%5D%20%3D%20'%5C0'%3B%0A%20%20%20%20return%200%3B%0A%7D%0A%0Aint%20read_int%28int%20*out_int%29%20%7B%0A%20%20%20%20char%20*input%20%3D%20NULL%3B%0A%20%20%20%20int%20rc%20%3D%20read_string%28%26input,%20MAX_DATA%29%3B%0A%0A%20%20%20%20*out_int%20%3D%20atoi%28input%29%3B%0A%0A%20%20%20%20free%28input%29%3B%0A%20%20%20%20return%200%3B%0A%7D%0A%0Aint%20read_scan%28const%20char%20*fmt,%20...%29%20%7B%0A%20%20%20%20int%20i%20%3D%200%3B%0A%20%20%20%20int%20rc%20%3D%200%3B%0A%20%20%20%20int%20*out_int%20%3D%20NULL%3B%0A%20%20%20%20char%20*out_char%20%3D%20NULL%3B%0A%20%20%20%20char%20**out_string%20%3D%20NULL%3B%0A%20%20%20%20int%20max_buffer%20%3D%200%3B%0A%0A%20%20%20%20va_list%20argp%3B%0A%20%20%20%20va_start%28argp,%20fmt%29%3B%0A%0A%20%20%20%20for%20%28i%20%3D%200%3B%20fmt%5Bi%5D%20!%3D%20'%5C0'%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20%20%20%20%20if%20%28fmt%5Bi%5D%20%3D%3D%20'%25'%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20i%2B%2B%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20switch%20%28fmt%5Bi%5D%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20case%20'%5C0'%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20break%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20case%20'd'%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20out_int%20%3D%20va_arg%28argp,%20int%20*%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20rc%20%3D%20read_int%28out_int%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20break%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20case%20'c'%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20out_char%20%3D%20va_arg%28argp,%20char%20*%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20*out_char%20%3D%20fgetc%28stdin%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20break%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20case%20's'%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20max_buffer%20%3D%20va_arg%28argp,%20int%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20out_string%20%3D%20va_arg%28argp,%20char%20**%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20rc%20%3D%20read_string%28out_string,%20max_buffer%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20break%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20printf%28%22Invalid%20format.%22%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%20else%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20fgetc%28stdin%29%3B%0A%20%20%20%20%20%20%20%20%7D%0A%0A%20%20%20%20%7D%0A%20%20%20%20va_end%28argp%29%3B%0A%20%20%20%20return%200%3B%0A%7D%0A%0Aint%20main%28int%20argc,%20char%20*argv%5B%5D%29%20%7B%0A%20%20%20%20char%20*first_name%20%3D%20NULL%3B%0A%20%20%20%20char%20initial%20%3D%20'%20'%3B%0A%20%20%20%20char%20*last_name%20%3D%20NULL%3B%0A%20%20%20%20int%20age%20%3D%200%3B%0A%0A%20%20%20%20printf%28%22What's%20your%20first%20name%3F%22%29%3B%0A%20%20%20%20int%20rc%20%3D%20read_scan%28%22%25s%22,%20MAX_DATA,%20%26first_name%29%3B%0A%0A%0A%20%20%20%20printf%28%22What's%20your%20initial%3F%22%29%3B%0A%20%20%20%20rc%20%3D%20read_scan%28%22%25c%5Cn%22,%20%26initial%29%3B%0A%0A%0A%20%20%20%20printf%28%22What's%20your%20last%20name%3F%22%29%3B%0A%20%20%20%20rc%20%3D%20%20read_scan%28%22%25s%22,%20MAX_DATA,%20%26last_name%29%3B%0A%20%20%20%20printf%28%22How%20old%20are%20you%3F%22%29%3B%0A%20%20%20%20rc%20%3D%20read_scan%28%22%25d%22,%20%26age%29%3B%0A%0A%20%20%20%20printf%28%22----%20RESULTS%20----%5Cn%22%29%3B%0A%20%20%20%20printf%28%22First%20Name%3A%20%25s%5Cn%22,%20first_name%29%3B%0A%20%20%20%20printf%28%22Initial%3A%20'%25c'%5Cn%22,%20initial%29%3B%0A%20%20%20%20printf%28%22Last%20Name%3A%20%25s%5Cn%22,%20last_name%29%3B%0A%20%20%20%20printf%28%22Age%3A%20%25d%5Cn%22,%20age%29%3B%0A%20%20%20%20%0A%20%20%20%20free%28first_name%29%3B%0A%20%20%20%20free%28last_name%29%3B%0A%20%20%20%20return%200%3B%0A%7D&cumulative=false&curInstr=110&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=c_gcc9.3.0&rawInputLstJSON=%5B%5D&textReferences=true)

Extra Credit
====

* Write a similar function to ``printf`` that uses the varargs system, and rewrite ``main`` to use it.
* As usual, read the man page on all of this so that you know what it does on your platform.  Some platforms will use macros, others will use functions, and some will have these do nothing.  It all depends on the compiler and the platform you use.



End Of Lecture 25
=====
