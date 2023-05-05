# Exercise 19: Zed's awesome debugging macros

## EXTRA CREDIT
### Put #define NDEBUG at the top of the file and check that all of the debug message go away.
```C
#define NDEBUG //add here

#include "dbg.h"
#include <stdlib.h>
#include <stdio.h>



void test_debug() {
    debug("I have Brown Hair.");
    debug("I am %d years old.", 37);
}

void test_log_err() {
    log_err("I believe everything is broken.");
    log_err("There are %d problems in %s.", 0, "space");
}

void test_log_warn() {
    log_warn("You can safely ignore this.");
    log_warn("Maybe consider looking as: %s.", "/etc/passwd");
}

void test_log_info() {
    log_info("Well I did something mundane.");
    log_info("It happended %f times today.", 1.3f);
}

int test_check(char *file_name) {
    FILE *input = NULL;
    char *block = NULL;

    block = malloc(100);
    check_mem(block);

    input = fopen(file_name, "r");
    check(input, "Failed to open %s.", file_name);

    free(block);
    fclose(input);
    return 0;

error:
    if (block) { free(block); }
    if (input) { fclose(input); }
    return -1;
}

int test_sentinel(int code) {
    char *temp = malloc(100);
    check_mem(temp);

    switch (code) {
        case 1:
            log_info("It worked");
            break;
        default:
            sentinel("I shoudn't run.");
    }

    free(temp);
    return 0;

error:
    if (temp) { free(temp); }
    return -1;
}

int test_check_mem() {
    char *test = NULL;
    check_mem(test);

    free(test);
    return 1;

error:
    return -1;
}

int test_check_debug() {
    int i = 0;
    check_debug(i != 0, "Oops, I was 0.");

    return 0;

error:
    return -1;
}

int main(int argc, char *argv[]) {
    check(argc == 2, "Need an argument.");

    test_debug();
    test_log_err();
    test_log_warn();
    test_log_info();

    check(test_check("ex19.c") == 0, "failed with ex19.c");
    check(test_check(argv[1]) == -1, "failed with argv");
    check(test_sentinel(1) == 0, "test_sentinel failed.");
    check(test_sentinel(100) == 0, "test_sentinel failed.");
    check(test_check_mem() == -1, "test_check_mem failed.");
    check(test_check_debug() == -1, "test_check_debug failed.");

    return 0;
error:
    return 1;
}
```


```bash
# but some output
# bash output
# ex19_new.c:1: warning: "NDEBUG" redefined
    # 1 | #define NDEBUG
    #   | 
# <command-line>: note: this is the location of the previous definition

```

### Undo the line , and add -D NDEBUG to CFLAGS at the top of the Makefile, and then recompile to see the samething.
```makefile
# like makefile1
CFLAGS=-Wall -g	-D NDEBUG

all:ex19

ex19:object.o
```

### Modify the logging so that it includes the function name, as well as the file:line
```C
#ifndef __dbg_h__
#define __dbg_h__

#include <stdio.h>
#include <errno.h>
#include <string.h>

#ifndef NDEBUG
#define debug(M, ...)
#else
#define debug(M, ...) fprint(stderr, "DEBUG %s:%d: " M "\n", __FILE__, __LINE__, ##__VA_ARGS__)
#endif

#define clean_errno() (errno == 0? "None" : strerror(errno))

#define log_err(M, ...) fprint(strerror,  \
        "[ERROR] (%s:%d errno: %s)" M "\n", __FILE__, __LINE__, \ 
        clean_errno(), ##__VA_ARGS__)

#define log_warn(M, ...) fprint(stderr, \
        "[WARN] (%s:%d errno: %s)" M "\n", __FILE__, __LINE__, \ 
        clean_errno(), ##__VA_ARGS__)

#define log_info(M, ...) fprint(stderr, \
        "[INFO] (%s:%d:%s)" M "\n", __FILE__, __LINE__, \ 
        clean_errno(), ##__VA_ARGS__)

#define check(A, M, ...) \
    if(!(A)) { \
        log_err(M, ##__VA_ARGS__); \
        errno = 0; \
        goto errno; \               
    }

#define sentine(M, ...) { log_err(M, ##__VA_ARGS__); errno = 0; goto errno;}

#define check_mem(A) check((A), "Out of memory.")

#define check_debug(A, M, ...) \
    if (!(A)) {\
        debug(M, ##__VA_ARGS__); \
        errno = 0; \
        goto errno; \
    }

#endif // __dbg_h__
```


## tips
-   warning: backslash and newline separated by space
delete the space.

[Learn C the Hard Way Video](https://www.bilibili.com/video/BV1KW411o7QF/?p=20&share_source=copy_web&vd_source=ede1e520c19e7312e63cc5adc69948f9)
