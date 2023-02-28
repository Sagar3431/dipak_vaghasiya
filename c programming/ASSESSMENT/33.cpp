#include<stdio.h>
int food()
{
	
{

	
	int pizza,burger,dosa,idli,qunty,i;
	char ch,na[50];
	float total,total1,total2,total3,total4;
	int choice = -1;
	

	

		
	printf("\n\n\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Fast food Restorent \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");
	while(1){
	printf("\n\n\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Fast food Menu \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2");	
	printf("\n1.pizza:  price=180/pcs");
	printf("\n2.burger:  price=100/pcs");
	printf("\n3.dosa:  price=120/pcs");
	printf("\n4.idli:  price=50/pcs");
	printf("\nEnter your choice?");
		
		
    
	scanf("%d",&choice);
	if(choice==1)
		{
	      printf("you have selected pizza \n");
		  printf("Enter pizza quantity : ");
		  scanf("%d", &qunty);
		  total1= 180.00 * qunty;
		  printf("Your total amo t is RM%.2f , Please pay at the counter\n ", total1);
		  	printf("\n\t Do you want place more orders? Y/N : ");
		fflush(stdin);
		scanf("%c",&ch);
		
		do
	{
	
	
		
		if(ch=='Y' || ch== 'y' )
		{
			food();
		}
		
		else(ch=='N' || ch== 'n');
		{
		  	  	
		}
		 
	
	}
	while(ch=='Y');
		 
		  
		  
        }
	else if(choice==2)
	{
		  printf("you have selected burger \n");
		  printf("Enter burger quantity : ");
		  scanf("%d", &qunty);
		  total2= 100*qunty,
		  printf("Your totalmount is RM%.2f , Please pay at the counter\n ", total2);
		  	printf("\n\t Do you want place more orders? Y/N : ");
		fflush(stdin);
		scanf("%c",&ch);
		
		do
	{
	
	
		
		if(ch=='Y' || ch== 'y' )
		{
			food();
		}
		
		else(ch=='N' || ch== 'n');
		{
		  	  	
		}
		 
	
	}
	while(ch=='Y');                                                                            
	}
	else if(choice==3)
	{
		  printf("you have selected dosa \n");
		  printf("Enter dosa quantity : ");
		  scanf("%d", &qunty);
		  total3= 120.00*qunty;
		  printf("Your total amo is RM%.2f , Please pay at the counter\n ", total3);
		  	printf("\n\t Do you want place more orders? Y/N : ");
		fflush(stdin);
		scanf("%c",&ch);
		
		do
	{
	
	
		
		if(ch=='Y' || ch== 'y' )
		{
			food();
		}
		
		else(ch=='N' || ch== 'n');
		{
		  	  	
		}
		 
	
	}
	while(ch=='Y');
    }
	else if(choice==4)
	{
		  printf("you have selected idali \n");
		  printf("Enter idli quantity : ");
		  scanf("%d", &qunty);
		  total4 = 50.00 * qunty;
		  printf("Your total amnt is RM%.2f , Please pay at the counter\n ", total4);
		  	printf("\n\t Do you want place more orders? Y/N : ");
		fflush(stdin);
		scanf("%c",&ch);
		
		do
	{
	
	
		
		if(ch=='Y' || ch== 'y' )
		{
			food();
		}
		
		else(ch=='N' || ch== 'n');
		{
		  	  	
		}
		 
	
	}
	while(ch=='Y');
    }
    else
    {
	
		                     
		
		printf("invalid input");
	
	}
	total=total1+total2+total3+total4;
    printf("Total amount%.2f:",(float)total);
	   
	 
	
//	printf("total amount your order %.2f ",((float)total+total+total+total+total));
	//printf("Final total = %.2f",total);
}
  total=total1+total2+total3+total4;
  printf("Total amount%.2f:",(float)total);
	
}
}
int total()
{
    int	total,total1,total2,total3,total4;
	total=total1+total2+total3+total4;
  printf("Total amount%.2f:",(float)total);
}

int main()


{
	food();
	total();
}