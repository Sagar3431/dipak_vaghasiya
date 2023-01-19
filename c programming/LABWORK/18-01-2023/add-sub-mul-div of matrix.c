#include<stdio.h>

void main()
{
	int a[3][3],b[3][3];
	int i,j;
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Enter A \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\n\t\tEnter elament [%d][%d] :",i,j);
			scanf("%d",&a[i][j]);
		}
		printf("\n");
	}
    printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Enter B \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\n\t\tEnter elament [%d][%d] :",i,j);
			scanf("%d",&b[i][j]);
		}
		printf("\n");
	}
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Display A \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\n\t\tValue at index : %d",a[i][j]);
		}
		printf("\n");
	}
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Display B \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\n\t\tValue at index : %d",b[i][j]);
		}
		printf("\n");
	}
		printf("\n\n\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 ADDITION BETWEEN OF A AND B : \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\n\t\t Addition of A and B : %d",a[i][j]+b[i][j]);
		}
		printf("\n");
	}
	printf("\n\n\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 SUBTRACTION BETWEEN OF A AND B : \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\n\t\t Subtraction of A and B : %d",a[i][j]-b[i][j]);
		}
		printf("\n");
	}
	printf("\n\n\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 MULTIPLICATION BETWEEN OF A AND B : \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\n\t\t Mulipliction of A and B : %d",a[i][j]*b[i][j]);
		}
		printf("\n");
	}
	printf("\n\n\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 DIVISION BETWEEN OF A AND B : \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\n\t\t Division of A and B : %.2f",(float)a[i][j]/b[i][j]);
		}
		printf("\n");
	}
}