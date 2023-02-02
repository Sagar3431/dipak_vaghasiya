#include<stdio.h>
/*14. Write a program to find the Max number from the given three number using
Ternary Operator*/
void main()
{
	int //a=64,b=54;
	 nu1,nu2,nu3,max;
	printf("Enter is value num1=");
	scanf("%d",&nu1);
	printf("\nEnter is  num2=");
	scanf("%d",&nu2);
	printf("\nEnter is  num3=");
	scanf("%d",&nu3);
	
    max=(nu1>nu2)?
          (nu1 > nu3 ? printf("nu1 is Greater") : printf("nu3 is greater")) :
          (nu2 > nu3 ? printf("nu2 is Greater") : printf("nu3 is greater"));
}