#include<stdio.h>
//Q20 pyramid (7)
/*        *
        * *
      * * *
    * * * *
  * * * * *
*/  
int main()
{
    int i, j, space=8;
    for(i=0; i<5; i++)
    {
        for(j=0; j<space; j++)
            printf(" ");
        space = space-2;
        for(j=0; j<=i; j++)
            printf("* ");
        printf("\n");
    }
   
}