/*
 * verion 01 :将字符打印到界面上
 * 
 *
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>  /* 需要使用System("cls")清屏函数 */
#include <conio.h>      /* 非标准函数，需要使用_getch()函数获取输入 */
#include <time.h>    /* 使用随机函数需要使用time()函数 */

/* 界面最大宽度和高度 */
#define MAXX 10000
#define MAXY 10000

void InitMap();                 /* initialize the background coordinate system */
void PrintMap();                /* print every point in the arr mapArr to the screen */
void StartMsg();                /* start message */
void GetSet();                  /* judge whether to edit the game setting */
void SetRandNum();              /* set a random 'food' point in the screen */
void SetSnakeNum();             /* the mopst complex and important algorithm of this game */
void EatFood();                  /* judge when to eat food and elongate the body */
void StartGame();               /* start the game */
void SetMoveNum();              /* algorithm of the start animation, some complex */
void JudgeEnd();                /* judge the end of the animation and loop again */
void StartView();               /* start the start animation view */

int speed = 10;                 /* default snake move speed */
int mapArr[MAXX][MAXY];         /* arr to store the point in the screen */
int inputX = 50, inputY = 20;   /* default width and height */
int randX = -1, randY = -1;     /* set a random food point in the background */
int foodFlag = 0;               /* judge when to change random food point */
int sx = 1, sy = 1;                     /* body x, y point */
int l = 0;                                      /* body length */
int *body[MAXX * MAXY];                 /* body array pointer */
char input = '6';                       /* default direction */
int overFlag = 1;                       /* judge when the game over, hit wall or eat self */
int moveX = 1, moveY = 1;               /* start move effect */
int moveFlag = 0;                       /* rrestart the loop effection */

void GetSet(){
    printf("\n");
    printf("请输入游戏空间的宽度:\n(Please input the width of game space:)\n");
    scanf("%d", &inputX);
    // 清空缓冲区
    getchar();
    printf("请输入游戏空间的高度:\n(Please input the height of game space:)\n");
    scanf("%d", &inputY);
    getchar();
    printf("请输入游戏速度(1到n,1最慢):\n Please input the speed of snake moving:(1 is slowest)\n");
    scanf("%d", &speed);
}

void InitMap(){
    int x, y;
    for( y = 0; y < inputY; y++){
        for(x = 0; x < inputX; x++){
            if((x==0) || (x== inputX -1) || (y == 0) || ( y == inputY - 1)){
                mapArr[x][y] = 1;
            }else{
                mapArr[x][y] = 0;
            }
        }
    }
}

void PrintMap(){
    int x, y;
    for(y = 0; y < inputY; y++){
        for(x = 0; x < inputX; x++){
            switch(mapArr[x][y]){
                case 0:
                    printf(" ");
                    break;
                case 1:
                    printf("+");
                    break;
                case 2:
                    printf("*");
                    break;
                case 3:
                    printf("@");
            }
        }
        printf("\n");
    }
}
int main(){
    GetSet();
    InitMap();
    PrintMap();
    return 0;
}









