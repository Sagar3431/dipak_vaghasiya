#include<stdio.h>


int main()

{
	//3. Write a program to make a square and cube of number
	int num, square, cube;
    
    // Taking input
    printf("Enter an integer: ");
    scanf("%d", &num);
    
    // Finding Square
    square = num * num;
    
    // Finding Cube
    cube = num * num * num;
    
    // Displaying result
    printf("Square of %d is: %d \n", num, square);
    printf("Cube of %d is: %d", num, cube);
}