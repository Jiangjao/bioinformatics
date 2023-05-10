Learn C The Hard Way
=======

Exercise 21
----

Advanced Data Types and Flow Control



The Plan
====

* Learn about the basic types and keywords for them.
* Cover all the keywords for modifying those types.
* Review fixed exact size types.
* Learn all the different operators on those types.

This is mostly a review!



Available Data Types
====

    int    Stores a regular integer, defaulting to 32 bits in size.
    double Holds a large floating point number.
    float  Holds a smaller floating point number.
    char   Holds a single 1 byte character.
    void   Indicates "no type".
    enum   Enumerated types, which work as and convert to integers.



Type Modifiers
====

    unsigned  Non-negative numbers.
    signed    Gives you negative and positive numbers.
    long      Bigger number.
    short     Smaller number.



Type Qualifiers
====

    const     Constant.
    volatile  Compiler can't trust it.
    register  Put it in a CPU register.



Type Conversion
====

C type promotion order:

* long double
* double
* float
* int (but only char and short int);
* long

When in doubt, parens it out!



Exact Size Types
====

If you need exact sizes use these:

    int8_t   8-bit signed integer
    uint8_t  8-bit unsigned integer
    int16_t  16-bit signed integer
    uint16_t 16-bit unsigned integer
    int32_t  32-bit signed integer
    uint32_t 32-bit unsigned integer
    int64_t  64-bit signed integer
    uint64_t 64-bit unsigned integer



Getting Sizes
====

Refer to the book as there's a large number of
macros to help you get size information for types.

Examples:

    int_least32_t  int that holds at least 32 bits.
    uint_fast32_t  unsigned fastest int for 32 bits.
    intptr_t       signed int that can hold a pointer.
    PTRDIFF_MAX    maximum value of ptrdiff_t
    SIZE_MAX       maximum value of a size_t



Available Operators
-------------------

This section is a review of what you memorized already
to make sure you know everything.

Memorize these again to be sure you have them.



Extra Credit
====

* Read stdint.h or a description of it, and write out all the
  available size identifiers.
  `stdint.h` is a header file in the C programming language that provides a set of typedefs that specify exact-width integer types, along with macros that specify minimum and maximum allowable values for each type. The available size identifiers in `stdint.h` are as follows:
  Sure, here's a list of the available size identifiers in `stdint.h` with numbers and brief explanations:

  1. `int8_t`: 8-bit signed integer
  2. `int16_t`: 16-bit signed integer
  3. `int32_t`: 32-bit signed integer
  4. `int64_t`: 64-bit signed integer
  5. `uint8_t`: 8-bit unsigned integer
  6. `uint16_t`: 16-bit unsigned integer
  7. `uint32_t`: 32-bit unsigned integer
  8. `uint64_t`: 64-bit unsigned integer
  9. `int_least8_t`: smallest signed integer type with at least 8 bits
  10. `int_least16_t`: smallest signed integer type with at least 16 bits
  11. `int_least32_t`: smallest signed integer type with at least 32 bits
  12. `int_least64_t`: smallest signed integer type with at least 64 bits
  13. `uint_least8_t`: smallest unsigned integer type with at least 8 bits
  14. `uint_least16_t`: smallest unsigned integer type with at least 16 bits
  15. `uint_least32_t`: smallest unsigned integer type with at least 32 bits
  16. `uint_least64_t`: smallest unsigned integer type with at least 64 bits
  17. `int_fast8_t`: fastest signed integer type with at least 8 bits
  18. `int_fast16_t`: fastest signed integer type with at least 16 bits
  19. `int_fast32_t`: fastest signed integer type with at least 32 bits
  20. `int_fast64_t`: fastest signed integer type with at least 64 bits
  21. `uint_fast8_t`: fastest unsigned integer type with at least 8 bits
  22. `uint_fast16_t`: fastest unsigned integer type with at least 16 bits
  23. `uint_fast32_t`: fastest unsigned integer type with at least 32 bits
  24. `uint_fast64_t`: fastest unsigned integer type with at least 64 bits
  25. `intptr_t`: integer type capable of holding a pointer
  26. `uintptr_t`: unsigned integer type capable of holding a pointer

  Note that the exact sizes of these types can vary depending on the platform and compiler being used.
* Go through each item here and write out what it does in code.  Research it online so you know you got it right.

* Get this information memorized by making flash cards and spending 15
  minutes a day practicing it.
* Create a program that prints out examples of each type, and confirm that your
  research is right.
```C
#include <stdio.h>
#include <stdint.h>

int main() {
    int8_t a = -128;
    int16_t b = 32767;
    int32_t c = 2147483647;
    int64_t d = 9223372036854775807;
    uint8_t e = 255;
    uint16_t f = 65535;
    uint32_t g = 4294967295;
    // Since the constant is not explicitly marked as unsigned, 
    // the compiler assumes that it is a signed type, and therefore generates a warning.
    uint64_t h = 18446744073709551615ULL;
    int_least8_t i = -128;
    int_least16_t j = -32768;
    int_least32_t k = -2147483647 - 1;
    int_least64_t l = -9223372036854775807 - 1;
    uint_least8_t m = 0;
    uint_least16_t n = 0;
    uint_least32_t o = 0;
    uint_least64_t p = 0;
    int_fast8_t q = -128;
    int_fast16_t r = 32767;
    int_fast32_t s = 2147483647;
    int_fast64_t t = 9223372036854775807;
    uint_fast8_t u = 255;
    uint_fast16_t v = 65535;
    uint_fast32_t w = 4294967295;
    uint_fast64_t x = 18446744073709551615ULL;
    intptr_t y = (intptr_t)&a;
    uintptr_t z = (uintptr_t)&a;

    printf("int8_t: %d\n", a);
    printf("int16_t: %d\n", b);
    printf("int32_t: %d\n", c);
    printf("int64_t: %ld\n", d);
    printf("uint8_t: %u\n", e);
    printf("uint16_t: %u\n", f);
    printf("uint32_t: %u\n", g);
    printf("uint64_t: %lu\n", h);
    printf("int_least8_t: %d\n", i);
    printf("int_least16_t: %d\n", j);
    printf("int_least32_t: %d\n", k);
    printf("int_least64_t: %ld\n", l);
    printf("uint_least8_t: %u\n", m);
    printf("uint_least16_t: %u\n", n);
    printf("uint_least32_t: %u\n", o);
    printf("uint_least64_t: %lu\n", p);
    printf("int_fast8_t: %d\n", q);
    printf("int_fast16_t: %ld\n", r);
    printf("int_fast32_t: %ld\n", s);
    printf("int_fast64_t: %ld\n", t);
    printf("uint_fast8_t: %u\n", u);
    printf("uint_fast16_t: %lu\n", v);
    printf("uint_fast32_t: %lu\n", w);
    printf("uint_fast64_t: %lu\n", x);
    printf("intptr_t: %p\n", (void*)y);
    printf("uintptr_t: %p\n", (void*)z);

    return 0;
}

```


End Of Lecture 21
=====

