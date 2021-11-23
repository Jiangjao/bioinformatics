
/* 循环函数，结构体，数组 */

#include <stdio.h>
#include <conio.h>
#include <windows.h>
// 做界面1, 创建一个窗口，图形窗口

void initGraphic(){
    /* 宽和 高 */
    int width = 50, height = width;
    /* 行和列 */
    int x, y;
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);

    // 设置窗口大小
    system("mode con:cols=64 lines=32");

    // 打印背景
    for(x=0; x<width; x++){
        for(y=0; y <height; y++){
            if(y==0 || y == width-1 || x == 0 || x == height -1){
                SetConsoleTextAttribute(hConsole, 4);
                printf("□");
            }else{  //贪吃蛇活动区域
                SetConsoleTextAttribute(hConsole, 2 );
                printf("■");
            }
        }
        printf("\n");
    }
    // 暂停
    getch();

}
int main(){
    // init graphic 图形窗口
    initGraphic();

    return 0;
}
