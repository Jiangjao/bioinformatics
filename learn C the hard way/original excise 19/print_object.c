#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <time.h>

// author:xiaojiao
// version 01

typedef struct {
    int x;
    int y;
    void (*print)(void *self);
    void (*init)(void *self, int x, int y);
    void (*destroy)(void *self);
} Point;

void die(const char *message) {
    if (errno) {
        perror(message);
    } else {
        printf("ERROR:%s\n", message);
    }
    exit(1);
}

void print_location(void *self) {
    Point *point = self;
    printf("point.x is %d, point.y is %d\n", point->x, point->y);
}

void init(void *self, int x, int y) {
    Point *point = self;
    point->x = x;
    point->y = y;
}

void destroy(void *self) {
    Point *point = self;
    free(point);
}

int main(int argc, char *argv[]) {
    Point *point = malloc(sizeof(Point));
    // the result is same
    point->print = print_location;
    point->init = init;
    point->destroy = destroy;
    // point->print = &print_location;
    // point->x = 0;
    // point->y = 0;
    point->init(point, 1, 2);
    point->print(point);
    point->destroy(point);
    return 0;
}

// UML
// //www.plantuml.com/plantuml/png/VP31JiCm343l-GeVcwhxWOd3a7P4uWCGchp4WA599iSC5V7nDBIbH9KuH4dydkFOXwme-XvwStz-9QTmyxNRmQq83dUSrIpXFN3KSR4sryGUsapzarsfUq61rbDsmXVb55Vquq_aJ9liIj4ampz66zAL_l0EZYpaIZdmoydMNqPLT6zLKWbx3FXCcmBJzHJfeydyIIU5idKmQnT9chfjizRyJWpsi_pm2DHJeAX7LAo4ycPZpO6Y7oV_3G00

// version 01
// //http://www.plantuml.com/plantuml/png/VP3HJiCW68NlUGekMsnVG1Cp4vTuPOsjyN9Xb2dQWe6_CsfyTu7oJvfbwqr_u7m7pbavu1QcSI1IJoEzLLOAK4RJ7qBzTzyyTdTL7Dlc2SVrJTlDq_EwxSWl8Gxi980sspUF9rQySajPBvsmwYDuNiLjfO4MJ6a5PR4tggVCoM5NpeTneqZGLfvLW3LVfmIiOAFPB_Wg2zVZLEPluW1Sl2-PSDBpaRz8B_L1nS2TIpatMdwch1V_EuLJtt83LH8zM0EcYcMmyZA-ZWMZpAAkhtCn8VvIQNTSIBp8juMjrc6EJmnsNkdDZe5K3p9fUS32VyaXYCqZYUlJA9AXRwJ2F1DPwrdwOthk7lbvXGvUV8YwahgVnk4F

