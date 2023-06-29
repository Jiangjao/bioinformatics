#include <stdio.h>
#include <dlfcn.h>
#include "dbg.h"

int main(int argc, char *argv[]) {
    void *handle;
    int (*lowercase)(const char *);
    void (*hello)();

    handle = dlopen("./libex29.so", RTLD_NOW);
    // if (!handle) {
    //     printf("Failed to open shared library: %s\n", dlerror());
    //     return 1;
    // }
    check(handle != NULL, "Failed to open shared lirary: %s\n", dlerror());

    lowercase = dlsym(handle, "lowercase");
    check(lowercase != NULL, "Failed to find symbol: %s\n", dlerror());
    lowercase("The lowercase function works fine");

    hello = dlsym(handle, "hello");

    // if (!hello) {
    //     printf("Failed to find symbol: %s\n", dlerror());
    //     return 1;
    // }
    check(hello != NULL, "Failed to find symbol: %s\n", dlerror());
    hello();


    dlclose(handle);

    return 0;

error:
    return 1;
}






