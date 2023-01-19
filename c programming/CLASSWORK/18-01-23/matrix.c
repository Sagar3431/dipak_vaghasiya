#include<stdio.h>
void main()

{
	int matrix1[3][3];
	int i,j;
	
	printf("\n\n\t\t\t\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Enter matrix1 \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
		for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\t\t\t\t\tEnter Element[%d][%d] :",i,j);
			scanf("%d",&matrix1[i][j]);
	    }	
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
}