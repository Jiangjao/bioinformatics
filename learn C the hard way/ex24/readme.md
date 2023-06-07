Learn C The Hard Way
=======

Exercise 24
----

Input, Output, Files



The Plan
====

* Learn the basics of working with files in C.
* Get an initial list of the "f-functions".



The Code
====



The Analysis
====



Breaking It
====

* Trying out *fgets* and the problems with *gets*.
Great! `fgets` is a safer alternative to the `gets` function in C. The `gets` function reads characters from the standard input stream until it encounters a newline character or end-of-file (EOF) character. However, the `gets` function has no way to limit the number of characters it reads, which can lead to buffer overflow vulnerabilities.

On the other hand, `fgets` function reads at most a specified number of characters from the input stream, and stores them in a character array. It also appends a null character ('\0') to the end of the string. This ensures that the string is properly terminated and helps prevent buffer overflow vulnerabilities.

Here is an example of using `fgets` to read a string of up to 100 characters from the standard input stream:

```c
#include <stdio.h>

#define MAX_LENGTH 100

int main() {
    char input[MAX_LENGTH];
    printf("Enter a string (up to %d characters):\n", MAX_LENGTH - 1);
    fgets(input, MAX_LENGTH, stdin);
    printf("You entered: %s", input);
    return 0;
}
```

In the example above, the `fgets` function reads a string of up to `MAX_LENGTH - 1` characters from the standard input stream (`stdin`) into the `input` buffer. The `fgets` function stops reading when it encounters a newline character, or when it has read the maximum number of characters specified.

Note that the newline character is included in the input string if it is encountered before the maximum number of characters is reached. To remove the newline character, you can use the `strcspn` function to find the position of the newline character and replace it with a null character:

```c
#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 100

int main() {
    char input[MAX_LENGTH];
    printf("Enter a string (up to %d characters):\n", MAX_LENGTH - 1);
    fgets(input, MAX_LENGTH, stdin);
    input[strcspn(input, "\n")] = '\0';  // remove newline character, if any
    printf("You entered: %s\n", input);
    return 0;
}
```

In the modified example above, the `strcspn` function is used to find the position of the newline character in the input string (if it exists), and the character at that position is replaced with a null character. This ensures that the input string is properly terminated and does not include any newline characters.

* Feed it */dev/urandom* to give it garbage.

```shell
 valgrind ./ex24 < /dev/urandom
```


Extra Credit
====

* Rewrite this to not use ``fscanf`` at all.  You'll need to use functions like ``atoi`` to convert the input strings to numbers.
```C
#include <stdio.h>
#include <stdlib.h>
#include "dbg.h"

#define MAX_DATA 100

typedef enum EyeColor {
    BLUE_EYES, GREEN_EYES, BROWN_EYES,
    BLACK_EYES, OTHER_EYES
} EyeColor;

const char *EYE_COLOR_NAMES[] = {
    "Blue", "Green", "Brown", "Black", "Other"
};

typedef struct Person {
    int age;
    char first_name[MAX_DATA];
    char last_name[MAX_DATA];
    EyeColor eyes;
    float income;
} Person;

int main(int argc, char *argv[]) {
    Person you = {.age = 0};
    int i = 0;
    char *in = NULL;

    printf("What's your First Name?");
    in = fgets(you.first_name, MAX_DATA - 1, stdin);
    check(in != NULL, "Failed to read first name.");

    printf("What's your last_name?");
    in = fgets(you.last_name, MAX_DATA - 1, stdin);
    check(in != NULL, "Failed to read last name.");

    printf("How lod are you?");
    char age_input[MAX_DATA];
    in = fgets(age_input, MAX_DATA - 1, stdin);
    check(in != NULL, "You have to enter a number.");
    you.age = atoi(age_input);

    printf("What color are your eyes:\n");
    for(i = 0; i <= OTHER_EYES; i++) {
        printf("%d) %s\n", i + 1, EYE_COLOR_NAMES[i]);
    }
    printf("> ");

    int eyes = -1;
    // int rc = fscanf(stdin, "%d", &eyes);
    char eyes_input[MAX_DATA];
    in = fgets(eyes_input, MAX_DATA - 1, stdin);
    check(in != NULL, "You have to enter a number.");
    eyes = atoi(eyes_input);
    you.eyes = eyes - 1;
    check(you.eyes <= OTHER_EYES && you.eyes >= 0, "Do it right, that's not an option.");

    printf("how much do you make an hour?");
    char income_input[MAX_DATA];
    in = fgets(income_input, MAX_DATA - 1, stdin);
    check(in != NULL, "Enter a floating point number.");
    you.income = atof(income_input);

    printf("----- RESULTS ------\n");

    printf("First Name: %s", you.first_name);
    printf("Last Name: %s", you.last_name);
    printf("Age: %d\n", you.age);
    printf("Eyes: %s\n", EYE_COLOR_NAMES[you.eyes]);
    printf("Income: %f\n", you.income);

    return 0;
error:

    return -1;
}

```
* Change this to use plain ``scanf`` instead of ``fscanf`` to see what the difference is.
    The scanf function and the fscanf function can both be used to read data from input streams, but they have several differences:

  1. The scanf function reads data from the standard input stream, while the fscanf function can read data from any file stream.
  2. The first argument of the scanf function is the format string, which specifies the data type and format to be read, and the remaining arguments are pointers to the variables to be read. The first argument of the fscanf function is a file pointer, and the remaining arguments are the same as scanf.
   3. scanf skips over spaces and newline characters in the input buffer, while fscanf treats them as ordinary characters that must be explicitly specified in the format string in order to be read.
   4. scanf returns the number of parameters successfully read, while fscanf returns the number of data items successfully read.

    Therefore, if you only need to read data from the standard input stream, use the scanf function. If you need to read data from a file or require more precise control over the input format, use the fscanf function.
* Fix it so that their input names get stripped of the trailing newline  characters and any whites pace.

```C
#include <stdio.h>
#include <stdlib.h>
// #include <ctype.h>
#include "dbg.h"

#define MAX_DATA 100

typedef enum EyeColor {
    BLUE_EYES, GREEN_EYES, BROWN_EYES,
    BLACK_EYES, OTHER_EYES
} EyeColor;

const char *EYE_COLOR_NAMES[] = {
    "Blue", "Green", "Brown", "Black", "Other"
};

typedef struct Person {
    int age;
    char first_name[MAX_DATA];
    char last_name[MAX_DATA];
    EyeColor eyes;
    float income;
} Person;

void check_whitespace_or_newline(char *string) {
    char *in = NULL;
    in = string; 
    for (int i = 0;in[i] != '\0'; i ++) {
        if (in[i] == 32){
            printf("It has white space\n");
            // check("Failed to read first name.");
            // Failure with exit
            exit(-1);
        }
    }
}

int main(int argc, char *argv[]) {
    Person you = {.age = 0};
    int i = 0;
    char *in = NULL;

    printf(">####### your input should not have whitespace.########\n\n");
    printf("What's your First Name?");
    in = fgets(you.first_name, MAX_DATA - 1, stdin);
    check(in != NULL, "Failed to read first name.");
    check_whitespace_or_newline(in);
    // Remove leading whitespace

    printf("What's your last_name?");
    in = fgets(you.last_name, MAX_DATA - 1, stdin);
    check(in != NULL, "Failed to read last name.");
    check_whitespace_or_newline(in);

    // int age_input;
    printf("How lod are you?");
    char age_input[MAX_DATA];
    in = fgets(age_input, MAX_DATA - 1, stdin);
    check(in != NULL, "You have to enter a number.");
    check_whitespace_or_newline(in);
    you.age = atoi(age_input);

    printf("What color are your eyes:\n");
    for(i = 0; i <= OTHER_EYES; i++) {
        printf("%d) %s\n", i + 1, EYE_COLOR_NAMES[i]);
    }
    printf("> ");

    int eyes = -1;
    // int rc = fscanf(stdin, "%d", &eyes);
    char eyes_input[MAX_DATA];
    in = fgets(eyes_input, MAX_DATA - 1, stdin);
    check(in != NULL, "You have to enter a number.");
    eyes = atoi(eyes_input);
    you.eyes = eyes - 1;
    check(you.eyes <= OTHER_EYES && you.eyes >= 0, "Do it right, that's not an option.");

    printf("how much do you make an hour?");
    // FixME(xiaojiao)if I use scanf in eyes_color, then I cannot get the income_input by function fgets here. 2023/06/06
    char income_input[MAX_DATA];
    in = fgets(income_input, MAX_DATA - 1, stdin);
    check(in != NULL, "Enter a floating point number.");
    check_whitespace_or_newline(in);
    you.income = atof(income_input);

    printf("----- RESULTS ------\n");

    printf("First Name: %s", you.first_name);
    printf("Last Name: %s", you.last_name);
    printf("Age: %d\n", you.age);
    printf("Eyes: %s\n", EYE_COLOR_NAMES[you.eyes]);
    printf("Income: %f\n", you.income);

    return 0;
error:

    return -1;
}

```


Extra Credit
====

* Use ``scanf`` to write a function that reads one character at a time and files in the names but doesn't go past the end.  Make this function generic so it can take a size for the string, but just make sure you end the string with ``'\0'`` no matter what.

    1. The function can read a string of any length, but not beyond the end of the string.
    2. It is generic and can take a size for the string as a parameter.
    3. It ensures that the string is terminated with '\0', regardless of whether the number of characters read reaches the length of the string.
```C
#include <stdio.h>
#include <stdlib.h>
#include "dbg.h"

#define MAX_DATA 100

int write_character() {
    FILE *temp;
    // open a file
    temp = fopen("test.txt", "a+");
    printf("How lod are you?");
    char age_input;
    int rc = scanf("%c", &age_input);
    
    if (rc <= 0) {
        printf("you have to enter a character.");
    }

    // wite something into file
    if (temp != NULL) {
        
        fputc(age_input, temp);
        fputc('\0', temp);
        fclose(temp);
    }
    printf("----- RESULTS ------\n");

    printf("Age: %c\n", age_input);

    return rc;
}

void read_string(char *str, int size) {
    int i = 0;
    char c;

    // read character, stop by '\n' or size limitation
    while (i < size - 1 && scanf("%c", &c) == 1 && c != '\n') {
        str[i++] = c;
    }

    // ensure the string end with '\0'
    str[i] = '\0';
}

int main(int argc, char *argv[]) {
    char str[100];
    printf("########## some string will input below ##########\n");

    read_string(str, 100);

    printf("%s have been input\n", str);

    return 0;
}
```





End Of Lecture 24
=====

