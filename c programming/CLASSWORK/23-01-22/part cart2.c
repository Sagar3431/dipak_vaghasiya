#include<stdio.h>

void swap(int n1,int n2)
{
	int t;
	t=n1;
	n1=n2;
	n2=t;
	printf("\nIn swap A= %d,B=%d",n1,n2);
}
void main()
{
	int a,b;
	printf("\nEnter A=");
	scanf("%d",&a);
	printf("\nEnter B=");
	scanf("%d",&b);
	printf("\nIn side main A= %d,b= %d",a,b);
	printf("\nstart the function");
	swap(a,b);
	printf("\nEnd the function");
	
}