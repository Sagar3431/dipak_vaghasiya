#include<stdio.h>

int main()

{
	int arr1[3],arr2[3];
	int i;
	printf("\nEnter array 1: \n\n");
	for(i=0;i<3;i++)
	{
		printf("enter Element [%d] :",i);
		scanf("%d",&arr1[i]);
		
	}
		printf("\nEnter array 2: \n\n");
	for(i=0;i<3;i++)
	{
		printf("enter Element [%d] :",i);
		scanf("%d",&arr2[i]);
		
	}
	printf("\nArrey 1: \n\n");
	for(i=0;i<3;i++)
	{
		printf("Element at index[%d] = %d\n",i,arr1[i]);
	}
		printf("\nArrey 2: \n\n");
	for(i=0;i<3;i++)
	{
		printf("Element at index[%d] = %d\n",i,arr2[i]);
	}
	printf("===============================\n");
	printf("\nAddition of arr1 and arr2 :\n\n");
	for(i=0;i<3;i++)
	{
		printf("\naddtion of array [%d] : %d",i,arr1[i]+arr2[i]);
	}
	printf("\n===============================\n");
	printf("\nsubtract of arr1 and arr2 :\n\n");
	for(i=0;i<3;i++)
	{
		printf("\nsubtract of array [%d] : %d",i,arr1[i]-arr2[i]);
	}
	printf("\n===============================\n");
	printf("\nmultiply of arr1 and arr2 :\n\n");
	for(i=0;i<3;i++)
	{
		printf("\nmultiply of array [%d] : %d",i,arr1[i]*arr2[i]);
	}

}