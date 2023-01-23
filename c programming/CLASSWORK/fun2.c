#include<stdio.h>

void add(int x,int y)
{
	printf("\nInside udf X=%d, y=%d",x,y);
	printf("\nAddition : %d",(x+y));
}
void main()
{
	int a,b;
	printf("\nEnter A :");
	scanf("%d",&a);
	printf("\nEnter B :");
	scanf("%d",&b);
	printf("\nstart function");
	add(a,b);
	printf("\nstop function");
	
}