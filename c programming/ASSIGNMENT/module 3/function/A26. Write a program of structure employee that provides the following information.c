/*A26. Write a program of structure employee that provides the following information
-print and display empno,empname,address and age*/
 
#include <stdio.h>
 
/*structure declaration*/
struct employee{
    char    name[30],address[50];
    int     empId,age;
    float   salary;
};
 
int main()
{
    /*declare structure variable*/
    struct employee emp;
     
    /*read employee details*/
    printf("\nEnter details :\n");
    printf("Name ?:");          gets(emp.name);
    printf("adress ?:");        gets(emp.address);
    printf("ID ?:");            scanf("%d",&emp.empId);
    printf("Salary ?:");        scanf("%f",&emp.salary);
    printf("Age ?:");            scanf("%d",&emp.age);
    
    /*print employee details*/
    printf("\nEntered detail is:");
    printf("\nName: %s"   ,emp.name);
    printf("\nAddress: %s"   ,emp.address);
    printf("\nId: %d"     ,emp.empId);
    printf("\nSalary: %f\n",emp.salary);
    printf("\nAge: %d"     ,emp.age);
    return 0;
}
