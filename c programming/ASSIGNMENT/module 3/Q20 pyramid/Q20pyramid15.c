#include<stdio.h>
/*
**********
****  ****
***    ***
**      **
*        *
*/
int main()
{
int i, j, k, m, a = 1;
for(i = 5;i > 0;i--)
{
for(j = i;j > 0;j--)
{
printf("*");
}
for(k = 1;k < a;k++)
{
printf(" ");
}
a = a + 2;
for(m = i;m > 0;m--)
{
printf("*");
}
printf("\n");
}
return 0;
}