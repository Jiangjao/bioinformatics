#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <conio.h>
#include <time.h>
#include <windows.h>

/* 在windows 上操作时，注意指定目录并且注意字符集合 */

//MAXWIDTH、MAXHEIGHT、INITLEN 以字符记
#define MAXWIDTH (30)
#define MAXHEIGHT MAXWIDTH
#define INITLEN (3)  //贪吃蛇的初始长度

//程序中用到的各种字符，以及它们的颜色和类型（以数字表示）
struct{
    char *ch;
    int color;
    char type;
}
charBorder = {"□", 4, 1},  //边框
charBg = {"■", 2, 2},  //背景
charSnake = {"★", 0xe, 3},  //贪吃蛇节点
charFood = {"●", 0xc, 4};  //食物

//用一个结构体数组保存地图中的各个点
struct{
    char type;
    int index;
}globalMap[MAXWIDTH][MAXHEIGHT];

//贪吃蛇有效活动范围地图的索引
struct{
    int x;
    int y;
} snakeMap[ (MAXWIDTH-2)*(MAXHEIGHT-2) ], scoresPostion;

// 🐍
struct Snake{
    int x;
    int y;
    int direction;  // 移动方向
    int size;       // 长度
} snake;

int scores = 0;  //得分
int snakeMapLen = (MAXWIDTH-2)*(MAXHEIGHT-2);
int headerIndex, tailIndex;  //蛇头蛇尾对应的snakeMap中的索引（下标）
HANDLE hStdin;  //控制台句柄

// 设置光标位置，x为行，y为列
void setPosition(int x, int y){
    COORD coord;
    coord.X = 2*y;
    coord.Y = x;
    SetConsoleCursorPosition(hStdin, coord);
}

// 设置颜色
void setColor(int color){
    SetConsoleTextAttribute(hStdin, color);
}

//创建食物
void createFood(){
    int index, rang, x, y;
    //产生随机数，确定 snakeMap 数组的索引 
    srand((unsigned)time(NULL));
    if(tailIndex<headerIndex){
        rang = headerIndex-tailIndex-1;
        index = rand()%rang + tailIndex + 1;
    }else{
        rang = snakeMapLen - (tailIndex - headerIndex+1);
        index = rand()%rang;
        if(index>=headerIndex){
            index += (tailIndex-headerIndex+1);
        }
    }

    x = snakeMap[index].x;
    y = snakeMap[index].y;
    setPosition(x, y);
    setColor(charFood.color);
    printf("%s", charFood.ch);
    globalMap[x][y].type=charFood.type;
}

//死掉
void die(){
    int xCenter = MAXHEIGHT%2==0 ? MAXHEIGHT/2 : MAXHEIGHT/2+1;
    int yCenter = MAXWIDTH%2==0 ? MAXWIDTH/2 : MAXWIDTH/2+1;

    setPosition(xCenter, yCenter-5);
    setColor(0xC);

    printf("You die! Game Over!");
    getch();
    exit(0);
}

// 蛇移动
void move(char direction){
    int newHeaderX, newHeaderY;  //新蛇头的坐标
    int newHeaderPreIndex;  //新蛇头坐标以前对应的索引
    int newHeaderPreX, newHeaderPreY;  //新蛇头的索引以前对应的坐标
    int newHeaderPreType;  //新蛇头以前的类型
    int oldTailX, oldTailY;  //老蛇尾坐标
    // -----------------------------------------------
    //新蛇头的坐标
    switch(direction){
        case 'w':
            newHeaderX = snakeMap[headerIndex].x-1;
            newHeaderY = snakeMap[headerIndex].y;
            break;
        case 's':
            newHeaderX = snakeMap[headerIndex].x+1;
            newHeaderY = snakeMap[headerIndex].y;
            break;
        case 'a':
            newHeaderX = snakeMap[headerIndex].x;
            newHeaderY = snakeMap[headerIndex].y-1;
            break;
        case 'd':
            newHeaderX = snakeMap[headerIndex].x;
            newHeaderY = snakeMap[headerIndex].y+1;
            break;
    }
    //新蛇头的索引
    headerIndex = headerIndex==0 ? snakeMapLen-1 : headerIndex-1;
    // -----------------------------------------------
    //新蛇头坐标以前对应的索引
    newHeaderPreIndex = globalMap[newHeaderX][newHeaderY].index;
    //新蛇头的索引以前对应的坐标
    newHeaderPreX = snakeMap[headerIndex].x;
    newHeaderPreY = snakeMap[headerIndex].y;

    //双向绑定新蛇头索引与坐标的对应关系
    snakeMap[headerIndex].x = newHeaderX;
    snakeMap[headerIndex].y = newHeaderY;
    globalMap[newHeaderX][newHeaderY].index = headerIndex;

    //双向绑定以前的索引与坐标的对应关系
    snakeMap[newHeaderPreIndex].x = newHeaderPreX;
    snakeMap[newHeaderPreIndex].y = newHeaderPreY;
    globalMap[newHeaderPreX][newHeaderPreY].index = newHeaderPreIndex;

    //新蛇头以前的类型
    newHeaderPreType = globalMap[newHeaderX][newHeaderY].type;
    //设置新蛇头类型
    globalMap[newHeaderX][newHeaderY].type = charSnake.type;
    // 判断是否出界或撞到自己
    if(newHeaderPreType==charBorder.type || newHeaderPreType==charSnake.type ){
        die();
    }
    //输出新蛇头
    setPosition(newHeaderX, newHeaderY);
    setColor(charSnake.color);
    printf("%s", charSnake.ch);
    //判断是否吃到食物
    if(newHeaderPreType==charFood.type){  //吃到食物
        createFood();
        //更改分数
        setPosition(scoresPostion.x, scoresPostion.y);
        printf("%d", ++scores);
    }else{
        //老蛇尾坐标
        oldTailX = snakeMap[tailIndex].x;
        oldTailY = snakeMap[tailIndex].y;
        //删除蛇尾
        setPosition(oldTailX, oldTailY);
        setColor(charBg.color);
        printf("%s", charBg.ch);
        globalMap[oldTailX][oldTailY].type = charBg.type;
        tailIndex = (tailIndex==0) ? snakeMapLen-1 : tailIndex-1;
    }
}

//下次移动的方向
char nextDirection(char ch, char directionOld){
    int sum = ch+directionOld;
    ch = tolower(ch);
    if( (ch=='w' || ch=='a' || ch=='s' || ch=='d') && sum!=197 && sum!=234 ){
        return ch;
    }else{
        return directionOld;
    }
}

//暂停
char pause(){
    return getch();
}

// 初始化
void init(){
    // 设置相关变量
    int x, y, i, index;
    int xCenter = MAXHEIGHT%2==0 ? MAXHEIGHT/2 : MAXHEIGHT/2+1;
    int yCenter = MAXWIDTH%2==0 ? MAXWIDTH/2 : MAXWIDTH/2+1;
    CONSOLE_CURSOR_INFO cci;  //控制台光标信息

    //判断相关设置是否合理
    if(MAXWIDTH<16){
        printf("'MAXWIDTH' is too small!");
        getch();
        exit(0);
    }

    //设置窗口大小
    system("mode con: cols=96 lines=32");

    //隐藏光标
    hStdin = GetStdHandle(STD_OUTPUT_HANDLE);
    GetConsoleCursorInfo(hStdin, &cci);
    cci.bVisible = 0;
    SetConsoleCursorInfo(hStdin, &cci);

    //打印背景
    for(x=0; x<MAXHEIGHT; x++){
        for(y=0; y<MAXWIDTH; y++){
            if(y==0 || y==MAXWIDTH-1 || x==0 || x==MAXHEIGHT-1){
                globalMap[x][y].type = charBorder.type;
                setColor(charBorder.color);
                printf("%s", charBorder.ch);
            }else{
                index = (x-1)*(MAXWIDTH-2)+(y-1);
                snakeMap[index].x= x;
                snakeMap[index].y= y;
                globalMap[x][y].type = charBg.type;
                globalMap[x][y].index = index;

                setColor(charBg.color);
                printf("%s", charBg.ch);
            }
        }
        printf("\n");
    }

    //初始化贪吃蛇
    globalMap[xCenter][yCenter-1].type = globalMap[xCenter][yCenter].type = globalMap[xCenter][yCenter+1].type = charSnake.type;

    headerIndex = (xCenter-1)*(MAXWIDTH-2)+(yCenter-1) - 1;
    tailIndex = headerIndex+2;
    setPosition(xCenter, yCenter-1);
    setColor(charSnake.color);
    for(y = yCenter-1; y<=yCenter+1; y++){
        printf("%s", charSnake.ch);
    }
    //生成食物
    createFood();

    //设置程序信息
    setPosition(xCenter-1, MAXWIDTH+2);
    printf("   Apples : 0");
    setPosition(xCenter, MAXWIDTH+2);
    printf("   Author : xiao p");
    setPosition(xCenter+1, MAXWIDTH+2);
    printf("Copyright : c.biancheng.net");
    scoresPostion.x = xCenter-1;
    scoresPostion.y = MAXWIDTH+8;
}

int main(){
    char charInput, direction = 'a';
    init();

    charInput = tolower(getch());
    direction = nextDirection(charInput, direction);

    while(1){
        if(kbhit()){
            charInput = tolower(getch());
            if(charInput == ' '){
                charInput = pause();
            }
            direction = nextDirection(charInput, direction);
        }
        move(direction);
        Sleep(500);
    }

    getch();
    return 0;
}
