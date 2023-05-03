# Exercise 19: A Simple Object System
## Audit the game
look at ex19.c
-   Review each function you define, one file at a time.
-   At the top of each function, add to ensure that the parameters are correct. For example, in to add.assertObject_newassert(description != NULL)
-   Browse through each line of the function to find any function that was called. Read their documentation (or man pages) to confirm what they return under error. Add another assertion to check if the error occurred. For example, checks that should occur after a call.Object_newcallocassert(el != NULL)
-   If the function should return a value, also make sure it returns an error value (for example), or add an assertion to ensure that the return value is valid. For example, you need to add before the final return, because it shouldn't be.NULLObject_newassert(el != NULL)NULL
-   For each statement you write, make sure you have a statement unless it's used for error checking and exiting.ifelse
-   For every statement you write, make sure that there is a branch that handles any unexpected situations.switchdefault

## Extra Credit
### Update the Makefile so that when you do make clean it will also remove the object.o file.
```
CFLAGS = -Wall -g

all: ex19

ex19: object.o

clean:
	rm -rf ex19 object.o
```

### Write a test script that can call the game in multiple ways and extend the Makefile to enable testing the game by running make test.
```bash
chmod u+x ex19.exp
```
```
CFLAGS = -Wall -g

all: ex19

ex19: object.o

clean:
	rm -rf ex19 object.o

test:
    ./ex19.exp
```

### Add more rooms and monsters to the game.
```C
// please look at ex19.c
// add bedroom
throne->north = bedroom;
bedroom->south = throne;
// add good monster
// add more monster
kitchen->bad_guy = NEW(Monster, "The good minotaur");
```

### Put the game's logic in another file and compile it to. Then, use it to write another mini-game. If you write it correctly, you'll create new sums and functions in your new game..oMapmain

```C
gcc -c ex19_without_main.c
gcc -c ex19_main.c
// object.o has been done before
gcc -o ex19 ex19_main.o ex19_without_main.o object.o

// /usr/bin/ld: warning: object.o: unsupported GNU_PROPERTY_TYPE (5) type: 0xc0010002
// /usr/bin/ld: warning: object.o: unsupported GNU_PROPERTY_TYPE (5) type: 0xc0010001
```

### tips
```bash
# original ex19 I don't have enough knowledge to complete  it, so there are some propblem hidden...
```
## ref
>[expect](https://core.tcl-lang.org/expect/index)

>[learn c the hard way solution orginal ex19](https://github.com/Frederick-S/Learn-C-The-Hard-Way-Exercise)

>[learn c the hard way solution ex19](https://github.com/preslavmihaylov/learn-c-the-hard-way)