#include<iostream>
using namespace std;
class sample
{ public:
	string name;
	int age;
	sample()
	{
		cout<<"\n default contractor";
	}
	sample(string n,int a)
	{
	    cout<<"\nParameterized constuctor called.";
	    name=n;
	    age=a;
    }
    void show()
    {
    	cout<<"\nName = "<<name;
    	cout<<"\n Age = "<<age;
	}
};



int main()
{
	sample obj1;
	int age;
	string name;
	cout<<"\n enter Name :";
	getline(cin,name);
	cout<<"\nEnter age :";
	cin>>age;
	sample obj2(name,age);
	obj2.show();
	return 0;
}