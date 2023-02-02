#include<stdio.h>
/*   
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
*/    
int main()
{
int i, j, k, m = 8;
for(i = 1;i <= 5;i++)
{
for(j = 5;j > i;j--)
{
printf(" ");
}
for(k = 1;k <= ((j*2)-1);k++)
{
printf("*");
}
printf("\n");
}
for(i = 1;i <= 4;i++)
{
for(j = 1;j <= i;j++)
{
printf(" ");
}
for(k = i;k < m;k++)
{
printf("*");
}
m-=1;
printf("\n");
}
return 0;
}