#include<iostream>
using namespace std;
/*
21.Assume that a bank maintainstwokinds of accountsfor customer, one called as saving account and
other as current accounts provides Simple interest and withdraw facilities but no cheque book
facility. The current account provides cheque book facility but no interest. Current account holders
should maintain a minimum balance and if the balance falls below this level a service charges is
imposed
Create a class account that stores customer name, account number and type of account.
From this derive classes curr_acc and sav_accttomake them
more specific to theirrequirementsIncludenecessary memberfunctionsin order to achieve the
following tasks
a. Accepts depositfrom a customerand update balance.
b. Display thebalance.
c. Compute and depositinterest.
d. Permit withdraws and updatesthe balance.
e.Check forthe minimumbalance,impose penalty,necessary and update the
balance.
*/

class account 
{
	int acno;
	string name;
	float bal;
	string type;
	public :
		
		void getdata()
		{
			cout<<"\nEnter the Account Number : ";
			cin>>acno;
			cout<<"\nEnter the Name : ";
			cin>>name;
			cout<<"\nEnter the Balance : ";
			cin>>bal;
			cout<<"\nEnter the type of Account : ";
			cin>>type;
		}
		void withdraw();
		void deposit();
		void display();
};

void account :: withdraw()
{
	int x;
	cout<<"Enter the value you want to withdraw : ";
	cin>>x;
	if(x<bal)
	  bal=bal-x;
	else
	  cout<<"Not enough balance : ";
}
void account :: deposit()
{
	int x;
	cout<<"Enter the amount you want to Deposit : ";
	cin>>x;
	bal=bal+x;
}
void account :: display()
{
	cout<<"\nAccount no : "<<acno;
	cout<<"\nName : "<<name;
	cout<<"\nBalance : "<<bal;
	cout<<"\nAccount : "<<type;
}
int main()
{
	account a;
	int ch;
	do
	{
		cout<<"\n==================================";
		cout<<"\nMENU";
		cout<<"\n1.Enter New Account.";
		cout<<"\n2.Withdraw.";
		cout<<"\n3.Deposit.";
		cout<<"\n4.Display.";
		cout<<"\n5.Exit.";
		cout<<"\n=================================";
		cout<<"\nEnter your Choice : ";
		
		cin>>ch;
		switch(ch)
		{
			case 1 :
				a.getdata();
				break;
			case 2 :
				a.withdraw();
				break;
			case 3 :
				a.deposit();
				break;
			case 4 :
				a.display();
				break;
			case 5 :
				exit(0);
				break;
		}
	}
	while(ch!=5);
	return 0;
}











