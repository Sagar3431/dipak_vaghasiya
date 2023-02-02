#include<stdio.h>
//f. Write aprogramyouhave to printthe table of givennumber
int main()

{
	int num , i;
	printf("\nEnter num of table c:");
	scanf("%d",&num);
	printf("\n Table of %d",num);
	
	for ( i = 1; i <= 10; i++)  
    {  
        printf ("\n %d * %d = %d", num, i, (num*i));  
    }  
    return 0;

}