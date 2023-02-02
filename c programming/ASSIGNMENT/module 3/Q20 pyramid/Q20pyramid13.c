#include<stdio.h>

/*
Q20.pyiramide(13)
*
**
***
****
*****
******
*******
********
*********
**********
**********
*********
********
*******
******
*****
****
***
**
*
*/

int main()
{
int n, i , j;
printf("Enter number of rows: ");
scanf("%d",&n);
for(i = 1; i <= n; i++)
{
for(j = 1; j <= i; j++)
{
printf("*");
}
printf("\n");
}
for(i = n; i >= 1; i--)
{
for(j = 1; j <= i; j++)
{
printf( "*");
}
// ending line after each row
printf("\n");
}

}