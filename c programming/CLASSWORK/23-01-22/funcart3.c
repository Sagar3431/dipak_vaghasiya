#include<stdio.h>

int add(int d,int g)
{
	printf("\n Inside UFD A = %d, B = %d",d,g);
	return d+g;
}
void main()
{
	int a,b,sum;
	printf("\n Enter A :");
	scanf("%d",&a);
	printf("\n Enter B :");
	scanf("%d",&b);
	printf("\n A = %d,B = %d",a,b);
	sum=add(a,b);
	printf("\nAddition : %d",sum);
	if(sum%2==0)
	{
		printf("\n sum is Even.");
	}
	else 
	{
		printf("\n sum is odd.");
	}
}