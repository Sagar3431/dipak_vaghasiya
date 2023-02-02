#include<stdio.h>

void main()

{
  //13.Write a program to find the Max number from the given three number usingNested If. 
  double n1, n2, n3;
  printf("Enter your n1=");
  scanf("%lf",&n1);
  printf("Enter your n2=");
  scanf("%lf",&n2);
  printf("Enter your n3=");
  scanf("%lf",&n3);

  // if n1 is greater than both n2 and n3, n1 is the largest
  if (n1 >= n2 && n1 >= n3)
    printf("%.2f is the largest number.", n1);

  // if n2 is greater than both n1 and n3, n2 is the largest
  if (n2 >= n1 && n2 >= n3)
    printf("%.2f is the largest number.", n2);

  // if n3 is greater than both n1 and n2, n3 is the largest
  if (n3 >= n1 && n3 >= n2)
    printf("%.2f is the largest number.", n3);
}