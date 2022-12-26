#include<stdio.h>

void main()

{
	int num1=42;
	int num2=23;
	printf("number1=%d \nnumber2%d",num1,num2);
	//printf("\nnumber2=%d,",num2);
	printf("\nAddition: %d",(num1+num2));
	printf("\nSubtraction: %d",(num1-num2));
	printf("\nMultiplication: %d",(num1*num2));
	printf("\nDivision:%.2f",((float)num1/num2));
	
	
}