#include<stdio.h>

void main()

{
	int a[6];
	int i;
	for(i=0;i<6;i++)
	{
		printf("Enter [%d]:",i);
		scanf("%d",&a[i]);
	}
	
	for(i=0;i<6;i++)
	{
		printf("%d\t",a[i]);
	}
}