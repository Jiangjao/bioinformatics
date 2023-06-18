#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <glob.h>

#define MAX_LINE_LENGTH 1024


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

        for (size_t i = 0; i < pglob.gl_pathc; i++) {
            files[i] = strdup(pglob.gl_pathv[i]);
            if (files[i] == NULL) {
                fprintf(stderr, "Error: Failed to allocate memory.\n");
                globfree(&pglob);
                exit(EXIT_FAILURE);
            }
        }
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
    // if (argc != 2) {
    //     fprintf(stderr, "Usage: %s <pattern>\n", argv[0]);
    //     exit(EXIT_FAILURE);
    // }
    
    // char **files = find_files(argv[1]);

    FILE *fp = NULL;
    char buffer[MAX_LINE_LENGTH];
    // string that will be matched
    char *match = "fprintf";
    int line_number = 1;

    const char *pattern = "/home/ubuntu/learn_C_the_hard_way/ex26/logfind.1/*";
    
    char **files = find_files(pattern);

    if (files == NULL) {
        return 1;
    }

    for (size_t i = 0; files[i] != NULL; i++) {
        // printf("%s\n", files[i]);
        // 尝试打开文件
        line_number = 1;
        fp = fopen(files[i], "r");
        if (fp == NULL) {
            fprintf(stderr, "Error: Failed to open file.\n");
        } else {
            printf("files %s has been opened\n", files[i]);
        }

        //  try to find the match string
        while (fgets(buffer, MAX_LINE_LENGTH, fp) != NULL) {
            if (strstr(buffer, match) != NULL) {
                // printf("Found: %s", buffer);
                printf("file %s \nLine %d: %s", files[i], line_number, buffer);
            }
            line_number ++;
        }
        fclose(fp);
        free(files[i]);
    }
    free(files);
    return 0;
}