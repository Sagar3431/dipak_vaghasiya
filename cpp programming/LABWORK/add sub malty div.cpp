#include<iostream>

using namespace std;
int add(int x,int y)
{   int choice;
	cout<<"\nInside UDF X = %d, Y = %d",x,y;
	cout<<"\n\n\t\t\xB2\xB2\xB2\xB2\xB2\xB2\xB2 choice calculator \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2";
	cout<<"\n\t\t====================";
	cout<<"\n\t\tPress 1. for addition";
	cout<<"\n\t\tPress 2. for subtraction";
	cout<<"\n\t\tPress 3. for maltiplaction";
	cout<<"\n\t\tPress 4. for division";
	cout<<"\n\t\t====================";
	cout<<"\n\t\tEnter your choice ?";
	cin>>choice;
	cout<<"\nInside UDF X = %d, Y = %d",x,y;
    if(choice==1)
    {
    	cout<<"\nAddition : "<<x+y;
	}
	else if(choice==2)
	{
    	cout<<"\nSubtraction : "<<x-y;	
	}
	else if(choice==3)
	{
	    cout<<"\nMultiplaction : "<<x*y;	
	}
	else if(choice==4)
	{
	    cout<<"\n Division : "<<((float)x/y);
	}
	else
	{
		cout<<"\nInvalide input ";
	}

}
int main()
{	
	int a,b;//a=10,b=20;
	cout<<"\nEnter A = ";
	cin>>a;
	cout<<"\nEnter B = ";
	cin>>b;
    cout<<"\nInside Main A = %d, B = %d"<<a,b;
	cout<<"\nStart Function";
	add(a,b);
	cout<<"\nStop Function";
	return 0;
}