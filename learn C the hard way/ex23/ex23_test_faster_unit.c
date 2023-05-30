#include <stdio.h>
#include <string.h>
#include "dbg.h"
#include <time.h>
#include <assert.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

int frequency = 1;
typedef int (Function_test)(char *from, char *to, int count);

void die(const char *message) {
    if (errno) {
        perror(message);
    } else {
        printf("ERROR: %s \n", message);
    }
    exit(1);
}

int normal_copy(char *from, char *to, int count) {
    int i = 0;

    for (i = 0; i < count; i++) {
        to[i] = from[i];
    }

    return i;
}

int duffs_device(char *from, char *to, int count) {
    {
        int n = (count + 7) / 8;

        switch(count % 8) {
            case 0: do {
                *to ++ = *from ++;
                case 7: *to ++ = *from ++;
                case 6: *to ++ = *from ++;
                case 5: *to ++ = *from ++;
                case 4: *to ++ = *from ++;
                case 3: *to ++ = *from ++;
                case 2: *to ++ = *from ++;
                case 1: *to ++ = *from ++;
            } while( --n > 0);
        }
    }

    return count;
}


int zeds_device(char *from, char *to, int count) {
    {
        int n = (count + 7) / 8;
        
        switch(count % 8) {
            case 0:
            again:  *to ++ = *from ++;

            case 7: *to ++ = *from ++;
            case 6: *to ++ = *from ++;
            case 5: *to ++ = *from ++;
            case 4: *to ++ = *from ++;
            case 3: *to ++ = *from ++;
            case 2: *to ++ = *from ++;
            case 1: *to ++ = *from ++;
                    if (--n > 0) goto again;
        }
    }

    return count;
}

int valid_copy(char *data, int count, char expects) {
    int i = 0;
    for (i = 0; i < count; i++) {
        if (data[i] != expects) {
            log_err("[%d] %c != %c", i, data[i], expects);
            return 0;
        }
    }

    return 1;
}

double function_finished_cost_with_average_seconds(Function_test *function, char *data, char *expects, int count) {
    clock_t start_time, end_time;
    double total_time = 0;
    // double time_used;
    
    for (int i = 0; i < frequency; i++) {
        start_time = clock();  // 记录开始时间
        function(data, expects, count);  // 运行需要统计时间的函数
        end_time = clock();  // 记录结束时间
        total_time += (double)(end_time - start_time) / CLOCKS_PER_SEC;  // 累加时间差
    }
    // count the average time
    double average_time = total_time / count;  

    printf("程序运行%d次的平均时间:%.15f 秒\n", frequency, average_time);
    return average_time;
}

int main(int argc, char *argv[]) {
    char from[1000] = {'a'};
    char to[1000] = {'c'};
    int rc = 0;
    frequency = 1000;
    // setup the from to have some stuff
    memset(from, 'x', 1000);

    // set it to a failure mode
    memset(to, 'y', 1000);

    check(valid_copy(to, 1000, 'y'), "Not initialized right.");

    // use normal copy to
    rc = normal_copy(from, to, 1000);
    check(rc == 1000, "Normal copy failed:%d", rc);
    check(valid_copy(to, 1000, 'x'), "Normal copy failed");

    // reset
    memset(to, 'y', 1000);

    // duffs version
    rc = duffs_device(from, to, 1000);
    check(rc = 1000, "Duff's devicce failed:%d", rc);
    check(valid_copy(to, 1000, 'x'), "Duff's device failed copy.");

    // reset
    memset(to, 'y', 1000);

    // my version
    rc = zeds_device(from , to, 1000);
    check(rc = 1000, "Zed's device failed: %d", rc);
    check(valid_copy(to, 1000, 'x'), "Zed's devicce failed copy.");

    double time_used_normal_copy;
    double time_used_duffs_device;
    double time_used_zeds_device;


    if (argc > 1){
        frequency = atoi(argv[1]);
    } 
    // if (id >= MAX_ROWS) die("There's not that many records.", conn);

    char action = argv[2][0];

    printf("action %c\n", action);

    // ./ex23_test_faster_unit 100000 c

    if (argc > 3) die("USAGE: ex23_test_faster_unit <count> <action> [action params]");

    switch(action) {
        case 'c':
            // reset
            memset(to, 'y', 1000);
            printf("%s", "normal_copy");
            time_used_normal_copy = function_finished_cost_with_average_seconds(normal_copy, from, to, 1000);
            break;
        
        case 'g':
            // reset
            memset(to, 'y', 1000);
            printf("%s", "duffs_device");
            time_used_duffs_device = function_finished_cost_with_average_seconds(duffs_device, from, to, 1000);
            break;
        
        case 's':
            // reset
            memset(to, 'y', 1000);
            printf("%s", "zeds_device");
            time_used_zeds_device = function_finished_cost_with_average_seconds(zeds_device, from, to, 1000);
            break;

        // case 'l':
        //     Database_list(conn);
        //     break;
        default:
            die("Invalid action, only: c=normal_copy, g=duffs_device, s=zeds_device, l=list");   
    }



    
    return 0;
error:
    return 1;
}





