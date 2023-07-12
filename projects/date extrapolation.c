#include <string.h>
#include <stdio.h>

/*
 version 1: xiaojiao
*/
void print_caluator() {
    for (int i = 1; i <= 6; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d*%d=%d\t", j, i, i * j);
        }
        printf("\n");
    }
}



int main(int argc, char *argv[]) {

    // class text one
    // char string[13];
    // char string2[13];
    // scanf("%s", string);

    // printf("the input string is %s\n", string);
    

    // scanf("%s %[^\n]", string, string2);
    // printf("please input string2\n");
    // printf("the first string is %s\n", string);
    // printf("the second string is %s\n", string2);

    // class two
    int y, m, d, X;     // 定义存储的 年 月 日 和 X 的变量
    scanf("%d%d%d", &y, &m, &d); // 读入 年 月 日 
    scanf("%d", &X);        // 读入 X 值
    for (int i = 0; i < X; i++) {
        d += 1;
        switch(m) {
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:{
                if (d > 31) {   //第一部分逻辑
                    d = 1, m += 1;
                }
                if (m == 13) {
                    m = 1, y += 1;
                }
            } break;
            case 4:
            case 6:
            case 9:
            case 11:{
                if (d > 30) {   // 第二部分逻辑
                    d = 1;
                    m += 1;
                }
            } break;
            case 2:{
                if ((y % 4 == 0 && y % 100 != 0) || y % 400 == 0) {
                    if (d > 29) { d = 1; m += 1; }
                } else if (d > 28) {
                    d = 1, m += 1;
                }
            } break;

        }
    }

    printf("%d %d %d\n", y, m, d);


    return 0;
}
