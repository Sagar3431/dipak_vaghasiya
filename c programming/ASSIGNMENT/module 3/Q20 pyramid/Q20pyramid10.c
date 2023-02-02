#include<stdio.h>
//Q20 pyramide (10)
/*
    1
   2 3
  4 5 6
 7 8 9 10
11 12 13 14 15
*/
int main()
{
    int i,j,k,n;
    
    // 'count' variable to count the numbers
    int count=0;
    
    // Take input from the user. Num of rows to print
    printf("Enter how many rows you want : ");
    scanf("%d",&n);
    
    // Loop until we reach row value
    for(i=1;i<=n;i++)
    {    for(k=1;k<=5-i;k++)
        {
        	printf(" ");
		}
        for(j=1;j<=i;j++)
        {
            // At each number, Increase the value of 'count' and display
            count++;
            printf("%d ",count);
        }
        
        printf("\n");
    }
    return 0;
}