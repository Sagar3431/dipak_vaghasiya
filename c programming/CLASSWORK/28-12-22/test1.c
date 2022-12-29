#include<stdio.h>


void main()

{
	int a,b;
	printf("\nEnter a:");
	scanf("%d",&a);
	printf("\nEnter b:");
	scanf("%d",&b);
	printf("A= %d B= %d",a,b);
	
	
	if(a>0)
	{
		printf("\n%d is positive value",a);

	}
	else
	{
		printf("\n%d is nagative value",a);
	}
	
	printf("\nOutside is block");
	
}