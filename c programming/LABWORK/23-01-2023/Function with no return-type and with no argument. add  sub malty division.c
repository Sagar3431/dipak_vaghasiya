#include<stdio.h>

void choicecalculator()
{
	int choice,a,b;
	//a=10,b=20;
	printf("\nEnter A = ");
	scanf("%d",&a);
	printf("\nEnter B = ");
	scanf("%d",&b);
	printf("\nInside UDF X = %d, Y = %d",a,b);
	printf("\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2 choice calculator \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
	printf("\n\t\t====================");
	printf("\n\t\tPress 1. for addition");
	printf("\n\t\tPress 2. for subtraction");
	printf("\n\t\tPress 3. for maltiplaction");
	printf("\n\t\tPress 4. for division");
	printf("\n\t\t====================");
	printf("\n\t\tEnter your choice ?");
	scanf("%d",&choice);
	printf("\nInside UDF X = %d, Y = %d",a,b);
    if(choice==1)
    {
    	printf("\nAddition : %d",(a+b));
	}
	else if(choice==2)
	{
    	printf("\nSubtraction : %d",(a-b));	
	}
	else if(choice==3)
	{
	    printf("\nMultiplaction : %d",(a*b));	
	}
	else if(choice==4)
	{
	    printf("\nDivision : %.2f",((float)a/b));	
	}
	else
	{
		printf("\nInvalide input ");
	}
}
void main()
{
		choicecalculator();
		choicecalculator();
		choicecalculator();
		choicecalculator();
}