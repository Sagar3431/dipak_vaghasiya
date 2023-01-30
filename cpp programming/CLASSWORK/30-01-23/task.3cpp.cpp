#include<iostream>

using namespace std;
class sample
{
	public:
		int a;
		void getA(int x)
		{
		   a=x;
			
		}
	    void putA()
	    {
	    	cout<<"\nA = "<<a;
		}
};
int main()
{
	sample h1;
	int a;
	cout<<"\nenter A :";
	cin>>a;
	h1.getA(a);
	h1.putA();
	return 0;
}