#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<string.h>
using namespace std;

//declaration of class books
class books
{

//data members of books class
public:
char author[20];
char title[20];
char publisher[50];
int price;
int copies;
int stock;

//setData() function to set data of books
void setData()
{
cout<<"\nEnter the following details:\nAuthor's Name:";
gets(author);
cout<<"\nTitle :";
gets(title);
cout<<"\nPublisher :";
gets(publisher);
cout<<"\nPrice :";
cin>>price;
cout<<"\nNumber of copies:";
cin>>copies;
stock=1;
}

//check() function to check if a book is available or not
void check()
{
char t[20],aut[20];
int cop;
cout<<"\nEnter the following details to search for book:\n";
cout<<"\nTitle of the book:";
gets(t);
cout<<"\nEnter Author's Name :";
gets(aut);
cout<<"\nNumber of copies:";
cin>>cop;
if(strcmp(t,title) & strcmp(aut,author) & (cop<=copies))
{
cout<<"\nBook is availabe in store\nPrice = "<<cop*price;
copies-=cop;
}
else
{
cout<<"Not available";
}
}
};


int main()
{

books bk;
bk.setData();
bk.check();
getch();
return 0;
}