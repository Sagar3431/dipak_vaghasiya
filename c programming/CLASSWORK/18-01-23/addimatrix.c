#include<stdio.h>

void main()

{
	int matrix1[3][3],matrix2[3][3];
	int i,j;
	printf("\n\n\t\t\t\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Enter matrix1 \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
		for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\t\t\t\tEnter Element[%d][%d] :",i,j);
			scanf("%d",&matrix1[i][j]);
	    }
		printf("\n");	
	}
	printf("\n\n\t\t\t\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Enter matrix2 \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
		for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\t\t\t\tEnter Element[%d][%d] :",i,j);
			scanf("%d",&matrix2[i][j]);
	    }
	    printf("\n");
    }
			printf("\n\n\t\t\t\t\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 matrix1 \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\tvalue at index : %d",matrix1[i][j]);
		}
		printf("\n");
	}	
		printf("\n\n\t\t\t\t\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 matrix2 \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\tvalue at index : %d",matrix2[i][j]);
		}
		printf("\n");
	}
	
			printf("\n\n\t\t\t\t\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 addition of matrix1 and matrix2 \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\taddition of matrix 1+ matrix2  : %d",(matrix1[i][j]+matrix2[i][j]));
		}
		printf("\n");
	}	
	
}