#include<stdio.h>

void f1()
{
	f2();
	printf("\nFunction1 called .");
}
void f2()
{
	printf("\nFunction2 called .");
}
void main()

{
	printf("\nstart function.");
	f1();
	f2();
	printf("\nend function.");
}