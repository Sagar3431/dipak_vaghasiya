#include<stdio.h>

void main()


{
	//10. Write a Program to check the given number is Positive, Negative. 
    int num;
    printf("Enter your num:");
    scanf("%d",&num);
 
    if(num == 0)
        printf("Neither positive nor negative");
    else if(num < 0)
        printf("Negative");
    else
        printf("Positive");
}