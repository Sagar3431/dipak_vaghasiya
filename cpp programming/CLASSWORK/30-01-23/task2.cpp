#include<iostream>

using namespace std;
class sample
{
	public:
		int a;
		void getA()
		{
			cout<<"\nEnter A :";
			cin>>a;
		}
	    void putA()
	    {
	    	cout<<"\nA = "<<a;
		}
};
int main()
{
	sample h1;
	h1.getA();
	h1.putA();
	return 0;
}