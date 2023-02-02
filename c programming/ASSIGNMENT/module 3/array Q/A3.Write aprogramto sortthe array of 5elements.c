#include<stdio.h>
//A3.Write aprogramto sortthe array of 5elements

void main()

{
	int rollno[5];
	int i,j,t;
	
	printf("\n\n\t\t\xB\xB2\xB2\xB2\xB2\xB2 element of array :\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<5;i++)	
	{
	printf("\t\t\nEnter the eliment [%d] :",i);
	scanf("%d",&rollno[i]);	
	}
	
	printf("\n\n\t\t\xB\xB2\xB2\xB2\xB2\xB2 eliment at array indax :\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<5;i++)
	{
		printf("\nEnter at index [%d] : %d",i,rollno[i]);
	}
	
	printf("\n\n\t\t\xB\xB2\xB2\xB2\xB2\xB2 array element in ascending order :\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<5;i++)
	{   for(j=i+1;j<5;j++)
	   {
		if(rollno[i]>rollno[j])
		{
			t=rollno[i];
			rollno[i]=rollno[j];
			rollno[j]=t;
	    }
       }  
    }
	
		for(i=0;i<5;i++)
	{
		printf("\nEnter at index [%d] : %d",i,rollno[i]);
	}
	
	printf("\n\n\t\t\xB\xB2\xB2\xB2\xB2\xB2 array element in discending order :\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<5;i++)
	{   for(j=i+1;j<5;j++)
	   {
		if(rollno[i]<rollno[j])
		{
			t=rollno[i];
			rollno[i]=rollno[j];
			rollno[j]=t;
	    }
       }  
    }
	
		for(i=0;i<5;i++)
	{
		printf("\nEnter at index [%d] : %d",i,rollno[i]);
	}
	
}

	
