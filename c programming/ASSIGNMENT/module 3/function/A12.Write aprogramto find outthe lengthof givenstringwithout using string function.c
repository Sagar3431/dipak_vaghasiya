// A12.Write aprogramto find outthe lengthof givenstringwithout using string function
#include <stdio.h>
#include <string.h>

int main()
{
	char Str[1000];
	int i;

	printf("Enter the String: ");
	scanf("%s", Str);

	for (i = 0; Str[i] != '\0'; ++i);

	printf("Length of Str is %d", i);

	return 0;
}
