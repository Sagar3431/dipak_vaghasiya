#include<iostream>
using namespace std;

class demo{
	public:
	void func();
};
void demo::func()
{
	cout<<"\n function implyment out side the class.";
}

int main()
{
	demo obj;
	obj.func();
	return 0;
}