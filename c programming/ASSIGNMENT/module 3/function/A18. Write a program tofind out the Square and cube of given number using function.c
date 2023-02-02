#include <stdio.h>
//A18. Write a program tofind out the Square and cube of given number using function 
int findSquare(int n)
{
    return n * n;
}

int findCube(int n)
{
    return n * n * n;
}

int main()
{
    int no;
    printf("Enter a number : ");
    scanf("%d", &no);

    printf("Square of %d is %d\n", no, findSquare(no));
    printf("Cube of %d is %d\n", no, findCube(no));
}