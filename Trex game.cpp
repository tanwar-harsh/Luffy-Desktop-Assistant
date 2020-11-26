#include <conio.h>
#include <windows.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void gotoxy(int eex , int eey)
 {
   COORD coord;
   coord.X=eex;
   coord.Y=eey;
   SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
 }
///////////////////////////////////////////////////////////////////////////////

 int scr=0,rn,p,q,l,d,m,k,j,x, y, lastx, lasty,lastp,lastq, choice;
 float t=40;
 char a;
 static int hscr=0;

///////////////////////////////////////////////////////////////////////////////

 void delay(unsigned int mseconds)
 {
     clock_t goal = mseconds + clock();
     while (goal > clock());
 }

 ///////////////////////////////////////////////////////////////////////////////
 void ground()
 {
   system("cls");                                 //clear screen
    gotoxy(2,2);
          printf("Press x to exit    Press space to jump");
   gotoxy(1,11);
          printf("____________________________________________________________________________________________________________________________________________________________");
 }

///////////////////////////////////////////////////////////////////////////////

void menu();

///////////////////////////////////////////////////////////////////////////////

 void bgm()
  {
    if(p<=1)
      { rn=rand()%(3-1) +1;
        p=65;
      }
    else
      for(l=2;l>=1;l--)
        {                     delay(t);
           p=p-1;
          gotoxy(lastp,lastq);
          printf(" ");

          gotoxy(p,q);
          printf("X");

           lastp=p;
           lastq=q;

           if(x==p&&y==q)
             {
               gotoxy(35,5);
               printf("GAME OVER");
                delay(1000);
                menu();
             }
            else if(x==p&&y!=q)
              {
                scr++;
                if(scr>hscr)
                hscr++;
                t=t-0.5;
              }
           gotoxy(50,2);
           printf("highscore : %d  scrore : %d",hscr,scr);

      }
  }

///////////////////////////////////////////////////////////////////////////////
void game()
 {
   x = 10 , y = 10;
   lastx = x ; lasty = y ;
   p = 65  , q = 10;
   lastp = p ; lastq = q ;


   while(1==1)
   {
    gotoxy(lastx,lasty);
     printf(" ");

    gotoxy(x,y);
     printf("@");

      gotoxy(lastp,lastq);
       printf(" ");

      gotoxy(p,q);
       printf("X");


      lastp=p;
      lastq=q;

    a=getch();

     lastx=x;
     lasty=y;

    if(a==32)
      {

              for(j=1;j<5;j++)
                {

                     y=y-1;

                     gotoxy(lastx,lasty);
                     printf(" ");

                     gotoxy(x,y);
                     printf("@");



                     lastx=x;
                     lasty=y;
                                           bgm(); // x movement


                }

                if(j==5)
                 {
                  for( k=5 ;k>1;k--)
                    {

                            y=y+1;

                            gotoxy(lastx,lasty);
                            printf(" ");

                            gotoxy(x,y);
                            printf("@");



                            lastx=x;
                            lasty=y;
                                                  bgm(); //x movment
                     }
                 }


        }
          while(!kbhit())
              {
                bgm();

              }

              if(a==120)
                 {
                   delay(500);
                   menu();
                 }
      }

 }




 int main()
{

  menu();



}

void menu()
{
  system("cls");                                    //clear screen
  gotoxy(35,3);
  printf("GAME");
gotoxy(20,6);
  printf("1. start");
gotoxy(20,7);
  printf("2. exit");
gotoxy(30,15);
  printf("ENTER YOUR OPTION  ");
scanf("%d",&choice);

if(choice==1)
     {  scr=0;
        ground();
        game();
     }

 else if(choice==2)
        {
          exit(0);
        }
}