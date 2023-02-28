#include<iostream>
//1. Writeaprogram of Fibonacci and factorial using Class
using namespace std;

class FibonacciSeries
{
	public:
		int fib, term_one, term_two;
		void generateFibonacci(int range);
};

void FibonacciSeries::generateFibonacci(int range)
{
	if(range == 0)
	{
		cout << "Cannot generate series" << endl;
		exit(0);
	}
	term_one = 0;
	term_two = 1;
	
	cout << "Fibonacci Series" << endl;
	if(range == 1)
		cout << term_one;
	else if(range >= 2)
	{
		cout << term_one << "\t" << term_two;
		for(int i = 0; i < range - 2; i++)
		{
			int fib = term_one + term_two;
			cout << "\t" << fib;
			term_one = term_two;
			term_two = fib;
		}
	}
	cout << endl;
}

int main()
{
	int range;
	cout << "Enter the range of fibonacci serics" << endl;
	cin >> range;

	FibonacciSeries fibSeries;
	fibSeries.generateFibonacci(range);

	return 0;
}
