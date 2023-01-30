#include<stdio.h>

struct student
{
	int rollno;
	char name[20];
	float par;
};
void main()
{
	struct student b1;
	printf("\nEnter student Rollno :");
	scanf("%d",&b1.rollno);
	printf("\nEnter student Name :");
	scanf("%s",&b1.name);
	fflush(stdin);
	printf("\nEnter student Per :");
	scanf("%f",&b1.par);
	
	printf("\nstudent Rollno : %d",b1.rollno);
	printf("\nstudent Name : %s",b1.name);
	printf("\nstudent Per : %.2f",b1.par);
}