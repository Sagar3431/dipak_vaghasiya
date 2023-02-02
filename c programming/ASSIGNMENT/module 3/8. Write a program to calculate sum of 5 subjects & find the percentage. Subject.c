#include<stdio.h>

void main()


{
	//Q.8 Write a program to calculate sum of 5 subjects & find the percentage. Subject marks entered by user.
	int hindi,english,science,math,computer,sum;
	float per;
	
	printf("Enter mark of hindi =");
	scanf("%d",&hindi);
	printf("Enter mark of english =");
	scanf("%d",&english);
	printf("Enter mark of science =");
	scanf("%d",&science);
	printf("Enter mark of math =");
	scanf("%d",&math);
	printf("Enter mark of computer =");
	scanf("%d",&computer);
	
	sum=hindi+english+science+math+computer;
	printf("sum of mark = %d",sum);
	
	per=(float)sum/5;
	printf("\npercentage of mark=%.2f",per);
}