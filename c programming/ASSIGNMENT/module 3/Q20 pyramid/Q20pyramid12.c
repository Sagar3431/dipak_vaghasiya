#include<stdio.h>
//Q12 pyramide (12).
/*
     1
   4 4
  9 9 9
 16 16 16 16
25 25 25 25 25

*/
void main()
{
    int i, j,k;
    for(i=1; i<=5; i++)
    {   for(k=1;k<=5-i;k++)
        {
        	printf(" ");
		}
        for(j=1; j<=i; j++)
        {
            printf("%d ", i*i);
        }
        printf("\n");
    }
}