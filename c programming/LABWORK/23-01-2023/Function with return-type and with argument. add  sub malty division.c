#include<stdio.h>

int add(int d,int g)
{
	printf("\n Inside UDF A = %d, B = %d",d,g);
	printf("\nAddition");
	return d+g;
}
int sub(int d,int g)
{
	printf("\n Inside UFD UDF A = %d, B = %d",d,g );
	printf("\nSubtraction");
	return d-g;
}
int multy(int d,int g)
{
	printf("\n Inside UFD UDF A = %d, B = %d",d,g );
	printf("\nMultipliction");
	return d*g;
}
int div(int d,int g)
{
	printf("\n Inside UFD UDF A = %d, B = %d",d,g );
	printf("\nDivision");
	return d/g;
}
void main()
{
	int a,b,sum,choice;
	printf("\n Enter A :");
	scanf("%d",&a);
	printf("\n Enter B :");
	scanf("%d",&b);
	printf("\n A = %d,B = %d",a,b);
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 calculator \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	printf("\n\t\t==============================");
	printf("\n\t\tPress 1. for addition");
	printf("\n\t\tPress 2. for subtraction");
	printf("\n\t\tPress 3. for maltiplaction");
	printf("\n\t\tPress 4. for division");
	printf("\n\t\t==============================");
	printf("\n\t\tEnter your choice ?");
	scanf("%d",&choice);
	
	if(choice==1)
	{
		sum=add(a,b);
		printf("\n\t\tAddition : %d",sum);
	}
    else	if(choice==2)
	{
		sum=sub(a,b);
		printf("\n\tSubtraction : %d",sum);
	}
	else if(choice==3)
	{
		sum=multy(a,b);
		printf("\n\tmultiplaction : %d",sum);
    }
	else if(choice==4)
	{
		sum=div(a,b);
		printf("\n\tDivision : %.2f",((float)sum));
    }
	else
	{
		printf("\tInvalide choice");
	}
   
}