#include<iostream>
using namespace std;
/*
10.Write a program of find the simple interest using constructor with dynamic
initialization. Make constructor like
Interest (int principal, int year, int rate)
Interest (int principal, int year, float rate =2.5)
*/

class bank
{
 private:
     float p;
     float r;
     float t;
     float si;
     float amount;

 public:
    void read ( )
          {
                 cout <<" Enter Principle Amount :: ";
                 cin>>p ;
                 cout<<"\n Enter Rate of Interest :: ";
                 cin>>r;
                 cout <<"\n Enter Number of years :: ";
                 cin>>t;

                 si= (p *r*t) /100;
                 amount = si + p;

          }

    void show( )
         {
                cout<<"\n Entered Details are :: \n";
                cout<<"\n Principle Amount: "<<p;
                cout <<"\n\n Rate of Interest: "<<r;
                cout <<"\n\n Number of years: "<<t;
                cout <<"\n\n Interest : "<<si;
                cout <<"\n\n Total Amount : "<<amount<<"\n";
         }
};


int main ()
{
    bank b ;

    b.read ( );
    b.show ( );

    return 0;
}
