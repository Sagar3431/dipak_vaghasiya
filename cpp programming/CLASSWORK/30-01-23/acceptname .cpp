#include<iostream>

using namespace std;
class Name{
	public:
		string name;
		void getName(string n)
		{
			name=n;
		}
		void putName()
		{
			cout<<"\nYour name Is :"<<name;
		}
};

int main()
{
	Name n;
	string name;
	cout<<"\nEnter name :";
	getline(cin,name);
	n.getName(name);
	n.putName();
	return 0;
}