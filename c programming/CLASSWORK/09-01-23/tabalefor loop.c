#include<stdio.h>

void main()

{
	int n,i;
	printf("Enter number :");
	scanf("%d",&n);
	for(i=1;i<=10;i++)
	{
		printf("%dx%d=%d\n",n,i,(i*n));
	}
}