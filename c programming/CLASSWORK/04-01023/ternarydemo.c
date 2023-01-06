#include<stdio.h>

/*
	ternary operator     (condition)?True:False
*/

void main()
{
	int //a=64,b=54;
	 a,b;
	printf("Enter is value A=");
	scanf("%d",&a);
	printf("\nEnter is value B=");
	scanf("%d",&b);
	
	(a<b)?printf("A is Greater"):printf("B is Greater");
}