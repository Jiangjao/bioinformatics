#include "dbg.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <glob.h>

const size_t MAX_LINE = 1024;


int list_file(glob_t *pglob) {
    char *line = calloc(MAX_LINE, 1);
    FILE *file = fopen(".logfind", "r");
    int glob_flags = GLOB_TILDE;
    int i = 0;
    int rc = -1;

    check(pglob != NULL, "Invalid glob_t given.");
    check_mem(line);
    check(file, "Failed to open .logfind. Make that first.");
    
    rc = glob("*.h", glob_flags, NULL, pglob);
    check(rc == 0, "Failed to glob.");
    rc = glob("*.c", glob_flags | GLOB_APPEND, NULL, pglob);
    check(rc == 0, "Failed to golb.");

    for (i = 0; i < pglob->gl_pathc; i++) {
        debug("Matched file: %s", pglob->gl_pathv[i]);
    }

    rc = 0;         // all good

error:              // failthrough
    if (line) free(line);
    return rc;
}


int scan_file(const char *filename, int search_len, char *search_for[]) {
    char *line = calloc(MAX_LINE, 1);
    FILE *file = fopen(filename, "r");
    char *found = NULL;
    int i = 0;

    check_mem(line);
    check(file, "Failed to open file: %s", filename);

    // read each line of the file and search that line for the contents
    while (fgets(line, MAX_LINE, file) != NULL && found == NULL) {
        for (i = 0; i < search_len && found == NULL; i++) {
            found = strcasestr(line, search_for[i]);
            if (found) {
                printf("%s\n", filename);
            }
        }
    }

    free(line);
    fclose(file);
    return 0;

error:
    if (line) free(line);
    if (file) fclose(file);

    return -1;
}


int main (int argc, char *argv[]) {
    int i = 0;
    glob_t files_found;
    check(argc > 1, "USAGE: logfind word word word.");

    check(list_file(&files_found) == 0, "Failed to list files.");

    for (i = 0; i < files_found.gl_pathc; i++) {
        scan_file(files_found.gl_pathv[i], argc, argv);
    }

    globfree(&files_found);
    return 0;

error:
    return 1;
}



