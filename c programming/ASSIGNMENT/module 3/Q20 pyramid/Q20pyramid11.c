#include<stdio.h>
//Q20 pyramid (11)
/*
     1
    0 1
   0 1 0
  1 0 1 0
 1 0 1 0 1
0 1 0 1 0 1
*/
int main()
{
    int i,j,b,n;
    
    // Take the number of rows as the input
    printf("Enter how many rows you want : ");
    scanf("%d",&n);
    
    // Lets start with 1
    // After printing the value then Negate the value '!'
    int k=1;
    
    // The Outer loop goes from 1 to n
    // So It is the number of Rows
    for(i=0;i<=n;i++)
    {   for(b=1;b<=5-i;b++)
         {
         	printf(" ");
		 }
        // Our Pattern is in Triangle Shape
        // So we need to stop the loop when i and j becomes equal
        // Start j from 1 and go until we reach 'i'
        for(j=0;j<=i;j++)
        {
            // Print the value
            printf("%d ",k);
 
            // Now Negate the value.
            k=!k;
        }
 
        printf("\n");
    }
 
    return 0;
}
