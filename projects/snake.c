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

void StartMsg(){
    printf(
        "'2(top)', '8(top)', '4(left)', '6(right)'\n"
    );
    printf("或'w(top)', 'a(left)', 's(down)', 'd(right)'\n");
    printf("控制方向(control the direction)\n");
}

void SetRandNum(){
    srand(time(0));
    while((mapArr[randX + 1][randY + 1] != 0) && (foodFlag == 0)){
        randX = rand() % (inputX - 2), randY = rand() % (inputY - 2);
    }
    mapArr[randX + 1][randY + 1] = 3;           /* set food number 3 */
    foodFlag = 1;
}

void SetSnakeNum(){
    /* if there is an input , get it;if not, go on */
    if(_kbhit()){
        int a = _getch();
        switch(input){
            case '2':
            case 'w':
                if(a == '4' || a == '6' || a == 'a' || a == 'd' || a == '2' || a == 'w'){
                    input = a;
                }
                break;

            case '8':
            case 's':
                if(a == '4' || a == '6' || a == 'a' || a == 'd' || a == '8' || a == 's'){
                    input = a;
                }
                break;

            case '4':
            case 'a':
                if(a == '2' || a == '8' || a == 'w' || a == 's' || a == '4' || a == 'a'){
                    input = a;
                }
                break;

            case '6':
            case 'd':
                if(a == '2' || a == '8' || a == 'w' || a == 's' || a == '6' || a == 'd'){
                    input = a;
                }
                break;
        }
    }
    /* judge the direction by value of input */
    switch(input){
        case '2':
        case 'w':
            sy--;
            break;
        case '8':
        case 's':
            sy++;
            break;
        case '4':
        case 'a':
            sx--;
            break;
        case '6':
        case 'd':
            sx++;
            break;
    }
    int i;
    /* every point's address of body move back one point */
    for(i = 1; i != 0; i--){
        body[i] = body[i - 1];
        *body[i] = 2;
    }
    body[0] = &mapArr[sx][sy];
    /* judge when the snake hit the wall or eat itself */
    if((*body[0] == 1) || (*body[0] == 2)){
        overFlag = 0;
    }
    /* assign the head of snake by pointer */
    *body[0] = 2;
}

void EatFood(){
    if(*body[0] == 3){
        l++;
        foodFlag = 0;
    }
}

void StartGame(){
    sx = 1;
    sy = 1;
    l = 0;
    input = '6';
    int j;
    /* assign the snake body initial address value */
    for(j = 0; j < l; j++){
        body[j] = &mapArr[sx - j][sy];
    }
    /* loop until the game over */
    while(overFlag){
        InitMap();
        SetSnakeNum();
        SetRandNum();
        EatFood();
        PrintMap();
        StartMsg();
        Sleep(1000/speed);
        system("cls");
    }
}

void SetMoveNum(){
    /* x move 1-- (X - 2); y mpve 1 -- (Y -2) */
    /* move y from top to buttom */
    if((moveY == 1 + moveFlag) && (moveX < inputX - 2 - moveFlag)){
        mapArr[moveX][moveY] = 2;
        moveX ++;
    /* move y from top to buttom */
    }else if ((moveX == inputX -2 - moveFlag) && (moveY < inputY - 2)){
        mapArr[moveX][moveY] = 2;
        moveY ++;
    /* move x from right to left */
    } else if((moveY == inputY - 2 - moveFlag) && (moveX > 1 + moveFlag)){
        mapArr[moveX][moveY] = 2;
        moveX --;
    /* move y from buttom to top */
    } else if((moveX == 1 + moveFlag) && (moveY > 1 + moveFlag)){
        mapArr[moveX][moveY] = 2;
        moveY --;
        if(moveY == 2 + moveFlag){  // judge when jump to the deeper layer
            moveFlag ++;
        }
    }
}

void JudgeEnd(){
    int i, j;
    int tmp = 1;
    for(j = 0; j <inputY; j++){
        for(i = 0;i < inputX; i++){
            if(mapArr[i][j] == 0){
                goto out;
            }
        }
    }
    moveX = 1, moveY = 1;
    InitMap();
    moveFlag = 0;
out:;
}

void StartView()
{
	moveX = 1, moveY = 1, moveFlag = 0;
	int startFlag = 1;
	InitMap();
	while (startFlag)
	{
		SetMoveNum();
		PrintMap();
		printf("按任意键开始游戏：\n(Press any key to start game: )\n");
		Sleep(10);
		system("cls");
		JudgeEnd();
		if (_kbhit())
		{
			int c = _getch();
			if ((c != '2') && (c != 'w') && (c != '8') && (c != 's') && (c != '4') && (c != 'a') && (c != '6') && (c != 'd'))
				startFlag = 0;
		}
	}
}

int main(){
    // GetSet();
    // InitMap();
    // PrintMap();
    // StartMsg();
    // SetRandNum();
    // SetSnakeNum();
    while(1){
        printf("是否修改设置（修改设置输入'y',否则按任意键):\nEdit the game setting or not? (Press 'y' to edit , or press another key to go on:)\n");
        if(_getch() == 'y'){
            GetSet();
        }
        StartView();
        StartGame();
        printf("Game over !!!\n游戏结束, 按任意键继续:\n(Press any key to quit!!!\n)");
        _getch();
        overFlag = 1;   /* restart the game by the flag */
        system("cls");
    }
    return 0;
}









