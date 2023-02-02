#include<stdio.h>
//A6. Write a program to print the Matrixusing 2-D Array
void main()

{
	int matrix1[3][3];
	int i,j;
	
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("Enter Element[%d][%d] :",i,j);
			scanf("%d",&matrix1[i][j]);
		}
		printf("\n");
	}
	        printf("\n============================================\n");
		for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("value at index[%d][%d] : %d\n",i,j,matrix1[i][j]);
		}
	}
}