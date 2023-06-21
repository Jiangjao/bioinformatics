#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <glob.h>

#define MAX_LINE_LENGTH 1024

/**
 * Find files matching a pattern using the glob library.
 */
char **find_files(glob_t pglob, const char *pattern) {

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
        if (files == NULL) {
            fprintf(stderr, "Error: Failed to allocate memory.\n");
            exit(EXIT_FAILURE);
        }
        return files;
    } else if (result == GLOB_NOMATCH) {
        fprintf(stderr, "Error: No files matching pattern '%s'.\n", pattern);
        return NULL;
    } else {
        fprintf(stderr, "Error: glob() failed with error code %d.\n", result);
        return NULL;
    }
}


char *process_arguments(int argc, char *argv[], char *match) {

    // set a flag to reminder "-o" argument whether exist.
    int flag = 0;

    // set match the default value to argv[1]
    // match = argv[1];
    char tokens_string_with_space[MAX_LINE_LENGTH] = {""};
    // Parse the command line arguments 
    for (int i = 1; i < argc; i++) {
        // FIXME (xiaojiao): The parameter after '- o' cannot match 2023/06/21
        if (strcmp(argv[i], "-o") == 0 && (i + 1 < argc)) {
            flag = 1;
            int j = i + 1;
            // printf("index %d 2 %s\n", j, argv[j]);
            while (j < argc && argv[j][0] != '-') {
                strcat(tokens_string_with_space, argv[j]);
                strcat(tokens_string_with_space, " ");
                // printf("-i parameter: %s\n", argv[j]);
                j ++;
            }
            break;
        } else {
            // flag = 0;
            strcpy(match, argv[i]);
        }
    }

    // printf("tokens_string_with_space is <%s>", tokens_string_with_space);
    // Remove trailing space from the string.
    int len = strlen(tokens_string_with_space);
    tokens_string_with_space[len - 1] = '\0';

    if (flag != 0) {
        match = tokens_string_with_space;
    }

    // Actually, the match string was not passed out
    return match;
}

void printf_match_line_with_file(char *match_string, char **files) {
    char *match = match_string;
    FILE *fp = NULL;
    char buffer[MAX_LINE_LENGTH];
    int line_number = 1;

    // Iterate over all files and search for the matching string in each file.
    for (size_t i = 0; files[i] != NULL; i++) {
        fp = fopen(files[i], "r");
        if (fp == NULL) {
            fprintf(stderr, "Error: Failed to open file.\n");
        } else {
            // reset the line_number at first.
            line_number = 1;
            while (fgets(buffer, MAX_LINE_LENGTH, fp) != NULL) {
                // Why can it even match white spaces?
                // (TODO:xiajiao)Why I use ./logfind5 word word, it can match each line? 2023/06/21
                if (strstr(buffer, match) != NULL) {
                    printf("file %s \nLine %d: %s", files[i], line_number, buffer);
                }
                line_number ++;
            }
            fclose(fp);
        }
        free(files[i]);
    }
}

int main(int argc, char *argv[]) {

    if (argc < 2) {
        fprintf(stderr, "Usage: %s <pattern>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    glob_t pglob;
    char *match = argv[1];
    // char *match = "";

    match = process_arguments(argc, argv, match);

    printf("match_string loaded...%s\n", match);

    // Find all files in the specified directory.
    const char *pattern = "/home/ubuntu/learn_C_the_hard_way/ex26/logfind.1/*";
    char **files = find_files(pglob, pattern);

    printf_match_line_with_file(match, files);

    free(files);

    return 0;
}