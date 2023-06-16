#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <glob.h>

#define MAX_LINE_LENGTH 1024

/**
 * Find files matching a pattern using the glob library.
 */
char **find_files(const char *pattern) {
    glob_t pglob;
    int result = glob(pattern, 0, NULL, &pglob);

    if (result == 0) {
        char **files = malloc(sizeof(char *) * (pglob.gl_pathc + 1));
        if (files == NULL) {
            fprintf(stderr, "Error: Failed to allocate memory.\n");
            globfree(&pglob);
            exit(EXIT_FAILURE);
        }

        // Copy the file names to new memory.
        for (size_t i = 0; i < pglob.gl_pathc; i++) {
            files[i] = strdup(pglob.gl_pathv[i]);
            if (files[i] == NULL) {
                fprintf(stderr, "Error: Failed to allocate memory.\n");
                globfree(&pglob);
                exit(EXIT_FAILURE);
            }
        }

        // Set the last pointer to NULL so we can iterate over the file list.
        files[pglob.gl_pathc] = NULL;
        globfree(&pglob);
        return files;
    } else if (result == GLOB_NOMATCH) {
        fprintf(stderr, "Error: No files matching pattern '%s'.\n", pattern);
        return NULL;
    } else {
        fprintf(stderr, "Error: glob() failed with error code %d.\n", result);
        return NULL;
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <pattern>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    int flag = 0;
    char *match = argv[1];
    char tokens_string_with_space[MAX_LINE_LENGTH] = {""};

    // Check if the -o option is present in the command line arguments and merge its subsequent arguments into a single string.
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-o") == 0 && i + 1 < argc) {
            flag = 1;
            int j = i + 1;
            while (j < argc && argv[j][0] != '-') {
                strcat(tokens_string_with_space, argv[j]);
                strcat(tokens_string_with_space, " ");
                printf("-i parameter: %s\n", argv[j]);
                j ++;
            }
            break;
        }
    }

    // Remove trailing space from the string.
    int len = strlen(tokens_string_with_space);
    tokens_string_with_space[len - 1] = '\0';

    if (flag == 1) {
        match = tokens_string_with_space;
    }

    printf("match_string loaded...%s\n", match);

    FILE *fp = NULL;
    char buffer[MAX_LINE_LENGTH];
    int line_number = 1;

    // Find all files in the specified directory.
    const char *pattern = "/home/ubuntu/learn_C_the_hard_way/ex26/logfind.1/*";
    char **files = find_files(pattern);

    if (files == NULL) {
        return 1;
    }

    // Iterate over all files and search for the matching string in each file.
    for (size_t i = 0; files[i] != NULL; i++) {
        fp = fopen(files[i], "r");
        if (fp == NULL) {
            fprintf(stderr, "Error: Failed to open file.\n");
        } else {
            line_number = 1;
            while (fgets(buffer, MAX_LINE_LENGTH, fp) != NULL) {
                if (strstr(buffer, match) != NULL) {
                    printf("file %s \nLine %d: %s", files[i], line_number, buffer);
                }
                line_number ++;
            }
            fclose(fp);
        }
        free(files[i]);
    }
    free(files);

    return 0;
}