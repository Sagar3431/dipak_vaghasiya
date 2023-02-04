#include <stdio.h>

 
typedef struct{
    char name[30],adrees;
    int no,age;
    
} Employee;
 
int main()
{
    //number of employees
    int n=5;

    //array to store structure values of all employees
    Employee employees[n];
 
    //Taking each employee detail as input
    printf("Enter %d Employee Details \n \n",n);
    for(int i=0; i<n; i++){
        printf("Employee %d:- \n",i+1);

        //Name
        printf("Name: ");
        scanf("%[^\n]s",employees[i].name);

        //ID
        printf("mobile no: ");
        scanf("%d",&employees[i].no);

        //Salary
        printf("Adrees: ");
        scanf("\n%[^\n]s",&employees[i].adrees);
        
         printf("age: ");
        scanf("%d",&employees[i].age);

        //to consume extra '\n' input
        char ch = getchar();
 
        printf("\n");
    }
 
    //Displaying Employee details
    printf("-------------- All Employees Details ---------------\n");
    for(int i=0; i<n; i++){
        printf("Name \t: ");
        printf("%s \n",employees[i].name);
 
        printf("mobile no \t: ");
        printf("%d \n",employees[i].no);
 
        printf("Salary \t: ");
        printf("%s \n",employees[i].adrees);
        
         printf("age \t: ");
        printf("%d \n",employees[i].age);
 
        printf("\n");
    }
 
    return 0;
}