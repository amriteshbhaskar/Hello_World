#include <stdio.h>

int main()
{
   int t,n;
   scanf("%d",&t);
   for(int i=0;i<t;i++)
   {
   		scanf("%d",&n);
   		int a=1;
   		long int b=1,sum=0,summation=1;
   		for(int j=0;j<n-2;j++)
   		{
   			sum=a+b;
   			a=b;
   			b=sum;
   			if(summation>1000000007)
   				summation=summation%1000000007;
   			summation*=sum;
   		}
   		printf("%ld\n",summation);


   }
 }


