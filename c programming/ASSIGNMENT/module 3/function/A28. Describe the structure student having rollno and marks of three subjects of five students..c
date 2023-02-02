#include<stdio.h>
struct student
{
	int rollno,english,math,computer,total;
	char name[20];
	float marks,per;
	
};
void main()
{    
    int i;
    for(i=0;i<5;i++)
    {
	
	struct student s[i];
	printf("\nEnter roll No: ");
	scanf("%d",&s[5].rollno);
	printf("\nEnter name : ");
	gets(s[5].name);
	scanf("%s",&s[5].name);
	fflush(stdin);
	printf("\nEnter English mark :");
	scanf("%d",&s[5].english);
	printf("\nEnter math mark :");
	scanf("%d",&s[5].math);
	printf("\nEnter computer mark :");
	scanf("%d",&s[5].computer);
	s[5].total=s[5].english+s[5].math+s[5].computer;
	printf("\n total marks : %d",s[5].total);
	s[5].per=s[5].total/3;
	printf("\n parsantange : %.2f",s[5].per);
	printf("\nclass :");
	if(s[5].per>=75)
	{
		printf("\ndistinction");
	}
	else if(s[5].per>=60)
	{
		printf("\nFirst class");
	}
	else if(s[5].per>=50)
	{
	    printf("\nSecond class");	
	}
	else if(s[5].per>=40)
	{
		printf("\npass");
	}
	else
	{
		printf("\nfail");
	}
	printf("\n\n\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2 result \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
	printf("\nRoll no : %d",s[5].rollno);
	printf("\nName : %s",s[5].name);
	printf("\nEnglis mark : %d",s[5].english);
	printf("\nMath mark : %d",s[5].math);
	printf("\nComputer mark : %d",s[5].computer);
	printf("\ntotal marks : %d",s[5].total);
	printf("\nparsantage : %.2f",s[5].per);
    }
    
	
}
