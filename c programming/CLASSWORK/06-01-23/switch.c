#include<stdio.h>

void main()

{
	int a,b,choice;
	printf("Enter A :");
	scanf("%d",&a);
	printf("Enter B :");
	scanf("%d",&b);
	printf("\nA = %d, B = %d",a,b);
	printf("\n============choice calculator==========");
	printf("\n\npress 1.add\npress 2.subtract\npress 3.multiply\npress 4.division");
	printf("\nEnter your choice ?");
	scanf("%d",&choice);
	switch(choice)
	{
		case 1:printf("\nAddition : %d",(a+b));
		       break;
		case 2:printf("\nsubtract : %d",(a-b));
		       break;
		case 3:printf("\nmultiply : %d",(a*b));
		       break;
		case 4:printf("\ndivision : %,2f",((float)a/b));
		       break;
		default:printf("\nInvalide choice");
		       break;
			   	          
		       
	}
}