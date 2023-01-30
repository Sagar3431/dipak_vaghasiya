#include<stdio.h>

union employee
{
	int eid;
	char name[20];
	float salary;
	
};
void main()
{
	union employee e1;
	printf("\n\nEnter employee id : ");
	scanf("%d",&e1.eid);
	printf("Employee Id : %d",e1.eid);
    fflush(stdin);
	printf("\n\nEnter employee Name :" );
	scanf("%s",&e1.name);
	printf("\Name : %s",e1.name);
    fflush(stdin);
	printf("\n\nEnter Employee Salary : ");
	scanf("%f",&e1.salary);
	printf("Salary : %.2f",e1.salary);
	
		printf("\nSize of Union is %d Bytes",sizeof(e1));
}