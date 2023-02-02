#include <stdio.h>  
#include <conio.h>
/*20. PyramidPrograms 
3)
 1
2 2
3 3 3
4 4 4 4
5 5 5 55*/ 
int main()  
{  
    // declare the local variables  
    int i, j, rows;  
    printf (" Enter a number to define the rows: \n ");  
    scanf("%d", &rows);   
    printf("\n");  
    for (i = 1; i <= rows; ++i)   
    {  
        for (j = 1; j <= i; ++j)   
        {  
            printf ("%d ", i); // print the number  
        }  
        printf ("\n");   
    }  
    getch();      
}  