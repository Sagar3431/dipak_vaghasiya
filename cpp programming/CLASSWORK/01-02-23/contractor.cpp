#include<iostream>
using namespace std;

class sample
{
	public:
		sample()
		{
			cout<<"\nDefault contructor called.";
		}
		void show()
		{
			cout<<"\nThis is show mathod.";
		}
};
int main()
{
	sample obj1;
	obj1.show();
	return 0;
}