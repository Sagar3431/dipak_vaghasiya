#include<iostream>

using namespace std;
class box
{
	public:
		double width,depth,height;
		box()
		{
			cout<<"\n\nDEfalt constructor called.";
			width=4;
			depth=5;
			height=3;
		}
		box(double w,double h,double d)
		{
			cout<<"\n\nparamiterrize contractor called.";
			width=w;
			depth=d;
			height=h;
		}
		box(const box &tops)
		{
			cout<<"\n\n copy contractor called.";
			width=tops.width;
			depth=tops.depth;
			height=tops.height;
		}
		void volume()
		{
			cout<<"\n\ndesplay contractor."<<(width*height*depth);
		}
};

int main()
{
	box b1;
	b1.volume();
	
	box b2(5,7,3);
	b2.volume();
	
	box b3(4,6,8);
	b3.volume();
	
	box b4(b2);
	b4.volume();
	
	return 0;
}